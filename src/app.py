import logging

from flask import Flask
from waitress import serve

logger = logging.getLogger("waitressi logging")
logger.setLevel(logging.INFO)

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    logger.info("/ invoked")
    return "Hi, Hello world Writen With Python Using Flask and Waitress - version 0.1.2"


if __name__ == "__main__":
    port = 8080
    serve(app, host="0.0.0.0", port=port)
