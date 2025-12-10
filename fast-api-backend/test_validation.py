# test_app.py
import json
from fastapi.testclient import TestClient
from main import app  # <-- replace with your file name if different

client = TestClient(app)


def test_predict_endpoint():
    # Example request payload
    payload = [
        {
            "hours_studied": 7,
            "previous_scores": 99,
            "extracurricular_activities": 1,
            "sleep_hours": 9,
            "sample_question_papers_practiced": True
        }
    ]

    # Call endpoint
    response = client.post(
        "/predict/regression/best",
        content=json.dumps(payload)
    )

    # Basic validation
    assert response.status_code == 200
    data = response.json()

    # Check keys exist
    assert "type_model" in data
    assert "model_name" in data
    assert "prediction" in data

    # prediction should be a list
    assert isinstance(data["prediction"], list)
