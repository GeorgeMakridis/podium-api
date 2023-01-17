FROM python:3.8-slim

# Install required libraries
RUN pip install tensorflow flask numpy

# Copy the code to the container
COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

# Run the API
CMD ["python", "api.py"]