
from model import config
config.db_path = 'test_game.sqlite'

from unittest import TestCase
from viewmodel.viewmodel import *
from web_interface.app import create_game_obj
from model import game


class TestDeleteGame(TestCase):

    def SetUp(self):
        game.db.drop_tables(MODELS)
        game.db.create_tables(MODELS)
        # create_game = add_game(fake_game_data,True)

    def test_delete_game_that_exists(self):

        # create_game = add_game(fake_game_data,True)
        # temp_game = find_game_by_igdb_id(394)
        # print(temp_game)
        delete = delete_game(394)
        print(delete)