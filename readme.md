# Scytale Home Assignment
This project consists of two main components designed to work with Docker containers: a PySpark application and a GitHub data fetching tool. Each component resides in its own folder (transform and extract respectively) and includes a Makefile for automating build and run processes.

## Prerequisites
Before you begin, make sure you have the following installed and configured on your system:

- **Docker:** Ensure Docker is installed and running on your machine. Docker is used to containerize and run the applications.
- **Windows Subsystem for Linux (WSL):** This project requires WSL for Windows users. Follow the official Microsoft documentation to install and set up WSL on your Windows system.
- **Make:** The make command is used to automate the building and running of Docker containers through Makefiles. Ensure make is installed on your system. Linux and macOS systems usually have it pre-installed. Windows users can access make through WSL or other Unix-like environments.

## Configuration
### Setting up the `.env` file for Github Data Fetching
For the GitHub data fetching component (extract), you need to set up a .env file to securely store your GitHub access token. This token allows the application to authenticate with GitHub's API and access data.

Link: https://github.com/settings/tokens

.env
```
GITHUB_TOKEN=your_token_here
```

## Structure
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
