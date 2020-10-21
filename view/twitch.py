import requests
import os
import logging

client_id = os.environ.get('CLIENT_ID')
auth = os.environ.get('AUTHORIZATION')

def get_twitch_game_id(game_name): #needs official game name from IGDB can't just be search
    url = f'https://api.twitch.tv/helix/games?name={game_name}'
    header_dict = {'Client-ID': client_id, 'Authorization': "Bearer " + auth}

    try:
        response = requests.get(url, headers=header_dict)
        data = response.json()
        return data['data'][0]['id']
    except Exception as e:
        logging.error(f'Something went wrong when calling the API: {e}')
        error = ('Error', data)
        return None, error