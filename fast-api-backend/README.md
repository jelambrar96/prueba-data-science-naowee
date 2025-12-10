# MLflow Prediction API

This API provides a bridge to a machine learning model managed by MLflow, allowing predictions to be made via a RESTful interface.

## How it works

The application loads a model from MLflow and exposes an endpoint to perform predictions. The model type (classification or regression) and its name are specified in the request URL.

## Endpoint

### `/predict/{type_model}/{model_name}`

- **Method:** `POST`
- **Description:** Makes a prediction using the specified model from MLflow.

#### Path Parameters

- `type_model` (string, required): The type of model to use. Must be either `'classification'` or `'regression'`.
- `model_name` (string, required): The name of the model (run name in MLflow) to use for the prediction. Use `'best'` to load the best model.

#### Request Body

A JSON array of feature objects. Each object must contain the following keys:

- `hours_studied` (float)
- `previous_scores` (float)
- `extracurricular_activities` (float)
- `sleep_hours` (float)
- `sample_question_papers_practiced` (boolean)

#### Example Request

```bash
curl -X 'POST' \
  'http://localhost:8000/predict/regression/best' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '[
  {
    "hours_studied": 8,
    "previous_scores": 85,
    "extracurricular_activities": 1,
    "sleep_hours": 7,
    "sample_question_papers_practiced": true
  }
]'
```
