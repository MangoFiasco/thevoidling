FROM python:3.6.5-alpine3.7

WORKDIR /thevoidling

ADD . /thevoidling

RUN  apk --no-cache add mysql mysql-client

RUN  pip install --upgrade pip setuptools && pip install flask requests flask-cors