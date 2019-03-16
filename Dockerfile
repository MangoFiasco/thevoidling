FROM python:3.6.5

WORKDIR /thevoidling

ADD . /thevoidling

RUN  apt-get update && apt-get install mysql-server mysql-client -y 

RUN  pip3 install --upgrade pip setuptools && pip3 install -r requirements.txt