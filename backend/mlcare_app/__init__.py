from datetime import date, datetime

from bson import ObjectId
from flask import Flask
from flask.json import JSONEncoder, JSONDecoder
from flask_cors import CORS


class MongoJSONEncoder(JSONEncoder):
    def default(self, o):
        # uses ISO format: YYYY-MM-DD, e. g. "2002-12-04"
        if isinstance(o, date):
            return str(date)

        # uses modified ISO format: YYYY-MM-DD HH-MM-SS
        # e. g. "2002-12-04 12:00:01"
        if isinstance(o, datetime):
            return o.strftime("%Y-%m-%d %H-%M-%S")

        if isinstance(o, ObjectId):
            return str(o)
        else:
            return super().default(o)


class MongoJSONDecoder(JSONDecoder):
    # uses the same formats as encoder
    def default(self, o):
        pass


app = Flask(__name__)
CORS(app)
app.json_encoder = MongoJSONEncoder


# Blueprints import
from .handlers.patient_handler import patient_bp

# Blueprints registration
app.register_blueprint(patient_bp)