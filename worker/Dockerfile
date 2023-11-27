# Use official python image as parent image
FROM python:3.10

# Set the working directory to /app
WORKDIR /app

# Install any needed packages specified in requirements.txt
RUN pip install torch==2.1.1
RUN pip install captum==0.6.0
RUN pip install scikit-learn==1.3.2
RUN pip install pandas==1.5.3
RUN pip install matplotlib==3.4.3
RUN pip install numpy==1.26.0

# Copy the current directory contents in the container at /app
COPY . /app/

# Devine environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "data_exploration.py"]