# Use official Python slim image
FROM python:3.12-slim
 
# Set working directory inside container
WORKDIR /app
 
# Copy requirements first (layer caching — only reinstalls if requirements change)
COPY requirements.txt .
 
# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
 
# Copy app code
COPY app.py .
 
# Expose port
EXPOSE 5000
 
# Run the app
CMD ["python", "app.py"]
 