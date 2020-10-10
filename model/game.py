from peewee import *
from project_4.model.basemodel import BaseModel, db

class Game(BaseModel):
    game_id = AutoField(primary_key=True)
    title = CharField(unique=True, constraints=[Check('length(name) >= 1'), Check('title is not null')])
    image_url = CharField(unique=True)

    def __str__(self):
        return f'Game title is {self.title}. Image is {self.image_url}'

db.connect()
db.create_tables(Game)