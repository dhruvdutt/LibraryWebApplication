from pymongo import MongoClient
class Database(object):
    def __init__(self):
        client = MongoClient('mongodb://localhost/')
        db = client['calibrary']