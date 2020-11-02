from model import config
config.db_path = 'test_game.sqlite'

from unittest import TestCase
from viewmodel.viewmodel import *
from web_interface.app import create_game_obj
from model import game
from view import game_API

MODELS = [Game]

class TestFindGameByIgbdId(TestCase):

    def SetUp(self):
        game.db.drop_tables(MODELS)
        game.db.create_tables(MODELS)

    
  	# Making sure only we get game  by igbd_id
    def test_find_game_by_igbd_id(self):
        Game = find_game_by_igdb_id()
        self.assertEqual(igdb_id)
    #testing find game by good id
    def test_find_game_by_igbd_good_id(self):
        game_id = 417752
        response = find_game_by_igdb_id(igdb_id= game_id)
        self.assertEqual(response[0])
    #testing find game by bad id
    def test_find_game_by_igbd_bad_id(self):
        bad_igdb_id = ('hhhhhhh', 000000000,"yyy7788kkk", 8888888888888)
        for i in bad_igdb_id:
            response = find_game_by_igdb_id(i,True)
            self.assertIsNone(response[0])
    #test no id
    def test_find_game_no_id(self):
        response = find_game_by_igdb_id(None, False)
        self.assertEqual((None), response)
