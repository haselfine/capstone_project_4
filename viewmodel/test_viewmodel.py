from model import config
config.db_path = 'test_game.sqlite'

from unittest import TestCase
from viewmodel.viewmodel import *
from web_interface.app import create_game_obj
from model import game

MODELS = [Game]

fake_game_data = {'name': 'Final Fantasy Tactics: The War of the Lions', 
'summary': 'An updated version of the PlayStation game Final Fantasy Tactics, released on PlayStation Portable and later released on iOS and Android.    &#34;The stage is set for what history would one day record as the War of the Lions.    Experience new CG cinematics. Meet new Characters. Explore new jobs &amp; missions. Wage new multiplayer battles. Behold a new legend!&#34;', 
'first_release_date': '1178582400', 
'rating': '85', 
'image_url': 'https://res.cloudinary.com/div5hxdz2/image/fetch/w_300,f_auto/https://images.igdb.com/igdb/image/upload/t_720p/co1pn8.jpg', 
'platforms': '[&#39;Android&#39;, &#39;PlayStation Portable&#39;, &#39;iOS&#39;, &#39;PlayStation Network&#39;]', 
'websites': '[&#39;https://en.wikipedia.org/wiki/Final_Fantasy_Tactics:_The_War_of_the_Lions&#39;, &#39;https://itunes.apple.com/us/app/final-fantasy-tactics-the-war-of-the-lions-ipad/id500098096?mt=8&amp;uo=4&#39;, &#39;https://play.google.com/store/apps/details?id=com.square_enix.android_googleplay.FFT_en2&amp;hl=en&amp;gl=us&#39;]', 
'id': '394'}

class TestAddGame(TestCase):

    def SetUp(self):
        game.db.drop_tables(MODELS)
        game.db.create_tables(MODELS)

    def test_add_game_none_data(self):
        temp_game = add_game(None, False)
        self.assertEqual((None, 'No game data'), temp_game)

    def test_add_game_good_data(self):
        create_game = add_game(fake_game_data, False)
        temp_game = find_game_by_igdb_id(394)
        expected_data = "(<Game: 1, Final Fantasy Tactics: The War of the Lions, An updated version of the PlayStation game Final Fantasy Tactics, released on PlayStation Portable and later released on iOS and Android.    &#34;The stage is set for what history would one day record as the War of the Lions.    Experience new CG cinematics. Meet new Characters. Explore new jobs &amp; missions. Wage new multiplayer battles. Behold a new legend!&#34;, 2007-05-07, 2007-05-07 19:00:00, 85, https://res.cloudinary.com/div5hxdz2/image/fetch/w_300,f_auto/https://images.igdb.com/igdb/image/upload/t_720p/co1pn8.jpg, ['Android', 'PlayStation Portable', 'iOS', 'PlayStation Network'], ['https://en.wikipedia.org/wiki/Final_Fantasy_Tactics:_The_War_of_the_Lions', 'https://itunes.apple.com/us/app/final-fantasy-tactics-the-war-of-the-lions-ipad/id500098096?mt=8&amp;uo=4', 'https://play.google.com/store/apps/details?id=com.square_enix.android_googleplay.FFT_en2&amp;hl=en&amp;gl=us'], 394, 25244>, None)"
        self.assertEqual(expected_data, str(temp_game))

    def test_add_game_bad_data(self):
        bad_data = [{'name':''}, {'name':'NULL'},{'name':12345, 'summary':12345, 'first_release_date':12345, 'rating':12345, 'image_url': 12345, 'platforms':'[12345]', 'websites':12345, 'id':12345}]
        for item in bad_data:
            create_game = add_game(item, True)
            self.assertIsNone(create_game[0])
        
    def test_add_game_no_id(self):
        fake_game_data['id']=''
        create_game = add_game(fake_game_data, True)
        create_game_not_api = add_game(fake_game_data, False)
        self.assertIsNone(create_game[0])
        self.assertIsNone(create_game_not_api[0])

class TestDeleteGame(TestCase):

    def SetUp(self):
        game.db.drop_tables(MODELS)
        game.db.create_tables(MODELS)
        # create_game = add_game(fake_game_data,True)

    def test_delete_game_that_exists(self):

        # create_game = add_game(fake_game_data,True)
        temp_game = find_game_by_igdb_id(394)
        print(temp_game)
        delete = delete_game(394)
        print(delete)
        