# import pymongo
from dotenv import load_dotenv
import os
from mongoengine import connect, disconnect, DEFAULT_CONNECTION_NAME

load_dotenv()


class QuestionDBConnection:
    def __init__(self):

        self.DB_url = os.getenv("ATLAS_URI")
        self.database = os.getenv("DB_NAME")
        self.test_DB_url = os.getenv("TEST_DB_NAME")
        # self._client = pymongo.MongoClient(self.DB_url)
        # self._db = self._client[self.database]
        # self._collection = self._db.question

    def connect_to_db(self):
        connect(db=self.database, host=self.DB_url, alias=DEFAULT_CONNECTION_NAME)

    def disconnect_from_db(self):
        disconnect(alias=DEFAULT_CONNECTION_NAME)

    def connect_to_test_db(self):
        connect(host=self.DB_url, db=self.test_DB_url)
