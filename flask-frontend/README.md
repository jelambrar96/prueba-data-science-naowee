# Frontend Flask para API de Predicción

Esta aplicación web, construida con Flask, proporciona una interfaz de usuario para interactuar con la API de predicción de FastAPI.

## Descripción General

El propósito de esta aplicación es ofrecer un formulario web sencillo donde un usuario puede introducir datos, enviarlos a la API de backend para obtener predicciones de modelos de machine learning (clasificación y regresión), y ver los resultados directamente en la página.

## Funcionamiento

La aplicación Flask renderiza un formulario HTML. Cuando el usuario completa y envía el formulario, la aplicación:
1.  Recopila los datos del formulario.
2.  Los formatea en el payload JSON esperado por la API de FastAPI.
3.  Realiza dos solicitudes `POST` a la API de backend: una para el modelo de clasificación (`/predict/classification/best`) y otra para el modelo de regresión (`/predict/regression/best`).
4.  Recibe las respuestas de la API.
5.  Vuelve a renderizar el formulario, mostrando los resultados de la predicción obtenidos.

## Cómo Ejecutar la Aplicación

1.  **Instalar dependencias:**
    Asegúrate de tener las dependencias listadas en `environment.yml` instaladas en tu entorno.

2.  **Configurar la API de Backend:**
    Esta aplicación necesita saber la dirección de la API de FastAPI. Esta se configura a través de la variable de entorno `FASTAPI_SOCKET`. Si no se especifica, se usará el valor por defecto `http://127.0.0.1:8000`.

    ```bash
    export FASTAPI_SOCKET="http://<direccion_de_tu_api_fastapi>"
    ```

3.  **Iniciar la aplicación:**
    Puedes ejecutar la aplicación directamente con Python:

    ```bash
    python app.py
    ```
    La aplicación estará disponible en `http://127.0.0.1:5000`.

## Rutas

-   **`/`**
    -   **Método:** `GET`
    -   **Descripción:** Muestra el formulario web principal para introducir los datos de predicción.

-   **`/predict`**
    -   **Método:** `POST`
    -   **Descripción:** Endpoint que recibe los datos del formulario. Se comunica con la API de FastAPI para obtener las predicciones y muestra los resultados en la página.
