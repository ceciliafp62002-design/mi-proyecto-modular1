import os
from kaggle.api.kaggle_api_extended import KaggleApi


def descargar_dataset_kaggle(slug: str, destino: str) -> str:
    """
    Descarga un dataset de Kaggle y lo descomprime en la carpeta destino.

    slug    -> identificador 'owner/dataset' de Kaggle.
    destino -> ruta absoluta donde dejar el CSV (típicamente data/raw).
    """
    os.makedirs(destino, exist_ok=True)   # crea data/raw si no existe
    api = KaggleApi()                     # objeto que habla con Kaggle
    api.authenticate()                    # lee  ~/.kaggle/access_token y te valida
    api.dataset_download_files(slug, path=destino, unzip=True)
    return destino