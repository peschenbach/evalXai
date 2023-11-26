# evalXai
Web app to evaluate explainable ai methods

# Build the Docker image
To create the image run: 
`docker build -t <image-name> <directory with Dockerfile>`

example: 
`docker build -t python-test-app .`

# Run a Docker container from the image
`docker run -it --rm <image-name>`

example:
`docker run -it --rm python-test-app`