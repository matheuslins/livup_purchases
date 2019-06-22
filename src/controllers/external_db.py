from pymongo import MongoClient

from src.settings import EXTERNAL_DB


class ExternalDBController:

    def __init__(self):
        self.client = MongoClient(EXTERNAL_DB['DB_HOST'])

    def read_external_data_base(self):
        db = self.client.get_database('livup_sales')
        collection = db['sales']
        return collection.find({})
