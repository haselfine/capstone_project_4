from unittest import TestCase
from unittest.mock import patch

from view import game_API


class TestGameAPI(TestCase):

    @patch('game_API.get_game_info')
    def test_specific_game_search(self, mock_game_info):

        example_game_id = 999

        example_api_response = 
    
