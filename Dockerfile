from python:3-alpine

COPY scripts/ /scripts/

RUN pip install github-webhook

WORKDIR scripts

ENTRYPOINT ["/scripts/app.py"]
