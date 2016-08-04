FROM ubuntu:xenial-20160713

MAINTAINER Jeremiah H. Savage <jeremiahsavage@gmail.com>

ENV merge_sqlite 0.23

USER root

RUN apt-get update && apt-get install -y \
    python3-pip \
    sqlite3

RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip install merge_sqlite
