# Use an official Python runtime as a base image
FROM python:3.9-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Copy the Streamlit app and Flask app into the container at /app
COPY . /app/

# 
COPY ./requirements.txt /app/requirements.txt

# 
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose the ports for Streamlit and Flask apps
EXPOSE 8501 80

# Start Streamlit and Flask

CMD sh -c 'streamlit run quiz.py --server.port 8501 --server.address 0.0.0.0 & python3 health.py'
