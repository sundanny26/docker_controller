# docker_controller
It resets barong_email containers every 20 minutes so the service keeps up and fresh

## Build Image
	docker build -t email_c_image .

## Run Container
	docker run -d --name email_controller -v /var/run/docker.sock:/var/run/docker.sock --rm email_c_image

