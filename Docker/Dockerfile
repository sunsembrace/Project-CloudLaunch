
# Use official Python image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app 

# copy app files
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app/ .

# Expose port Flask uses
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]


