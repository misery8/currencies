FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /currencies

COPY requirements.txt ./

RUN pip install --upgrade pip && pip install -r requirements.txt

RUN python manage.py migrate