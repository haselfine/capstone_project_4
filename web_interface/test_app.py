from unittest import TestCase
from unittest.mock import patch

import app


example_response_search_games =[{'id': 740, 'name': 'Halo: Combat Evolved'},
 {'id': 6803, 'name': 'Halo 5: Guardians'},
 {'id': 7348, 'name': 'Halo: The Master Chief Collection'},
 {'id': 2640, 'name': 'Halo: Combat Evolved Anniversary'},
 {'id': 45148, 'name': 'Halo 4: Limited Edition'},
 {'id': 989, 'name': 'Halo 3: ODST'},
 {'id': 991, 'name': 'Halo 4'},
 {'id': 77343, 'name': 'Halo 4: King of the Hill Fueled by Mountain Dew'},
 {'id': 103281, 'name': 'Halo Infinite'},
 {'id': 987, 'name': 'Halo 3'}]


class TestGameAPI(TestCase):

    # making a requrest where the game is not found and making sure that an error message is returned
    # def test_search_games_game_not_found(self):

    #     example_search = 'gosajrpjepjfaljdpsa'

    #     response_data = game_API.search_game_request(example_search)

    #     self.assertIsNotNone(response_data[1])

    # testing the results of a correct search and making sure the proper data is returned
    # def test_search_games_correct_data(self):

    #     example_search = 'halo'

    #     response_data, error = game_API.search_game_request(example_search)

    #     self.assertIsNone(error)
    #     self.assertEqual(example_response_search_games, response_data)

    # testing the results of trying to get a game but inputting a string instead of the int game code,
    # making sure that the expected error is returned
    @patch('app.get_game_info')
    def test_create_game_obj_with_string(self, mock_response):

        example_search = 'lgjsldjf'

        example_response = (error,('Expecting a STRING as input, surround your input with quotes starting at '
 "'lgjsldjf' expecting {'{', 'f', '(', '[', 'true', 't', 'false', 'null', 'n'"))

        mock_response.side_efffect = [example_response]

        data = app.create_game_obj(example_search)

        self.assertIsNone(response_data)
       

    #again searching for game but by id 0 and making sure none is returned for data, and the exception is also returned
    @patch('app.get_game_info')   
    def test_create(self, mock_response):
        example_search = 0

        example_response = (None, IndexError('list index out of range'))
        mock_response.side_efffect = [example_response]

        data = app.create_game_obj(example_search)

        self.assertIsNone(data)







        

    
