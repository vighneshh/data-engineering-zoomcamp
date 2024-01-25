# :movie_camera: DE Zoomcamp 1.2.2 - Ingesting NY Taxi Data to Postgres

# Error and Debugging

1. Docker needs commands and filepath in lowercases and no space in between.

2. Docker gave error: docker: Error response from daemon: invalid mode: \Program Files\Git\var\lib\pos
tgresql\data.

then change windows path to c:/ to /c/ and for some reason its creating ;C at end of path


# Commands

Windows
Running Postgres on Windows (note the full path)

```
winpty docker run -it \
  -e POSTGRES_USER="root" \
  -e POSTGRES_PASSWORD="root" \
  -e POSTGRES_DB="ny_taxi" \
  -v /c/dataengcourse/ingestingdatapostgres:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres:13
```


 Install pgcli to connect to database and check database. 
 I think its not needed if I can connect with sqlalchemy and run queries.

 ```
 pip install pgcli
```

For SQLAlchemy code check jupiter notebook

