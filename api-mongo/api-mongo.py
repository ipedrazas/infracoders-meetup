"""APi-mongo.

Infracoders meetup example
"""

from flask import Flask, request
from flask.ext.pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
import os


app = Flask(__name__)

# connect to another MongoDB server altogether
app.config['MONGO_HOST'] = os.getenv('MONGO_HOST')
app.config['MONGO_PORT'] = int(os.getenv('MONGO_PORT',))
app.config['MONGO_DBNAME'] = os.getenv('MONGO_DBNAME', 'infratest')


mongo = PyMongo(app, config_prefix='MONGO')


@app.route('/')
def hello_infra():
    """Hello function."""
    return 'Hello Infracoders!'


@app.route('/entries', methods=['POST'])
def save_entry():
    """Save entry."""
    app.logger.debug(request.get_json())
    content = request.get_json()
    new_object = mongo.db.entries.insert(
        {
            'body': content.get('body').encode("utf-8"),
            'title': content.get('title', '').encode("utf-8")
        }
    )
    app.logger.debug(new_object)
    return dumps(new_object)


@app.route('/entries/<entry>')
def get_entry(entry):
    """Get entry."""
    entry = mongo.db.entries.find_one_or_404({'_id': ObjectId(entry)})
    return dumps(entry)


@app.route('/entries', methods=['GET'])
def get_entries():
    """Get entries."""
    entries = mongo.db.entries.find()
    return dumps(entries)


@app.route('/_status/healthz', methods=['GET'])
def get_healthz():
    """Get entries."""
    return "ok"


@app.route('/_status/mongo/healthz', methods=['GET'])
def get_mongo_healthz():
    """Get entries."""
    entries = mongo.db.entries.find()
    app.logger.debug(entries)
    return dumps(entries)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
