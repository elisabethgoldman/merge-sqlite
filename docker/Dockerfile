FROM ubuntu:xenial-20161010

MAINTAINER Jeremiah H. Savage <jeremiahsavage@gmail.com>

RUN echo 'Acquire::http::Proxy "http://cloud-proxy:3128";' >> /etc/apt/apt.conf.d/01proxy \
    && echo 'Acquire::https::Proxy "http://cloud-proxy:3128";' >> /etc/apt/apt.conf.d/01proxy \
    && apt-get update \
    && apt-get install -y \
       python3-pip \
       sqlite3 \
    && apt-get clean \
    && pip3 install merge_sqlite \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && rm -f /etc/apt/apt.conf.d/01proxy