import requests
import os
import logging

client_id = os.environ.get('CLIENT_ID')
auth = os.environ.get('AUTHORIZATION')

def get_twitch_game_id(game_name): #needs official game name from IGDB can't just be search
    url = f'https://api.twitch.tv/helix/games?name={game_name}'
    header_dict = {'Client-ID': client_id, 'Authorization': auth}

    try:
        response = requests.get(url, headers=header_dict)
        data = response.json()
        return data['data'][0]['id'], None
    except Exception as e:
        logging.error(f'Something went wrong when calling the API: {e}')
        error = ('Error', data)
        return None, error
   
def get_current_streamers(twitch_id):
    url = f'https://api.twitch.tv/helix/streams?game_id={twitch_id}'
    header = {'Client-ID': client_id, 'Authorization': key_auth}
    
    try:
        response = requests.get(url, headers= header)
        jsondata = response.json()
        return jsondata['data'][0]['user_name'], None
    except Exception as e:
        logging.error(f'Error checking user: ', e)
        return None, e
    