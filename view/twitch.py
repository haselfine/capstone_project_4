import requests
import os
import logging

client_id = os.environ.get('CLIENT_ID')
auth = os.environ.get('AUTHORIZATION')
twitch_base_url = 'twitch.tv/'

def get_twitch_game_id(game_name): #needs official game name from IGDB can't just be search
    url = f'https://api.twitch.tv/helix/games?name={game_name}'
    header_dict = {'Client-ID': client_id, 'Authorization': auth}

    try:
        response = requests.get(url, headers=header_dict)
        data = response.json()
        if len(data) > 0:
            return data['data'][0]['id'], None
        else:
            return None, 'No twitch_id found'
    except Exception as e:
        logging.error(e)
        return None, e
    
   
def get_current_streamers(twitch_id):
    url = f'https://api.twitch.tv/helix/streams?game_id={twitch_id}'
    header = {'Client-ID': client_id, 'Authorization': auth}
    
    if twitch_id is None:
        return [], 'No twitch_id'
    
    try:
        response = requests.get(url, headers= header)
        data = response.json()['data']
        
        if len(data) > 0:
            
            # extract username and make url based on it
            active_streamers = []
            for stream in data:
                streamer_name = stream['user_name']
                url = twitch_base_url + streamer_name
                
                stream_dict = {'streamer_name': streamer_name, 'url': url}
                active_streamers.append(stream_dict)
                
            return active_streamers, None
        
        else:
            return [], 'No active streamers'
        
    except Exception as e:
        logging.error(e)
        return [], e

def get_streamr_data_from_twitch(game_id):
    url = f'https://api.twitch.tv/helix/streams?game_id={game_id}'
    
    header = {'Client-ID': client_id, 'Authorization': auth}
    

    try:
        response = requests.get(url, headers= header)
        jsondata = response.json()
        return jsondata['data'][0]['user_name']
    except Exception as e:
        logging.error(f'Error checking user: ', e)
