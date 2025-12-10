import os
import requests
from flask import Flask, request, render_template

app = Flask(__name__)

# Leer el socket de la API FastAPI desde variable de entorno
FASTAPI_SOCKET = os.getenv("FASTAPI_SOCKET", "http://127.0.0.1:8000")


@app.route("/", methods=["GET"])
def home():
    return render_template("form.html")


@app.route("/predict", methods=["POST"])
def predict():

    # Convertir los datos del formulario a dict con el formato requerido por FastAPI
    payload = [{
        "hours_studied": int(request.form["hours_studied"]),
        "previous_scores": int(request.form["previous_scores"]),
        "extracurricular_activities": True if request.form.get("extracurricular_activities") == "on" else False,
        "sleep_hours": int(request.form["sleep_hours"]),
        "sample_question_papers_practiced": int(request.form["sample_question_papers_practiced"])
    }]

    # Endpoints
    url_class = f"{FASTAPI_SOCKET}/predict/classification/best"
    url_reg = f"{FASTAPI_SOCKET}/predict/regression/best"

    # Llamada a clasificación/best
    r1 = requests.post(url_class, json=payload)
    classification = r1.json() if r1.status_code == 200 else f"Error: {r1.text}"

    # Llamada a regresión/best
    r2 = requests.post(url_reg, json=payload)
    regression = r2.json() if r2.status_code == 200 else f"Error: {r2.text}"

    return render_template(
        "form.html",
        classification=classification,
        regression=regression
    )


if __name__ == "__main__":
    app.run(port=5000, debug=True)
