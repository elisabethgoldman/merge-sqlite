FROM ubuntu:xenial-20160809

MAINTAINER Jeremiah H. Savage <jeremiahsavage@gmail.com>

USER root

RUN apt-get update \
    && apt-get install -y \
       python3-pip \
       sqlite3 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    &&  pip3 install merge_sqlite
