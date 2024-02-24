# Start with a base image that includes Java
FROM openjdk:11-jre-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Install Python and procps
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    procps \
 && rm -rf /var/lib/apt/lists/*

# Ensure python and pip commands are available (Python 3)
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1 && \
    update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1

# Install Python dependencies
RUN pip install pyspark

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Define environment variable
ENV PYTHONUNBUFFERED=1

VOLUME /usr/src/app/files

# Run app.py when the container launches
CMD ["python", "./app.py"]
