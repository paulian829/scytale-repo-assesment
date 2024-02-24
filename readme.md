Create a Volume
First, you need to create a Docker volume. This volume will be mounted into both containers, enabling them to share data. You can create a volume using the Docker CLI:

`docker volume create shared_volume`



# Scytale Home Assignment
This project consists of two main components designed to work with Docker containers: a PySpark application and a GitHub data fetching tool. Each component resides in its own folder (transform and extract respectively) and includes a Makefile for automating build and run processes.

## Prerequisites
Before you begin, ensure you have Docker installed and running on your machine. Knowledge of Docker, PySpark, and GitHub APIs will be beneficial.

## Transform
- `/transform` - Contains the PySpark application designed to perform data transformations.
- `/extract` - Contains the tool for fetching data from GitHub.

# Getting Started

## Extract Component
The `extract` folder contains a Dockerfile for the GitHub data fetching tool. To build and run this component, execute:

```
cd extract
make build
make run
```

This builds the Docker image `github-fetch` and runs it, similarly mounting a volume from `../files` to `/usr/src/app/files` in the container.

## Transform Component
The `transform` folder contains a Dockerfile to containerize the PySpark application. Use the following commands to build and run the application:

```
cd transform
make build
make run
```
This will build the Docker image named `pyspark-app` and run it, mounting a volume from `../files` to` /usr/src/app/files` in the container for data persistence.
