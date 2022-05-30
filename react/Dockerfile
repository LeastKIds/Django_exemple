FROM node:fermium-alpine3.15

MAINTAINER "leastkids@gmail.com"

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN cd /app

RUN npx create-react-app blogapi .
RUN cd ./blogapi


