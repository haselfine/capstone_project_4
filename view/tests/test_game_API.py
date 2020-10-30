from unittest import TestCase
from unittest.mock import patch

from view import game_API


example_api_response_game = ({'cover': {'id': 90046,
            'url': '//images.igdb.com/igdb/image/upload/t_thumb/co1xha.jpg'},
  'first_release_date': 1284422400,
  'id': 990,
  'name': 'Halo: Reach',
  'platforms': [{'id': 6, 'name': 'PC (Microsoft Windows)'},
                {'id': 12, 'name': 'Xbox 360'}],
  'rating': 85.46384505686581,
  'summary': 'Experience the story before the events of Halo: Combat Evolved '
             'as you fight to defend the planet Reach from a harrowing '
             'Covenant invasion. In this first-person shooter you can '
             'customize your own Spartan with armor and accessories to '
             'experience both a pulse-pounding campaign and addictive '
             "multiplayer mode. Reach will fall, but it won't go down without "
             'a fight.',
  'websites': [{'id': 2990,
                'url': 'https://www.halowaypoint.com/en-us/games/halo-reach/xbox-360'},
               {'id': 6032, 'url': 'http://halo.wikia.com/wiki/Halo:_Reach'},
               {'id': 6033, 'url': 'https://en.wikipedia.org/wiki/Halo:_Reach'},
               {'id': 126894,
                'url': 'https://store.steampowered.com/app/1064220/Halo_Reach/'}]},
 None)

class TestGameAPI(TestCase):

    def test_specific_game_search(self, mock_game_info):

        example_game_id = 990

        expected_data = example_api_response_game

        response_data = game_API.get_game_info(example_game_id)

        self.assertEqual(expected_data,game_data)

    
