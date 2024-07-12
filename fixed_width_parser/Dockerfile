FROM python:3.9-slim

# Setting the working directory in the container
WORKDIR /app

# Copying the current directory contents into the container at /app location
COPY . /app


# Run fixed_width_parser.py when the container launches
CMD ["python", "fixed_width_parser.py"]


Build the Docker image using the below commands:


docker build -t fixed-width-parser .


Run the Docker container:


docker run -v $(pwd):/app fixed-width-parser


