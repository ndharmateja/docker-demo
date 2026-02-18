# Pull base image
FROM python:3.11

# Set working directory
WORKDIR /app

# Copy files required
COPY hello.py .
COPY test.txt .

# Set command to run
CMD ["python", "hello.py"]