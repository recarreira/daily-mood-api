from peewee import *

db = SqliteDatabase('mood.db', threadlocals=True)

class BaseModel(Model):
    def __marshallable__(self):
        """Return the marshallable dictionary that will be serialized by
        marshmallow. Peewee models have a dictionary representation where the
        ``_data`` key contains all the field:value pairs for the object.
        """
        return dict(self.__dict__)['_data']

    class Meta:
        database = db
