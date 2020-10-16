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

    try:
        api_request = requests.post(url, data=search_data, headers=header_dict)
        cover = api_request.json()
        create_image_link(cover)
    except Exception as e:
        logging.error(f'Something went wrong when calling the API: {e}')
        return None

def create_image_link(cover):
    base_url = cover.url.replace('t_thumb', 't_720p')
    final_url = base_url[:2]
    print(final_url)

call_api_covers(1000)
