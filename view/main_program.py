# from project_4.viewmodel import *
import os
from pprint import pprint
import requests

def main():
    #TODO connect to APIs
    #TODO search games in Steam, Twitch.tv
    #TODO store game info


    game_list = search_game_request(input('Enter game name'))
    pprint(game_list)
    pass


#takes the game name input and returns a list of games with that name, and their id's.
#If there was an error encouterd it will return "Failed" instead, if no games were found it will return an empty list
def search_game_request(game_name):

    url = 'https://api.igdb.com/v4/search'
    header_data = {'Client-ID':'oeo0x5v3bza05utlsgajehq2elvg6t', 'Authorization':'Bearer qa788f01fsmbzn1skgydmzc4vylpwz'}
    body_data = f'search "{game_name}"; fields name;'

    try:
        res = requests.post(url, data = body_data, headers = header_data)
        game_list = res.json()

    except Exception as e:
        return 'Failed'
        #todo add logging for the error 

    return game_list
    

if __name__ == '__main__':
    main()