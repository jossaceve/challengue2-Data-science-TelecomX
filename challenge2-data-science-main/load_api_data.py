# ==========================================
# Telecom X - Carga de datos desde API
# ==========================================

import requests
import pandas as pd

# URL de la API con datos en JSON
API_URL = "https://raw.githubusercontent.com/ingridcristh/challenge2-data-science/main/TelecomX_Data.json"


def cargar_datos_api(url):
    """
    Extrae datos desde una API en formato JSON
    y los convierte en un DataFrame de Pandas.
    """

    try:
        response = requests.get(url)
        response.raise_for_status()

        data_json = response.json()

        # Convertir JSON a DataFrame
        df = pd.json_normalize(data_json)

        print("Datos cargados correctamente desde la API")
        print(f"Registros: {df.shape[0]}")
        print(f"Columnas: {df.shape[1]}")

        return df

    except requests.exceptions.RequestException as e:
        print("Error al conectar con la API:", e)
        return None


def main():

    df = cargar_datos_api(API_URL)

    if df is not None:

        print("\nPrimeras filas del dataset:\n")
        print(df.head())

        # Guardar copia local del dataset
        df.to_csv("data/telecomx_dataset.csv", index=False)

        print("\nDataset guardado en data/telecomx_dataset.csv")


if __name__ == "__main__":
    main()