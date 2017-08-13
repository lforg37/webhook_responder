from python:3-alpine

RUN pip install github-webhook
COPY scripts/ /scripts/
WORKDIR scripts

ENTRYPOINT ["/scripts/app.py"]
