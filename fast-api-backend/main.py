from typing import Literal, List

import numpy as np
import pandas as pd

import sklearn

from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel, Field


from model_utils import load_model_from_mlflow

app = FastAPI(title="MLflow Prediction API")



class FeatureInput(BaseModel):
    hours_studied: float
    previous_scores: float
    extracurricular_activities: bool
    sleep_hours: float
    sample_question_papers_practiced: float



@app.post("/predict/{type_model}/{model_name}")
async def predict(type_model: Literal["classification", "regression"] = Path(..., description="'classification' o 'regression'"),
            model_name: str = Path(..., description="Nombre del modelo (run name en MLflow)"),
            features: List[FeatureInput] = ...):
    
    if model_name == 'best':
        model_name = None
    
    try:
        loaded_model = await load_model_from_mlflow(type_model, model_name)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

    # Convertimos los datos a DataFrame
    input_df = pd.DataFrame([item.model_dump() for item in features])

    # Realizamos la predicción
    try:
        prediction = loaded_model.predict(input_df.to_dict(orient='records'))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al predecir: {str(e)}")

    return {"type_model": type_model, "model_name": model_name, "prediction": prediction.tolist()}

