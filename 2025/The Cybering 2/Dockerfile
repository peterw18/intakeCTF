# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's code into the container at /app
COPY ./ /app/

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variables for the database connection
ENV MYSQL_HOST=db
ENV MYSQL_USER=admin
ENV MYSQL_PASSWORD=password
ENV MYSQL_DB=db

# Run main.py when the container launches
CMD ["python", "main.py"]