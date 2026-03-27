FROM python:3.10-slim

WORKDIR /app

COPY . .

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r api/requirements.txt

# Set root as PYTHONPATH so 'api' can be imported
ENV PYTHONPATH=/app

EXPOSE 5000

# Run the app
CMD ["python", "api/app.py"]
