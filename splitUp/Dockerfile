# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# set work directory
WORKDIR /code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
