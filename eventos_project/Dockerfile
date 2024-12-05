# Dockerfile
FROM python:3.10-slim

WORKDIR /eventos_project

COPY requirements.txt requirements.txt
RUN apt-get update && apt-get install -y libpq-dev
RUN pip install --no-cache-dir -r requirements.txt

COPY . /eventos_project/

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "eventos_project.wsgi:application"]
