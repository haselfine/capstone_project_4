import unittest
from unittest import TestCase
from unittest.mock import patch, call


import twitch

class Testtwitch(TestCase):
    @patch('twitch.get_current_streamers')
    def test_user_input(self,twitch_id):
        self.assertTrue(twitch.get_current_streamers(twitch_id).isalnum)# test checking input is only number

    @patch('twitch.get_current_streamers')# test checkin good data
    def test_current_stream(self, mock_requests_json):
        mock_id = 417752
        example_api_response = {"data":{"game_id": mock_id}}
        mock_requests_json.return_value = example_api_response
        result = twitch.get_current_streamers(mock_id)
        self.assertEqual(example_api_response,result)


    @patch('twitch.get_current_streamers') # test checking bad data
    def test_search_games_game_not_found(self,mock_requests_json):
        mock_id = 'hhhhhhhhhh'
        example_api_response = {"data":{"game_id": mock_id}}
        mock_requests_json.return_value = example_api_response
        result = twitch.get_current_streamers(mock_id)
        self.assertNotEqual(result,mock_id)
