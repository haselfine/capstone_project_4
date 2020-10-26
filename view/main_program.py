# from project_4.viewmodel import *
import logging
import os
from pprint import pprint
import requests
import image

logging.basicConfig(filename='debug.log', level=logging.DEBUG, format=f'%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def main():
    api_image = image.call_api_covers(1000)
    print(api_image)
    #TODO connect to APIs
    #TODO search games in Steam, Twitch.tv
    #TODO store game info


    pass


if __name__ == '__main__':
    main()
