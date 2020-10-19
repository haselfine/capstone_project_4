# from project_4.viewmodel import *
import logging
import os
from pprint import pprint
import requests


logging.basicConfig(filename='debug.log', level=logging.DEBUG, format=f'%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def main():
    #TODO connect to APIs
    #TODO search games in Steam, Twitch.tv
    #TODO store game info
    # get_game_urls(990)
    get_game_info(990)
    pass


#takes the game name input and returns a list of games with that name, and their id's.
#If there was an error encouterd it will return None instead, if no games were found it will return an empty list
def search_game_request(game_name):


    client_id = os.environ.get('CLIENT_ID')
    auth = os.environ.get('AUTHORIZATION')
    
    url = 'https://api.igdb.com/v4/search'
    header_data = {'Client-ID': client_id, 'Authorization': auth}
    body_data = f'search "{game_name}"; fields name;'

    try:
        res = requests.post(url, data = body_data, headers = header_data)
        game_list = res.json()

    except Exception as e:
        return None
        logging.error(f'No response recieved '+ e)

    return game_list

    
# funtion that takes the game id, and returns a list containing one dictionary that includes
# all the data 
def get_game_info(game_id):

    client_id = os.environ.get('CLIENT_ID')
    auth = os.environ.get('AUTHORIZATION')

    url = 'https://api.igdb.com/v4/games'
    header_data = {'Client-ID': client_id, 'Authorization': auth}
    body_data = f'fields name, rating, platforms.name, summary, first_release_date, cover.url, websites.url; where id = {game_id};'
    
    try:

        res = requests.post(url, data=body_data, headers = header_data)
        game_info = res.json()
    except Exception as e:
        return None
        logging.error(f'No response recieved ' + e)
    
    return game_info








if __name__ == '__main__':
    main()
