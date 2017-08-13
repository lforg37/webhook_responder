#!/bin/python3
from github_webhook import Webhook
from flask import Flask
import sys
import socket

secret = None

if len(sys.argv) > 1:
    secret = sys.argv[1]

app = Flask(__name__)  # Standard Flask app
webhook = Webhook(app, secret=secret) # Defines '/postreceive' endpoint

@webhook.hook()        # Defines a handler for the 'push' event
def on_push(data):
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    try:
        sock.connect("/trigger.so")
        sock.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
