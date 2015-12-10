FROM ubuntu:14.04

MAINTAINER Jeremiah H. Savage <jeremiahsavage@gmail.com>

USER root

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
    && apt-get dist-upgrade -y --force-yes

RUN apt-get update && apt-get install -y --force-yes \
    gfortran \
    git \
    python-pip \
    python-virtualenv \
    python3-dev \
    software-properties-common \
    time \
    zlib1g-dev

RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN adduser --disabled-password --gecos '' ubuntu && adduser ubuntu sudo && echo "ubuntu	ALL=(ALL)	NOPASSWD:ALL" >> /etc/sudoers.d/ubuntu

USER ubuntu

ENV HOME /home/ubuntu

WORKDIR ${HOME}

RUN pip install --user virtualenvwrapper \
    && /bin/bash -c "source ${HOME}/.local/bin/virtualenvwrapper.sh \
    && mkvirtualenv --python=/usr/bin/python3 p3 \
    && pip install ipython pandas pysam sqlalchemy \
    && echo source ${HOME}/.local/bin/virtualenvwrapper.sh >> ${HOME}/.bashrc \
    && echo source ${HOME}/.virtualenvs/p3/bin/activate >> ${HOME}/.bashrc"

ENV merge_sqlite 0.007

RUN git clone https://github.com/jeremiahsavage/merge_sqlite.git
