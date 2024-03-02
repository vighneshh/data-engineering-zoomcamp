
# Commands
Windows

# Build docker compose file
```
docker compose build
```
# Start the container
```
docker compose up
```
# Start the container and loading part in terminal
```
docker compose up -d
```
# Stop the container
```
docker compose down
```
###  For set up refer this: [Superset with docker](https://medium.com/towards-data-engineering/quick-setup-configure-superset-with-docker-a5cca3992b28)
# Superset url: 
```
http://localhost:8085/
```
# PG Adming can be access here
```
http://localhost:8088
```
### [Run PySpark and Jupyter Notebook using Docker](https://medium.com/analytics-vidhya/run-pyspark-and-jupyter-notebook-using-docker-bed12ecb755a)
# Access Pyspark with jupiter lab 
```
http://127.0.0.1:8888/?token=YOUR_TOKEN
```
### Refer this repo for prefect docker [prefect-docker-compose](https://github.com/rpeden/prefect-docker-compose)

# To run Prefect Server, open a terminal, navigate to the directory where you cloned this repository, and run:
```
docker-compose --profile server up
```
#  navigate to url to see the Prefect UI.
```
http://localhost:4200
```
## Prefect CLI

Next, open another terminal in the same directory and run:

```
docker-compose run cli
```

This runs an interactive Bash session in a container that shares a Docker network with the server you just started. If you run `ls`, you will see that the container shares the `flows` subdirectory of the repository on the host machine:

```
flow.py
root@fb032110b1c1:~/flows#
```

To demonstrate the container is connected to the Prefect Server instance you launched earlier, run:

```
python flow.py
```

navigate to `http://localhost:4200/runs` and you will see the flow you just ran in your CLI container.

If you'd like to use the CLI container to interact with Prefect Cloud instead of a local Prefect Server instance, update `docker-compose.yml` and change the agent service's `PREFECT_API_URL` environment variable to match your Prefect Cloud API URL. Then, uncomment the `PREFECT_API_KEY` environment variable and replace `YOUR_API_KEY` with your own API key. If you'd prefer not to put your API key in a Docker Compose file, you can also store it in an environment variable on your host machine and pass it through to Docker Compose like so:

```
- PREFECT_API_KEY=${PREFECT_API_KEY}
```

## Prefect Agent

You can run a Prefect Agent by updating `docker-compose.yml` and changing `YOUR_WORK_QUEUE_NAME` to match the name of the Prefect work queue you would like to connect to, and then running the following command:

```
docker-compose --profile agent up
```

This will run a Prefect agent and connect to the work queue you provided. 

As with the CLI, you can also use Docker Compose to run an agent that connects to Prefect Cloud by updating the agent's `PREFECT_API_URL` and `PREFECT_API_KEY` settings in `docker-compose.yml`.
