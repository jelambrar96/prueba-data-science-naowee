# Prueba Técnica para Científicos de Datos

Este repositorio contiene la solución a una prueba técnica para científicos de datos, que abarca desde el análisis de datos hasta el desarrollo de un producto de datos completo, incluyendo modelos de machine learning y una API para su consumo.

## Objetivo de la Prueba

El objetivo es resolver dos casos prácticos:

1.  **Resultados Mundiales de Fútbol Femenino:** Analizar datos históricos de partidos para identificar tendencias, equipos destacados y la evolución competitiva del torneo.
2.  **Desempeño de Estudiantes de Matemáticas:** Analizar factores que afectan el rendimiento académico y desarrollar un modelo predictivo para identificar estudiantes con bajo desempeño.

## Componentes del Proyecto

Este repositorio está estructurado como un sistema de microservicios orquestado con Docker Compose. A continuación se describen los componentes principales:

-   **`notebooks/`**: Contiene los Jupyter Notebooks donde se realiza el análisis exploratorio de datos (EDA) para ambos casos prácticos, así como el entrenamiento y registro de los modelos de machine learning.
-   **`fast-api-backend/`**: Una aplicación en FastAPI que sirve los modelos de machine learning entrenados. Expone un endpoint para realizar predicciones.
-   **`flask-frontend/`**: Una aplicación web en Flask que proporciona una interfaz de usuario sencilla para interactuar con la API de FastAPI, permitiendo a los usuarios introducir datos y ver las predicciones del modelo.
-   **`mlflow/`**: Contenedor para el servicio de MLflow, una plataforma de código abierto para gestionar el ciclo de vida del machine learning. Se utiliza para el seguimiento de experimentos, registro de modelos y artefactos.
-   **`minio/`**: Un servicio de almacenamiento de objetos compatible con Amazon S3. MLflow lo utiliza como backend para almacenar los artefactos de los modelos.
-   **`postgres/`**: Una base de datos PostgreSQL que sirve como backend para el tracking de experimentos y modelos de MLflow.

## Herramientas y Tecnologías

-   **Lenguaje de Programación:** Python
-   **Análisis de Datos:** Pandas, Scikit-learn, Jupyter
-   **Desarrollo de API:** FastAPI
-   **Frontend Web:** Flask
-   **Orquestación de Contenedores:** Docker, Docker Compose
-   **Ciclo de Vida de ML:** MLflow
-   **Almacenamiento de Artefactos:** MinIO
-   **Base de Datos (MLflow):** PostgreSQL

## Cómo Ejecutar el Proyecto

Sigue estos pasos para configurar y ejecutar todo el entorno en tu máquina local.

### 1. Pre-requisitos

-   Tener Docker y Docker Compose instalados.

### 2. Configuración del Entorno

1.  **Clona este repositorio:**
    ```bash
    git clone <url-del-repositorio>
    cd <nombre-del-repositorio>
    ```

2.  **Crea el archivo `.env`:**
    Copia el contenido de `sample.env` a un nuevo archivo llamado `.env`.
    ```bash
    cp sample.env .env
    ```

3.  **Configura las variables de entorno:**
    Abre el archivo `.env` y reemplaza los valores de ejemplo con tus propias credenciales y nombres. Por ejemplo:
    ```env
    MINIO_ACCESS_KEY=minioadmin
    MINIO_SECRET_KEY=minioadmin
    MINIO_BUCKET_NAME=mlflow-bucket

    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    POSTGRES_DB=mlflow_db
    POSTGRES_HOST=postgres
    POSTGRES_PORT=5432

    MLFLOW_EXPERIMENT_NAME=student-performance

    JUPYTER_TOKEN=your-secure-token
    ```

### 3. Ejecutar con Docker Compose

Una vez que el archivo `.env` esté configurado, puedes levantar todos los servicios con un solo comando:

```bash
docker-compose up --build
```

El flag `--build` es importante para construir las imágenes de los servicios la primera vez que se ejecutan.

### 4. Acceder a los Servicios

Una vez que todos los contenedores estén en funcionamiento, podrás acceder a los diferentes componentes a través de tu navegador:

-   **Jupyter Notebook:** `http://localhost:8888` (usa el token que configuraste en `.env`)
-   **MLflow:** `http://localhost:5000`
-   **MinIO Console:** `http://localhost:9001` (usa el access y secret key de `.env`)
-   **FastAPI (Documentación Swagger):** `http://localhost:8000/docs`
-   **Flask Frontend:** `http://localhost:5001`
