# Usa una imagen base de Miniconda para una gestión eficiente del entorno
FROM continuumio/miniconda3:23.10.0-1

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instala dependencias del sistema si son necesarias (ej. git, build-essential)
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    build-essential && \
    rm -rf /var/lib/apt/lists/*

# Copia el archivo de entorno Conda
COPY environment.yml .

# Crea el entorno Conda desde el archivo YAML
RUN conda env create -f environment.yml --name jupyter_env

# Activa el entorno, instala ipykernel para que Jupyter lo detecte y limpia la caché de conda
# El entorno 'jupyter_env' debe contener duckdb, jupyter notebook y otras dependencias.
# Se asume que estos paquetes están listados en el archivo environment.yml.
RUN conda run -n jupyter_env pip install ipykernel && \
    conda clean -all -f -y

# Configura variables de entorno para Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# Define la variable de entorno PATH para incluir los binarios del entorno conda
ENV PATH="/opt/conda/envs/jupyter_env/bin:$PATH"

# Copia el resto de archivos de tu proyecto al directorio de trabajo
COPY . .

# Expone el puerto por defecto de Jupyter
EXPOSE 8888

# Comando para ejecutar el servidor Jupyter Notebook usando la variable de entorno JUPYTER_TOKEN
# Utilizamos la "shell form" de CMD para que las variables de entorno se expandan correctamente.
CMD ["/bin/bash", "-c", "conda run -n jupyter_env jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root --NotebookApp.token=${JUPYTER_TOKEN}"]
