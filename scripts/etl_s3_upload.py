"""
Script de Ingesta, Filtrado y Particionado a Amazon S3
Autores: Matías Yévenes & Derek Pagels
INACAP Big Data 2026
"""

import os
import boto3
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, year, month

def run_pipeline():
    # 1. Iniciar PySpark
    spark = SparkSession.builder \
        .appName("NYC_Taxi_Pipeline_Inacap") \
        .master("local[*]") \
        .getOrCreate()

    # 2. Cargar datos crudos en Parquet
    df_raw = spark.read.parquet("tripdata_2024.parquet")
    print(f"Total registros ingestados: {df_raw.count():,}")

    # 3. Limpieza y generación de particiones
    df_clean = df_raw.filter(
        (col("trip_distance") > 0.1) & (col("trip_distance") < 70.0) &
        (col("total_amount") >= 2.5) & (col("total_amount") <= 250.0) &
        (col("passenger_count").isNotNull())
    ).withColumn("year", year(col("tpep_pickup_datetime"))) \
     .withColumn("month", month(col("tpep_pickup_datetime")))

    df_sample = df_clean.limit(100000)

    # 4. Escritura local particionada
    output_dir = "./silver_local"
    df_sample.write.mode("overwrite").partitionBy("year", "month").parquet(output_dir)

    # 5. Carga a S3 con Boto3
    s3 = boto3.client('s3')
    bucket_name = "bigdata-ev2-myevenes-dpagels"
    
    for root, _, files in os.walk(output_dir):
        for file in files:
            if file.endswith(".parquet"):
                local_file = os.path.join(root, file)
                rel_path = os.path.relpath(local_file, output_dir)
                s3.upload_file(local_file, bucket_name, f"silver/{rel_path}")

    print("Pipeline ETL completado exitosamente.")

if __name__ == "__main__":
    run_pipeline()
