from flask import jsonify, request
from flask_restful import Resource

from src.database import async_session
from src.database.schemas import PurchaseOutSchema
from src.models.purchases import Purchase
from src.controllers import build_payload


class PurchasesResource(Resource):

    def get(self):
        user_id = None
        args = request.args
        if args:
            user_id = args.get('user_id', None)

        with async_session() as session:
            if user_id:
                data = Purchase().get_all_by_user(session, user_id)
            else:
                data = Purchase().get_all(session)

            if not data:
                return None, 204

            processed_data = build_payload(data)
            serialized_data = PurchaseOutSchema().dump(processed_data, many=True)

            return jsonify(serialized_data)


def purchases(api):
    root = '/purchases/{}'
    api.add_resource(PurchasesResource, root.format('/'))
