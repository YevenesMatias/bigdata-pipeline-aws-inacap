-- Consultas de Análisis Exploratorio Distribuido (EDA) en Amazon Athena
-- Base de datos: db_bigdata_nyc | Tabla: silver

-- 1. Vista previa de datos catalogados
SELECT * 
FROM "db_bigdata_nyc"."silver" 
LIMIT 10;

-- 2. Agregación distribuida por cantidad de pasajeros
SELECT 
    passenger_count,
    COUNT(*) AS total_viajes,
    ROUND(AVG(trip_distance), 2) AS distancia_promedio_millas,
    ROUND(AVG(total_amount), 2) AS tarifa_promedio_usd
FROM "db_bigdata_nyc"."silver"
GROUP BY passenger_count
ORDER BY total_viajes DESC;
