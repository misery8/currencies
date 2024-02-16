FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /currencies

COPY requirements.txt ./

COPY docker-entrypoint.sh ./

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

RUN mkdir -p /currencies/static

ENTRYPOINT ["sh", "./docker-entrypoint.sh"]