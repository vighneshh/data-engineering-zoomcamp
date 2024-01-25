# :movie_camera: DE Zoomcamp 1.2.3 - Connecting pgAdmin and Postgres

# Error and Debugging



# Commands

Windows

## Create network in docker

```
winpty docker network create pg-network
```


## Running Postgres on Windows on above created network (note the full path)

```
winpty docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v /c/dataengcourse/ingestingdatapostgres:/var/lib/postgresql/data \
  -p 5432:5432 \
  --network pg-network \
  --name pgdatabase \
  postgres:13
```

--name is important so you can get previous same postgres database

## PgAdmin container deployment in docker

```
winpty docker run -p 8088:80 \
    -e 'PGADMIN_DEFAULT_EMAIL=user@domain.com' \
    -e 'PGADMIN_DEFAULT_PASSWORD=SuperSecret' \
    --network pg-network \
    --name pgadmin2 \
    -d dpage/pgadmin4
```


## Remove Docker Container
```
docker rm pgadmin1
```

