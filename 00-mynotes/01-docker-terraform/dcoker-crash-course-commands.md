# :movie_camera: Docker Crash Course for Absolute Beginners [NEW] By TechWorld with Nana

# Commands

Check list of docker images available

```
docker images
```
Check list of running containers
```
docker ps
```
To get docker image from docker registry
```
docker pull nginx
```
To run docker image on container
```
docker run nginx:latest
```
To run container in background
```
docker run -d nginx:latest
```
To get container log which running in background
```
docker logs <containerid/containername>
```
To Stop running container
```
docker stop <containerid/containername>
```
To start preivous container
```
docker start <containerid/containername>
```
To port bind running container
```
docker run -d -p 9000:80 nginx:latest
```
To list all of container which are running and stop
```
docker ps -a
```
To give container custom name
```
docker run --name web-app -d nginx:latest
```






