build:
	docker build -t github-fetch .

run: build
	sudo mkdir -p $$(pwd)/../files && sudo docker run -v $$(pwd)/../files:/usr/src/app/files github-fetch

