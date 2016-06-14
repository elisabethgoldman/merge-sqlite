FROM quay.io/jeremiahsavage/cdis_base

ENV merge_sqlite 0.14

USER root

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --force-yes \
    sqlite3

RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN /bin/bash -c "source ${HOME}/.virtualenvs/p3/bin/activate \
    && pip install merge_sqlite"
