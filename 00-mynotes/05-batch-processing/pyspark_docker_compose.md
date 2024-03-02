## Using Apache Spark and Jupiter Notebook in Docker Compose

These steps are taken from this medium aricle.
[Run PySpark and Jupyter Notebook using Docker](https://medium.com/analytics-vidhya/run-pyspark-and-jupyter-notebook-using-docker-bed12ecb755a)


## Create docker-compose.yaml file and paste below code.
```
version: "3"
services:
  pyspark:
    image: "jupyter/all-spark-notebook"
    volumes:
      - c:/code/pyspark-data:/home/jovyan
    ports:
      - 8888:8888

```
## Start Docker container
```
docker-compose up
```

## Open Jupiter notebook in broweser using this url.
```
http://127.0.0.1:8888/?token=YOUR_TOKEN
```

## Run this code from jupiter lab to see if pyspark is working
```
# Import the necessary modules
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Create a SparkSession
spark = SparkSession.builder \
   .appName("My App") \
   .getOrCreate()

rdd = spark.sparkContext.parallelize(range(1, 100))

print("THE SUM IS HERE: ", rdd.sum())
# Stop the SparkSession
spark.stop()
```
 
