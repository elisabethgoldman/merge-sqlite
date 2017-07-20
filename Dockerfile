FROM ubuntu:xenial-20161010

MAINTAINER Jeremiah H. Savage <jeremiahsavage@gmail.com>

ENV VERSION 0.33

RUN apt-get update \
    && apt-get install -y \
       python3-pip \
       sqlite3 \
    && apt-get clean \
    && pip3 install merge_sqlite \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*