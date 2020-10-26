import logging
import requests
import os

logging.basicConfig(filename='debug.log', level=logging.DEBUG, format=f'%(asctime)s - %(name)s - %(levelname)s - %(message)s')
client = os.environ.get('CLIENT_ID')
api_auth = os.environ.get('AUTHORIZATION')

cloudinary_id = os.environ.get('CLOUD_ID')

def create_image_link(original_url):
    if original_url is not None:
        base_url = original_url.replace('t_thumb', 't_720p') #change from thumbnail to 720p image
        final_igdb_url = base_url[2:] #remove "//" from beginning
        return make_it_small(final_igdb_url)
    else:
        return None

def make_it_small(igdb_url): #cloudinary uses the igdb url to resize the image... We can use this 25,000 times for free. Limit game results. And use cache
    if len(cloudinary_id) > 0: #make sure it's the correct id
        cloudinary_url = f'https://res.cloudinary.com/{cloudinary_id}/image/fetch/w_150,f_auto/https://'
        return cloudinary_url + igdb_url
    else:
        error = ('Error', 'Need cloudinary ID')
        return None, error
