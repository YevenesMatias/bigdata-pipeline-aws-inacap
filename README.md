# bigdata-pipeline-aws-inacap
Pipeline de Big Data de Alta Disponibilidad en AWS (S3, Glue, Athena, PySpark ML)

# Pipeline de Big Data de Alta Disponibilidad en AWS (INACAP 2026)

**Asignatura:** Big Data (TI13025)  
**Evaluación:** Evaluación Sumativa 02 (25%)  
**Institución:** IP INACAP – Sede Punta Arenas  
**Docente:** Paulo Simunovic Oyarzún  

### Integrantes:
* **Matías Yévenes Martínez** (Cloud Architecture & Data Engineering)
* **Derek Pagels** (Data Analysis & ML Engineering)

---

## 📌 Descripción del Proyecto
Diseño e implementación de un pipeline de Big Data de alta disponibilidad y desacoplado en la nube (AWS Free Tier / Learner Lab) para el procesamiento, análisis distribuido y modelamiento predictivo del dataset oficial de viajes de **NYC Taxi & Limousine Commission (TLC)** con más de 2.9 millones de registros.

## 🏗️ Arquitectura de la Solución
* **Ingesta y Procesamiento Distribuido:** Google Colab con **Apache PySpark 3.5**.
* **Almacenamiento (Data Lake):** **Amazon S3** (`s3://bigdata-ev2-myevenes-dpagels/`) con particionamiento temporal (`year=2024/month=1/`) en formato columnar comprimido (**Parquet / Snappy**).
* **Catálogo y Gobierno:** **AWS Glue Crawler** (`crawler-nyc-taxi`) gobernado por `LabRole` (IAM), catalogado en la base de datos `db_bigdata_nyc`.
* **Exploración Masiva (EDA Distribuido):** **Amazon Athena** (Trino/Presto Engine Serverless) con latencias de 1.066 seg y escaneos de 367 KB.
* **Modelamiento Predictivo:** **PySpark ML** (`pyspark.ml`) utilizando `RandomForestRegressor`.

## 📊 Métricas de Rendimiento del Modelo de ML
* **$R^2$ (Coeficiente de Determinación):** `0.9055` (explica el 90.55% de la varianza)
* **RMSE (Error Cuadrático Medio):** `$7.71 USD`
* **MAE (Error Absoluto Medio):** `$4.29 USD`

## 📂 Estructura del Repositorio
* `/notebooks`: Notebook principal con la ejecución de PySpark, ETL y Random Forest.
* `/sql`: Consultas analíticas distribuidas ejecutadas en Amazon Athena.
* `/scripts`: Script automatizado de carga y particionado hacia Amazon S3.

## 👥 División de Roles y Trabajo en Equipo (Criterio 2.1.4)
* **Matías Yévenes:** Diseño de la arquitectura de alta disponibilidad en AWS S3, gobierno IAM con LabRole, configuración y ejecución del Glue Crawler, redacción del informe técnico.
* **Derek Pagels:** Limpieza y estructuración del dataset en PySpark, particionamiento en formato Parquet, consultas analíticas en Athena y pipeline de Machine Learning (`VectorAssembler` + `RandomForestRegressor`).
