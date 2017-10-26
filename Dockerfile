FROM ubuntu:artful-20171019

MAINTAINER Jeremiah H. Savage <jeremiahsavage@gmail.com>

ENV VERSION 0.36

RUN apt-get update \
    && apt-get install -y \
       python3-pip \
       sqlite3 \
    && apt-get clean \
    && pip3 install merge_sqlite \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*