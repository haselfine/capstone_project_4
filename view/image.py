import logging
import requests
import os

logging.basicConfig(filename='debug.log', level=logging.DEBUG, format=f'%(asctime)s - %(name)s - %(levelname)s - %(message)s')
client = os.environ.get('CLIENT_ID')
api_auth = os.environ.get('AUTHORIZATION')

cloudinary_id = os.environ.get('CLOUD_ID')
cloudinary_url = f'https://res.cloudinary.com/{cloudinary_id}/image/fetch/w_300,f_auto/https://'

def create_image_link(original_url):
    if original_url is None:
        return None, 'Original url was empty'
    if str(original_url)[0:2]=='//':
        base_url = original_url.replace('t_thumb', 't_720p') #change from thumbnail to 720p image
        final_igdb_url = base_url[2:] #remove "//" from beginning
        return make_it_small(final_igdb_url)
    else:
        return None, 'Url must be from IGDB'

def make_it_small(igdb_url): #cloudinary uses the igdb url to resize the image... Can be used to fetch 25,000 unique images for free.
    if igdb_url is None:
        return None, 'IGDB url was empty'
    if cloudinary_id is not None and len(cloudinary_id) > 0: #make sure it's the correct id
        return cloudinary_url + igdb_url #Cloudinary already caches images for the user, so implementing caching here is unnecessary. See https://support.cloudinary.com/hc/en-us/articles/207307269-For-how-long-does-Cloudinary-cache-my-delivered-content-on-the-CDN-
    else:
        error = 'Need cloudinary ID'
        return None, error
