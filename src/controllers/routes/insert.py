from flask_restful import Resource

from src.database import async_session
from src.models.purchases import Purchase
from src.controllers.external_db import ExternalDBController
from src.controllers import prepare_item


class InsertResource(Resource):
    def post(self):
        external_db = ExternalDBController()
        items = external_db.read_external_data_base()
        with async_session() as session:
            [Purchase().save(prepare_item(item), session) for item in items]
        return "ok", 200


def insert(api):
    root = '/insert/{}'
    api.add_resource(InsertResource, root.format('/'))
