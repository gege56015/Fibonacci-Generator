FROM python:2.7.15-alpine

WORKDIR /app

COPY Pipfile .
COPY Pipfile.lock .
COPY main/ ./main/

RUN apk update && apk upgrade && pip install pipenv && pipenv install --system

WORKDIR /app/main

EXPOSE 8000

CMD [ "gunicorn", "wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3" ]