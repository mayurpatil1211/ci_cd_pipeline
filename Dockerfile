FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ app/

ENV APP_VERSION=v1
ENV FLASK_ENV=production

EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "2", "app:create_app()"]

# # Use official Python slim image
# FROM python:3.12-slim
 
# # Set working directory inside container
# WORKDIR /app
 
# # Create non-root user
# RUN useradd -m appuser

# # Copy requirements first (layer caching — only reinstalls if requirements change)
# COPY requirements.txt .
 
# # Install dependencies
# RUN pip install --no-cache-dir -r requirements.txt
 
# # Copy app code
# COPY app.py .
 
# # Expose port
# EXPOSE 5000


# USER appuser
 
# # Run the app
# CMD ["python", "app.py"]
 