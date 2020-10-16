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
    get_game_urls(990)
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
        #todo add logging for the error 

    return game_list


# take the game id input and returns a list of urls associated with it
#If there was an error encouterd it will return None instead, if no games were found it will return an empty list
def get_game_urls(game_id):


    client_id = os.environ.get('CLIENT_ID')
    auth = os.environ.get('AUTHORIZATION')
    
    url = 'https://api.igdb.com/v4/websites'
    header_data = {'Client-ID': client_id, 'Authorization': auth}
    body_data = f'fields url; where game = {game_id};'

    try:
        res = requests.post(url, data = body_data, headers = header_data)
        url_list = res.json()

    except Exception as e:
        return None
        logging.error(f'No response recieved '+ e)
        #todo add logging for the error 

    return url_list
    

if __name__ == '__main__':
    main()
