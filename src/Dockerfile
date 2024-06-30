# Use the official Python 3.7 image as the base image
FROM python:3.7

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY src .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Specify the command to run the application
CMD [ "python", "helloworld/core.py" ]