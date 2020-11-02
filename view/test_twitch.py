import unittest
from unittest import TestCase
from unittest.mock import patch, call


import twitch

class Testtwitch(TestCase):
    @patch('twitch.get_current_streamers')
    def test_user_input(self,twitch_id):
        self.assertTrue(twitch.get_current_streamers(twitch_id).isalnum)# test checking input is only number

    @patch('twitch.get_current_streamers')# test checkin good game id
    def test_current_stream_by_ggod_id(self, mock_requests_json):
        mock_id = 417752
        example_api_response = {"data":{"game_id": mock_id}}
        mock_requests_json.return_value = example_api_response
        result = twitch.get_current_streamers(mock_id)
        self.assertEqual(example_api_response,result)


    @patch('twitch.get_current_streamers') # test checking bad game id
    def test_current_stream_by_bad_game_id(self,mock_requests_json):
        mock_id = 'hhhhhhhhhh'
        example_api_response = {"data":{"game_id": mock_id}}
        mock_requests_json.return_value = example_api_response
        result = twitch.get_current_streamers(mock_id)
        self.assertNotEqual(result,mock_id)

    
    @patch('twitch.get_current_streamers')
    def test_get_request_empty(self, mock_requests_get):
        mock_requests_get.return_value.status_code = [] 
        result = twitch.get_current_streamers()
        self.assertNotEqual(result, [])
 