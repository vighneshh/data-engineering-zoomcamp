# :movie_camera: DE Zoomcamp 1.2.1 - Introduction to Docker

## What is a Docker
Docker is an open platform for developing, shipping, and running applications. Docker enables you to separate your applications from your infrastructure so you can deliver software quickly.

## What is a data pipeline?
A data pipeline is a method in which raw data is ingested from various data sources and then ported to data store, like a data lake or data warehouse, for analysis.

A Docker image is a snapshot of a container that we can define to run our software, or in this case our data pipelines.
By exporting our Docker images to Cloud providers such as Amazon Web Services or Google Cloud Platform we can run our containers there.

## Installing Docker on Windows
follow steps from here: https://docs.docker.com/desktop/install/windows-install/

##  Error and Debugging
## 1. Docker cannot start on Windows
On windows Docker Desktop application must be running to work on docker
https://stackoverflow.com/questions/40459280/docker-cannot-start-on-windows

## 2. Gave Wintpy error on this command
'''$ docker run -it ubuntu bash'''
the input device is not a TTY.  If you are using mintty, try prefixing the command with 'winpty'
'''$ wintpy docker run -it ubuntu bash'''

