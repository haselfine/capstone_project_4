from peewee import *
from project_4.model.config import db_path

db = SqliteDatabase(db_path, pragmas={'foreign_keys': 1})

class BaseModel(Model):
    class Meta:
        database = db