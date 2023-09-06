FROM python:3 as builder

COPY ./ /opt

WORKDIR /opt

RUN apt-get update \
    && apt-get install -y \
       sqlite3 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip install tox && tox -p

FROM python:3

COPY --from=builder /opt/dist/*.tar.gz /opt
COPY requirements.txt /opt

WORKDIR /opt

RUN pip install -r requirements.txt \
	&& pip install *.tar.gz \
	&& rm -f *.tar.gz requirements.txt

ENTRYPOINT ["merge_sqlite"]

CMD ["--help"]
