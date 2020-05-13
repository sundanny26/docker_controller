# docker_controller

## Build Image
	docker build -t email_c_image .

## Run Container
	docker run --name email_controller -v /var/run/docker.sock:/var/run/docker.sock --rm email_c_image

