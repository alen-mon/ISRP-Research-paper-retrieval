FROM tiangolo/uvicorn-gunicorn-fastapi

# Copy requirements.txt to container
COPY ./requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copy your source code into the container
COPY ./src /app/src

# Set the working directory
WORKDIR /app/src/server

# Command to run the FastAPI application (replace "app.py" with your actual file name)
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
