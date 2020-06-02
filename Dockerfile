FROM python:3.7-alpine
MAINTAINER PuneetRohtela

ENV PYTHONUNBUFFERED 1
COPY ./requirments.txt /requirments.txt
RUN pip install -r /requirments.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D puneet
USER puneet