from peewee import *
from model.basemodel import db, BaseModel
from dataclasses import dataclass
from datetime import datetime
import ast

class Game(BaseModel):
    
    game_id = AutoField(primary_key=True)
    title = CharField(unique=True, constraints=[Check('length(title) >= 1'), Check('title is not null')]) #title must be at least one character long and cannot be null
    summary = CharField(null=True)  # allow null values
    date_released = DateField(null=True)
    date_released_timestamp = TimestampField(null=True)
    rating = IntegerField(null=True)
    image_url = CharField(unique=True) #can only have one image_url
    platforms = TextField()
    website_urls = TextField()
    igdb_id = IntegerField()
    twitch_id = IntegerField(null=True) 

    def __str__(self):
        return f'{self.game_id}, {self.title}, {self.summary}, {self.date_released}, {self.date_released_timestamp}, {self.rating}, {self.image_url}, {self.platforms}, {self.website_urls}, {self.igdb_id}, {self.twitch_id}'
    
    def get_platforms(self):
        return ast.literal_eval(self.platforms)
    
    def get_websites(self):
        return ast.literal_eval(self.website_urls)
    

@dataclass
class TempGame(): # game object that's not automatically saved
    
    title: str
    summary: str
    date_released: datetime
    date_released_timestamp: int
    rating: int
    image_url: str
    platforms: list
    website_urls: list
    igdb_id: int
    twitch_id: int
    
    def __str__(self):
        return self.title 
    
    def save(self): # save to db
        game_obj = Game.create(title=self.title,
                               summary=self.summary,
                               date_released=self.date_released,
                               date_released_timestamp=self.date_released_timestamp,
                               rating=self.rating,
                               image_url=self.image_url,
                               platforms=self.platforms,
                               website_urls=self.website_urls,
                               igdb_id=self.igdb_id,
                               twitch_id=self.twitch_id)
        game_obj.save()
        
    def get_platforms(self):
        return self.platforms
    
    def get_websites(self):
        return self.website_urls
        

db.connect()
db.create_tables([Game])
