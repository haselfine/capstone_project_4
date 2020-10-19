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
    # get_game_info(990)
    
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
        logging.error(f'No response recieved ' + e)

    return url_list
    
def get_game_info(game_id):

    client_id = os.environ.get('CLIENT_ID')
    auth = os.environ.get('AUTHORIZATION')

    url = 'https://api.igdb.com/v4/games'
    header_data = {'Client-ID': client_id, 'Authorization': auth}
    body_data = f'fields name, rating, summary, platforms, first_release_date, cover; where id = {game_id};'
    
    try:

        res = requests.post(url, data=body_data, headers = header_data)
        game_info = res.json()
    except Exception as e:
        return None
        logging.error(f'No response recieved ' + e)

    return game_info


    def get_platforms(platforms_list):

    client_id = os.environ.get('CLIENT_ID')
    auth = os.environ.get('AUTHORIZATION')

    platforms_string = ''

    for platform in platfroms_list:

        if i != len(platforms_list)-1:

            platforms_string = platforms_string + platform + ' |'

        else:

            platforms_string = platforms_string + platform + ';'


    url = 'https://api.igdb.com/v4/platforms'
    header_data = {'Client-ID': client_id, 'Authorization': auth}
    body_data = f'fields name,platform_logo; where id = {platforms_string}'
    
    res = requests.post(url, data = body_data, headers = header_data)
    platform_data = res.json()

    pprint(platform_data)


if __name__ == '__main__':
    main()
