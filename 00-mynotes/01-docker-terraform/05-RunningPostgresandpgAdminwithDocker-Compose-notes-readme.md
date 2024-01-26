# :movie_camera: DE Zoomcamp 1.2.5 - Running Postgres and pgAdmin with Docker-Compose

# Commands

Windows

## Run command to see, docker compose is installed

```
docker compose
```

## write below code in docker-compose.yaml file to get create both containers from preivous video.

```
services:
  pgdatabase:
    image: postgres:13
    environment:
      - POSTGRES_USER=root
      - POSTGRES_PASSWORD=root
      - POSTGRES_DB=ny_taxi
    volumes:
      - "/c/dataengcourse/ingestingdatapostgres:/var/lib/postgresql/data:rw"
    ports:
      - "5432:5432"
  pgadmin1:
    image: dpage/pgadmin4
    environment:
      - PGADMIN_DEFAULT_EMAIL=user@domain.com
      - PGADMIN_DEFAULT_PASSWORD=SuperSecret
    ports:
      - "8088:80"
```


## Run below command in same folder to for docker-compose to run

```
docker-compose up
```

## Run below command to stop docker-compose

```
docker-compose down
```

## Need to find way to connect to previous images using docker-compose
