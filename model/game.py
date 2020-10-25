from peewee import *
from project_4.model.basemodel import db, BaseModel
import json

class Game(BaseModel):
    game_id = AutoField(primary_key=True)
    title = CharField(unique=True, constraints=[Check('length(title) >= 1'), Check('title is not null')])
    summary = CharField()
    date_released = DateField()
    rating = FloatField()
    image_url = CharField(unique=True)
    platforms = TextField() # store json for these as text in db
    website_urls = TextField()  # store json for these as text in db
    igdb_id = IntegerField()
    twitch_id = IntegerField()

    def __str__(self):
        return f'Game title is {self.title}. Image is {self.image_url}'
    
    # converts the raw text from db to a usable json
    def get_platforms(self):
        return json.loads(self.platforms)
    
    # converts the raw text from db to a usable json
    def get_websites(self):
        return json.loads(self.website_urls)
        

db.connect()
db.create_tables([Game])
