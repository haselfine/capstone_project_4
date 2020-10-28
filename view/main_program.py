import logging
from pprint import pprint
import .web_interface.app as app

logging.basicConfig(filename='debug.log', level=logging.DEBUG, format=f'%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def main():
    app.start()



if __name__ == '__main__':
    main()
