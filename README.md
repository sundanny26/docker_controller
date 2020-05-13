# docker_controller
It resets barong_email containers every 20 minutes so the service keeps up and fresh

## Build Image
	docker build -t email_c_image .

## Run Container
	docker run -d --name email_controller -v /var/run/docker.sock:/var/run/docker.sock --rm email_c_image

### documentation of module
https://docker-py.readthedocs.io/en/stable/client.html
https://pypi.org/project/docker/
https://docs.docker.com/engine/api/sdk/#install-the-sdks

