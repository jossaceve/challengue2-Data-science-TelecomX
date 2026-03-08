# Telecom X – Análisis de Evasión de Clientes 

## Descripción del Proyecto

Este proyecto analiza la **evasión de clientes (Churn)** en una empresa ficticia de telecomunicaciones llamada **Telecom X**.
El objetivo principal es identificar patrones y factores que influyen en la cancelación de servicios por parte de los clientes.

Para lograrlo se implementa un proceso de **ETL (Extract, Transform, Load)** utilizando Python, donde los datos se extraen desde una **API en formato JSON**, se transforman y limpian con **Pandas**, y posteriormente se realiza un **Análisis Exploratorio de Datos (EDA)** para generar insights estratégicos.

El análisis permite comprender mejor el comportamiento de los clientes y proponer estrategias que ayuden a reducir la tasa de cancelación.

---

# Objetivos

* Extraer datos de clientes desde una **API en formato JSON**.
* Convertir los datos en un **DataFrame de Pandas** para su análisis.
* Realizar **limpieza y transformación de datos**.
* Analizar variables relacionadas con la evasión de clientes.
* Identificar **patrones de churn** en variables categóricas y numéricas.
* Generar **conclusiones e insights de negocio**.

---

# Tecnologías Utilizadas

* Python 3
* Pandas
* NumPy
* Requests
* Matplotlib
* Seaborn
* Jupyter Notebook

---

# Estructura del Proyecto

```
Telecom-X

├── data/
│   └── .csv
│
├── notebooks/
│   └── .ipynb
│
├── src/
│   └── .py
│
├── reports/
│   └── .md
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Extracción de Datos desde la API

Los datos del proyecto se encuentran en formato **JSON** y son cargados directamente desde una API utilizando Python.

Ejemplo de código para obtener los datos:

```python
import requests
import pandas as pd

url = "https://raw.githubusercontent.com/ingridcristh/challenge2-data-science/main/TelecomX_Data.json"

response = requests.get(url)
data = response.json()

df = pd.json_normalize(data)
print(df.head())
```

Este proceso convierte los datos JSON en un **DataFrame de Pandas**, lo que facilita su manipulación y análisis.

---

# Proceso de Análisis de Datos

El proyecto sigue las siguientes etapas:

### 1. Extracción

* Carga de datos desde la API en formato JSON.
* Conversión de los datos a DataFrame.

### 2. Transformación

* Limpieza de datos.
* Normalización de columnas.
* Conversión de variables categóricas y numéricas.
* Manejo de valores nulos.

### 3. Análisis Exploratorio de Datos (EDA)

Se analizan diferentes variables para comprender el comportamiento del churn:

* Tipo de contrato
* Método de pago
* Antigüedad del cliente
* Cargos mensuales
* Cargos totales

Se generan gráficos y visualizaciones para identificar patrones.

---

# Principales Resultados

Los resultados del análisis muestran que:

* Los clientes con **contratos mes a mes** presentan mayor probabilidad de cancelar el servicio.
* Los clientes con **menor antigüedad** tienen mayor tasa de churn.
* Los **cargos mensuales altos** están asociados con mayor evasión.
* Los **métodos de pago automáticos** presentan menor tasa de cancelación.

Estos resultados permiten identificar segmentos de clientes con mayor riesgo de abandono.

---

# Recomendaciones

A partir del análisis realizado, se proponen las siguientes estrategias:

**1. Programas de fidelización para nuevos clientes**
Ofrecer beneficios o descuentos durante los primeros meses.

**2. Promoción de contratos a largo plazo**
Incentivar planes anuales con beneficios adicionales.

**3. Optimización de planes de precio**
Analizar si los cargos mensuales elevados generan percepción negativa en los clientes.

**4. Incentivar métodos de pago automáticos**
Estos métodos muestran menor tasa de cancelación.

---

# Cómo Ejecutar el Proyecto

### 1. Clonar el repositorio

```
git clone https://github.com/tuusuario/TelecomX.git
```

### 2. Instalar dependencias

```
pip install -r requirements.txt
```

### 3. Ejecutar la carga de datos desde la API

```
python src/load_api_data.py
```

### 4. Abrir el notebook

```
jupyter notebook notebooks/Telecom_X_Alura.ipynb
```

---

# Reproducibilidad

Todos los análisis pueden reproducirse ejecutando el notebook incluido en el repositorio.
El dataset se obtiene directamente desde la API, por lo que no es necesario descargar archivos manualmente.

---

# Autor

Proyecto desarrollado como parte de un ejercicio de **análisis de datos y ciencia de datos**, enfocado en el estudio en empresas de telecomunicaciones.

---

# Licencia

Este proyecto es de uso educativo
