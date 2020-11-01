import os
import requests
import logging
from pprint import pprint

client_id = os.environ.get('CLIENT_ID')
auth = os.environ.get('AUTHORIZATION')

header_data = {'Client-ID': client_id, 'Authorization': auth}


#takes the game name input and returns a list of games with that name, and their id's.
#If there was an error encouterd it will return "Failed" instead, if no games were found it will return an empty list
def search_game_request(game_name):
    
    url = 'https://api.igdb.com/v4/games'
    body_data = f'search "{game_name}"; fields name;'

    try:
        res = requests.post(url, data = body_data, headers = header_data)
        game_list = res.json()
        
        if game_list[0] != 'message':  # failed searches will contain an error message
            return game_list, None
        else:
            error = 'Search failed: ' + game_list['message']
            logging.error(error)
            return None, error

    except Exception as e:
        logging.error(e)
        return None, e
    
    
# funtion that takes the game id, and returns a list containing one dictionary that includes
# all the data 
def get_game_info(game_id):
    url = 'https://api.igdb.com/v4/games'
    body_data = f'fields name, rating, platforms.name, summary, first_release_date, cover.url, websites.url; where id = {game_id};'
    
    try:
        res = requests.post(url, data=body_data, headers = header_data)
        game_info = res.json()[0]
        
        if res.status_code == 200:
            return game_info, None
        
        else:
            return None, game_info['cause']

    except Exception as e:
        logging.error(e)
        return None, e

