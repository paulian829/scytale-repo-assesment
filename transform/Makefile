build:
	docker build -t pyspark-app .

run: build
	# docker run --rm -it pyspark-app
	
	sudo mkdir -p $$(pwd)/../files && sudo docker run -v $$(pwd)/../files:/usr/src/app/files pyspark-app