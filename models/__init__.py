from peewee import *

db = SqliteDatabase('mood.db', threadlocals=True)

class BaseModel(Model):
    class Meta:
        database = db
