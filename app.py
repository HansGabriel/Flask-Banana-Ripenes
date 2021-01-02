from flask import Flask
from algorithms.classify import classifyBanana

app = Flask(__name__)


@app.route('/')
def hello():
    # result = classifyBanana('static/images/banaa.png')
    result = classifyBanana('static/images/banaa.png')
    return 'Hello, Hans!'