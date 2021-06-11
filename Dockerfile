FROM python:3

ENV PYTHONONBUFFERED 1
ENV PORT 8080

WORKDIR /app

ADD . /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app
