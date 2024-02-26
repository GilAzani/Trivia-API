import pymongo
from dotenv import load_dotenv
import os
from mongoengine import connect

load_dotenv()


class question_DB_connection:
    def __init__(self):

        self.DB_url = os.getenv("ATLAS_URI")
        self.database = os.getenv("DB_NAME")

        connect(db=self.database, host=self.DB_url)

        self._client = pymongo.MongoClient(self.DB_url)
        self._db = self._client[self.database]
        self._collection = self._db.question
