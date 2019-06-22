from flask_cors import CORS
from flask import Flask

from flask_restful import Api
from flask_compress import Compress
from src.database import DBHandler

from src.controllers.routes.purchases import purchases
from src.controllers.routes.insert import insert


def create_routes(app):
    api = Api()
    purchases(api)
    insert(api)
    api.init_app(app)


def create_app() -> Flask:
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    create_routes(app)

    db = DBHandler(app)
    db.init_db()

    CORS(app, automatic_options=True)
    Compress(app)

    return app
