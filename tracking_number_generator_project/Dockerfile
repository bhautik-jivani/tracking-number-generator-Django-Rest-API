FROM python:latest

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /tracking_number_generator_project/tracking_number_generator_project

COPY requirements.txt .

RUN python -m pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /var/log/gunicorn
RUN chown -R 777 /var/log/gunicorn

RUN mkdir -p /var/log/nginx
RUN chown -R 777 /var/log/nginx