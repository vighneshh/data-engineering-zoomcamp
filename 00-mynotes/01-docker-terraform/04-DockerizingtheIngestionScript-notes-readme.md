# :movie_camera: DE Zoomcamp 1.2.4 - Dockerizing the Ingestion Script

# Error and Debugging



# Commands

Windows

## Convert Jupyter notebook to normal python file

```
jupyter nbconvert --to=script connecting-to-postgres-using-sqlalchemy.ipynb
```

## Run current folder as http.server using python

```
python -m http.server
```

## After converting jupiter file to python code, converted code for argparse to load input from command line.
and run file like this.

```
URL="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"

python ingest_data.py \
  --user=root \
  --password=root \
  --host=localhost \
  --port=5432 \
  --db=ny_taxi \
  --table_name=yellow_taxi_trips \
  --url=${URL}
```

## We can dockerize above code and build it docker image (Check docker file)

```
docker build -t taxi_ingest:v001 .
```

run code in docker like this.

```
URL = "http://192.168.0.107:8000/yellow_tripdata_2021-01.csv"

winpty docker run -it \
  --network=pg-network \
  taxi_ingest:v001 \
    --user=root \
    --password=root \
    --host=pgdatabase \
    --port=5432 \
    --db=ny_taxi \
    --table_name=yellow_tripdata_trip \
    --url=${URL}
```

