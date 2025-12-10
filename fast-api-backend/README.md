# API de Predicción con MLflow

Esta API sirve como puente para un modelo de machine learning gestionado por MLflow, permitiendo realizar predicciones a través de una interfaz RESTful.

## Cómo funciona

La aplicación carga un modelo desde MLflow y expone un endpoint para realizar predicciones. El tipo de modelo (clasificación o regresión) y su nombre se especifican en la URL de la solicitud.

## Endpoint

### `/predict/{type_model}/{model_name}`

- **Método:** `POST`
- **Descripción:** Realiza una predicción utilizando el modelo especificado desde MLflow.

#### Parámetros de Ruta

- `type_model` (string, requerido): El tipo de modelo a utilizar. Debe ser `'classification'` o `'regression'`.
- `model_name` (string, requerido): El nombre del modelo (nombre de la ejecución o "run name" en MLflow) a utilizar para la predicción. Use `'best'` para cargar el mejor modelo.

#### Cuerpo de la Solicitud (Request Body)

Un array JSON de objetos de características. Cada objeto debe contener las siguientes claves:

- `hours_studied` (float)
- `previous_scores` (float)
- `extracurricular_activities` (float)
- `sleep_hours` (float)
- `sample_question_papers_practiced` (boolean)

#### Ejemplo de Solicitud

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
