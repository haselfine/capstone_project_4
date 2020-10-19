from project_4.viewmodel import *
import logging
import os
from pprint import pprint
import requests


logging.basicConfig(filename='debug.log', level=logging.DEBUG, format=f'%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def main():
    #TODO connect to APIs
    #TODO search games in Steam, Twitch.tv
    #TODO store game info
    pass


#takes the game name input and returns a list of games with that name, and their id's.
#If there was an error encouterd it will return "Failed" instead, if no games were found it will return an empty list
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


def get_current_streamer_from_twitch(user_id):

    url = 'https://api.twitch.tv/helix/streams'
    clientid = os.environ.get('Client_id')
    auth_key = os.environ.get('authorization')
    
    Api_headers = {'Client_id': clientid, 'authorization': auth_key}
    streamer_search = f'fields id; where user = {user_id};'
    try:
        response = requests.post(url, data = streamer_search, headers = Api_headers)
        jsondata = response.json()
        if 'stream' in jsondata:
            if jsondata['stream'] is not None: #stream is online
                return True
            else:
                return False
    except Exception as e:
        logging.error(f'Error checking user: ', e)
        return False
        

       





    

if __name__ == '__main__':
    main()
