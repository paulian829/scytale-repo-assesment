Create a Volume
First, you need to create a Docker volume. This volume will be mounted into both containers, enabling them to share data. You can create a volume using the Docker CLI:

`docker volume create shared_volume`