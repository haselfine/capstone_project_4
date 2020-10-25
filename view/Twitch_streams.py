import logging
import requests
import os
import json

url = 'https://api.twitch.tv/helix/streams'
client_id = os.environ.get('CLIENT_ID')
auth_key = os.environ.get('AUTHORIZATION')

Api_headers = {'Client-ID': client_id , 'Authorization': auth_key}

def get_live_stream_data(game_id):
    query =f'{game_id}' 
    response = requests.get(url,  headers = Api_headers)
    streamer_data = response.json()
    return streamer_data

def get_streamer_name_url(streamer_data):
    mylist = []
    
    result = streamer_data['data']
    for  stream in result:
      
        streamer_name = stream['user_name']
        streamer_url = stream['thumbnail_url']
        my_dic = {streamer_name:streamer_url}
        mylist.append(my_dic)
        
    return mylist