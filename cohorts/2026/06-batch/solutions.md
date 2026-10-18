# Module 6 Homework Solutions

Dataset: [Yellow Taxi Trip Data - November 2025](https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2025-11.parquet)


## Question 1: Install Spark and PySpark

```python
import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local[*]") \
    .appName('homework') \
    .getOrCreate()

spark.version
```

**Answer: `4.1.1`**

(The answer depends on the installed version)


## Question 2: Yellow November 2025

```python
df = spark.read.parquet("yellow_tripdata_2025-11.parquet")
df = df.repartition(4)
df.write.parquet("yellow_tripdata_2025-11_partitioned")
```

Then check the file sizes:

```python
import os, glob

parquet_files = glob.glob("yellow_tripdata_2025-11_partitioned/*.parquet")
for f in parquet_files:
    size_mb = os.path.getsize(f) / (1024 * 1024)
    print(f"{os.path.basename(f)}: {size_mb:.1f} MB")
```

Each file is approximately 24.4 MB.

**Answer: 25MB**


## Question 3: Count records

```python
from pyspark.sql import functions as F

count_15 = df.filter(
    F.to_date(F.col("tpep_pickup_datetime")) == "2025-11-15"
).count()

print(count_15)
# 162604
```

**Answer: 162,604**


## Question 4: Longest trip

```python
df_with_duration = df.withColumn(
    "duration_hours",
    (F.unix_timestamp(F.col("tpep_dropoff_datetime")) - F.unix_timestamp(F.col("tpep_pickup_datetime"))) / 3600
)

longest = df_with_duration.agg(F.max("duration_hours")).collect()[0][0]
print(f"{longest:.1f}")
# 90.6
```

**Answer: 90.6**


## Question 5: User Interface

Spark's User Interface runs on port 4040 by default.

**Answer: 4040**


## Question 6: Least frequent pickup location zone

```python
zones = spark.read.option("header", "true").csv("taxi_zone_lookup.csv")
zones.createOrReplaceTempView("zones")
df.createOrReplaceTempView("trips")

spark.sql("""
    SELECT z.Zone, COUNT(*) as cnt
    FROM trips t
    JOIN zones z ON t.PULocationID = z.LocationID
    GROUP BY z.Zone
    ORDER BY cnt ASC
    LIMIT 5
""").show(truncate=False)
```

```
+---------------------------------------------+---+
|Zone                                         |cnt|
+---------------------------------------------+---+
|Governor's Island/Ellis Island/Liberty Island|1  |
|Eltingville/Annadale/Prince's Bay            |1  |
|Arden Heights                                |1  |
|Port Richmond                                |3  |
|Rikers Island                                |4  |
+---------------------------------------------+---+
```

Three zones are tied with count=1. Among the answer options, Governor's Island/Ellis Island/Liberty Island is the least frequent.

**Answer: Governor's Island/Ellis Island/Liberty Island**
