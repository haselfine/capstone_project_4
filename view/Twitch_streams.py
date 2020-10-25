import logging
import requests
import os
import json

def get_streamrs_data_from_twitch(game_id):
    url = f'https://api.twitch.tv/helix/streams?game_id={game_id}'
    client_id = os.environ.get('CLIENT_ID')
    key_auth = os.environ.get('AUTHORIZATION')

    header = {'Client-ID': client_id, 'Authorization': key_auth}
    

    try:
        response = requests.get(url, headers= header)
        jsondata = response.json()
        return jsondata['data'][0]['user_name']
    except Exception as e:
        logging.error(f'Error checking user: ', e)
        
