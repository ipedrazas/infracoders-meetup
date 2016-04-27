"""Simple APi.

Simple API for an Infracoders meetup
"""

from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_bw():
    """Hello function."""
    return 'Hello Infracoders! this is a simple api'


@app.route('/_status/healthz')
def healthz():
    """Hello function."""
    return 'Healthy'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True, threaded=True)
