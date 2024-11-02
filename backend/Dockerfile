# Use an official Python image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Upgrade pip
# Copy the requirements and install dependencies
COPY requirements.txt .
RUN python -m pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
# Copy the current directory contents into the container
COPY . .

# Install dependencies with a timeout and retry mechanism
RUN pip install --default-timeout=100 -i https://mirrors.aliyun.com/pypi/simple/ -r requirements.txt || \
    (sleep 5 && pip install --default-timeout=100 -i https://mirrors.aliyun.com/pypi/simple/ -r requirements.txt)

# Expose the backend port
EXPOSE 8000

# Run the backend
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
