import logging
import requests
import os

logging.basicConfig(filename='debug.log', level=logging.DEBUG, format=f'%(asctime)s - %(name)s - %(levelname)s - %(message)s')
client = os.environ.get('CLIENT_ID')
api_auth = os.environ.get('AUTHORIZATION')

def call_api_covers(game_id):
    url = 'https://api.igdb.com/v4/covers'
    header_dict = {'Client-ID': client, 'Authorization': api_auth}
    search_data = f'fields url; where game = {game_id};'

    if header_dict['Client-ID'] is not None and header_dict['Authorization'] is not None:
        try:
            api_request = requests.post(url, data=search_data, headers=header_dict)
            data = api_request.json()
        except Exception as e:
            logging.error(f'Something went wrong when calling the API: {e}')
            error = ('Error', data)
            return error
        create_image_link(data)
    else:
        error = ('Error', 'Need client-id and authorization key.')
        return error

def create_image_link(data):
    base_url = data[0]['url'].replace('t_thumb', 't_720p')
    final_url = base_url[2:]
    return final_url
