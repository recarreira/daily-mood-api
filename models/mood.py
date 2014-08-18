from peewee import *
from models import BaseModel

import datetime


class Mood(BaseModel):
    level = CharField()
    created = DateTimeField(default=datetime.datetime.now)
