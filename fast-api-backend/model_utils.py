import anyio
import json
from datetime import datetime, timedelta, timezone
from functools import lru_cache, wraps

import mlflow
from mlflow.tracking import MlflowClient

from core import MLFLOW_EXPERIMENT_NAME, MLFLOW_SERVER, MLFLOW_TRACKING_URI
# from core import MINIO_ACCESS_KEY, MINIO_SECRET_KEY, MINIO_BUCKET_NAME


mlflow.set_tracking_uri(MLFLOW_SERVER)
# mlflow.set_experiment(MLFLOW_EXPERIMENT_NAME)



def timed_lru_cache(seconds: int, maxsize: int = 128):
    def wrapper_cache(func):
        func = lru_cache(maxsize=maxsize)(func)
        func.expiration = datetime.now(timezone.utc) + timedelta(seconds=seconds)

        @wraps(func)
        def wrapped_func(*args, **kwargs):
            if datetime.now(timezone.utc) >= func.expiration:
                func.cache_clear()
                func.expiration = datetime.now(timezone.utc) + timedelta(seconds=seconds)
            return func(*args, **kwargs)
        return wrapped_func
    return wrapper_cache


@lru_cache(maxsize=128)
def _load_model_sync(type_model: str, run_name: str | None = None):

    order_str = None
    if type_model == "classification":
        order_str = "metrics.roc_auc DESC"
    elif type_model == "regression":
        order_str = "metrics.f1 DESC"
    else:
        raise ValueError("Invalid type param")

    experiment = mlflow.search_experiments(filter_string=f"name='{MLFLOW_EXPERIMENT_NAME}_{type_model}'")[0]

    if run_name is not None:
        runs = mlflow.search_runs(
            experiment_ids=[experiment.experiment_id],
            filter_string=f"tags.mlflow.runName = '{run_name}'",
            order_by=[order_str]
        )
        if runs.shape[0] == 0:
            raise ValueError(f"No se encontró ningún run con el nombre: {run_name}")
    else:
        runs = mlflow.search_runs(
            experiment_ids=[experiment.experiment_id],
            order_by=[order_str]
        )
        if runs.shape[0] == 0:
            raise ValueError(f"No se encontró ningún run")

    selected_run = runs.iloc[0]
    # print(selected_run)
    run_id = selected_run['run_id']
    # print(run_id)
    model_uri = f"runs:/{run_id}/model"

    # Cargar el modelo
    # print(MINIO_ACCESS_KEY, MINIO_SECRET_KEY, MINIO_BUCKET_NAME)
    # model = mlflow.sklearn.load_model(selected_run['artifact_uri'])
    model = mlflow.sklearn.load_model(model_uri)
    return model


async def load_model_from_mlflow(type_model: str, run_name: str | None = None):
    """
    Async wrapper around a sync MLflow model loader.
    """
    return await anyio.to_thread.run_sync(_load_model_sync, type_model, run_name)
