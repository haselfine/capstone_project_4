from project_4.model.game import Game, TempGame, DatabaseError
from project_4.view.image import *
from project_4.view.twitch import *
import logging
import ast
from datetime import datetime

def add_game(game_data, from_api):
    try:
        temp_game = create_game(game_data, from_api)
        temp_game.save()
        return 'Game saved.', None
    except DatabaseError as e:
        logging.error(e)
        return None, 'There was an error in adding the game.'
    except Exception as e:
        print(e)
        logging.error(e)
        return None, e
    
def create_game(game_data, from_api): # from_api indicates whether there is an image_url field
    if from_api:
        
        # sanitize data
        if 'cover' in game_data: image_url = create_image_link(game_data['cover']['url'])
        else: original_image_url = None
        if 'rating' in game_data: rating = int(game_data['rating'])
        else: rating = 0
        if 'websites' in game_data: website_urls = make_list_from_json(game_data['websites'], 'url')
        else: website_urls = []
        if 'platforms' in game_data: platforms = make_list_from_json(game_data['platforms'], 'name')
        else: platforms = []
        if 'first_release_date' in game_data: timestamp = game_data['first_release_date']
        else: timestamp = 0
        
    else:
        image_url = game_data['image_url']
        website_urls = ast.literal_eval(game_data['websites'].replace('&#39;', '\''))
        platforms = ast.literal_eval(game_data['platforms'].replace('&#39;', '\''))
        rating = game_data['rating']
        timestamp = game_data['first_release_date']
    
    game_obj = TempGame(title=game_data['name'],
                        summary=game_data['summary'].replace('\n', ' '),
                        date_released=datetime.fromtimestamp(int(timestamp)),
                        date_released_timestamp=int(timestamp),
                        rating=rating,
                        image_url=image_url,
                        platforms=platforms,
                        website_urls=website_urls,
                        igdb_id=int(game_data['id']),
                        twitch_id=int(get_twitch_game_id(game_data['name'])[0]))
    return game_obj

def find_game(title_in):
    try:
        searched_game = Game.get_or_none(Game.title == title_in)
        return searched_game, None
    except DatabaseError:
        return None, 'Sorry. There was an error retrieving the game.'

def find_game_by_igdb_id(igdb_id):
    try:
        searched_game = Game.get_or_none(Game.igdb_id == igdb_id)
        return searched_game, None
    except DatabaseError:
        return None, 'Sorry. There was an error retrieving the game.'

def get_all_games():
    try:
        return Game.select(), None
    except DatabaseError:
        return None, 'Sorry. There was an error retrieving the games'

def delete_game(game_id_in):
    try:
        return Game.delete().where(Game.game_id == game_id_in).execute(), None
    except DatabaseError:
        return None, 'Sorry. There was an error deleting the artwork'
    
def make_list_from_json(json, field_name):
    output_list = []
    
    for item in json:
        output_list.append(item[field_name])
    
    return output_list
