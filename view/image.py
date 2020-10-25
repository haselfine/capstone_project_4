import logging
import requests
import os

logging.basicConfig(filename='debug.log', level=logging.DEBUG, format=f'%(asctime)s - %(name)s - %(levelname)s - %(message)s')
client = os.environ.get('CLIENT_ID')
api_auth = os.environ.get('AUTHORIZATION')

cloudinary_id = os.environ.get('CLOUD_ID')

def call_api_covers(game_id):
    url = 'https://api.igdb.com/v4/covers'
    header_dict = {'Client-ID': client, 'Authorization': api_auth}
    search_data = f'fields url; where game = {game_id};'

    if header_dict['Client-ID'] is not None and header_dict['Authorization'] is not None:
        try:
            api_request = requests.post(url, data=search_data, headers=header_dict)
            data = api_request.json()
            
            if len(data) > 0:
                return create_image_link(data), None
            else:
                error = ('Error', 'No image url found')
                return None, error
            
        except Exception as e:
            logging.debug(f'Something went wrong when calling the API: {e}')
            error = ('Error', data)
            return None, error
    
    else:
        error = ('Error', 'Need client-id and authorization key.')
        return None, error

def create_image_link(data):
    base_url = data[0]['url'].replace('t_thumb', 't_720p') #change from thumbnail to 720p image
    final_igdb_url = base_url[2:] #remove "//" from beginning
    return make_it_small(final_igdb_url)

def make_it_small(igdb_url): #cloudinary uses the igdb url to resize the image... We can use this 25,000 times for free. Limit game results. And use cache
    if len(cloudinary_id > 0): #make sure it's the correct id
        cloudinary_url = f'https://res.cloudinary.com/{cloudinary_id}/image/fetch/w_150,f_auto/https://'
        return cloudinary_url + igdb_url
    else:
        error = ('Error', 'Need cloudinary ID')
        return None, error