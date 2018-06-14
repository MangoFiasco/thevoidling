FROM python:3.6.5-alpine3.7

WORKDIR /thevoid

ADD . /thevoid

RUN  pip install --upgrade pip setuptools && pip install flask requests flask-cors