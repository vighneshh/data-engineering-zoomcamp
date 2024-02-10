-- Query public available table
SELECT station_id, name FROM
    bigquery-public-data.new_york_citibike.citibike_stations
LIMIT 100;

-- Check yello trip data
SELECT * FROM `dataengzoomcamp-413305.ny_taxi.yellowtaxibq` LIMIT 1000;

-- Create a non partitioned table from external table
CREATE OR REPLACE TABLE dataengzoomcamp-413305.ny_taxi.yellow_non_partitoned AS
SELECT * FROM `dataengzoomcamp-413305.ny_taxi.yellowtaxibq`;


-- Create a partitioned table from non partitoned table
CREATE OR REPLACE TABLE dataengzoomcamp-413305.ny_taxi.yellow_partitoned
PARTITION BY
  DATE(tpep_pickup_datetime) AS
SELECT * FROM dataengzoomcamp-413305.ny_taxi.yellow_non_partitoned;



-- Impact of partition
-- Scanning 1.6GB of data
SELECT DISTINCT(VendorID)
FROM dataengzoomcamp-413305.ny_taxi.yellow_partitoned
WHERE DATE(tpep_pickup_datetime) BETWEEN '2019-06-01' AND '2019-06-30';


-- Scanning ~106 MB of DATA
SELECT DISTINCT(VendorID)
FROM dataengzoomcamp-413305.ny_taxi.yellow_non_partitoned;


-- Let's look into the partitons
SELECT table_name, partition_id, total_rows
FROM `ny_taxi.INFORMATION_SCHEMA.PARTITIONS`
WHERE table_name = 'yellow_partitoned'
ORDER BY total_rows DESC;

-- Creating a partition and cluster table
CREATE OR REPLACE TABLE dataengzoomcamp-413305.ny_taxi.yellow_partitoned_clustered
PARTITION BY DATE(tpep_pickup_datetime)
CLUSTER BY VendorID AS
SELECT * FROM dataengzoomcamp-413305.ny_taxi.yellowtaxibq;


-- Query scans 1.1 GB
SELECT count(*) as trips
FROM dataengzoomcamp-413305.ny_taxi.yellow_partitoned_clustered
WHERE DATE(tpep_pickup_datetime) BETWEEN '2019-06-01' AND '2020-12-31'
  AND VendorID=1;

-- Query scans 864.5 MB
SELECT count(*) as trips
FROM dataengzoomcamp-413305.ny_taxi.yellow_partitoned
WHERE DATE(tpep_pickup_datetime) BETWEEN '2019-06-01' AND '2020-12-31'
  AND VendorID=1;
