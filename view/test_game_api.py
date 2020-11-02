from unittest import TestCase
from unittest.mock import patch

import game_API


class TestGameAPI(TestCase):

    
    # making a requrest where the game is not found and making sure that an error message is returned
    @patch('requests.get')
    def test_search_games_game_not_found(self):

        example_search = 'gosajrpjepjfaljdpsa'

        response_data = game_API.search_game_request(example_search)
        mock_requests_get().json.return_value = example_api_response


        self.assertIsNotNone(response_data[1])


    # testing the results of trying to get a game but inputting a string instead of the int game code,
    # making sure that the expected error is returned
    def test_get_game_info_string_input(self):

        example_search = 'lgjsldjf'

        response_data, error = game_API.get_game_info(example_search)

        self.assertIsNone(response_data)
        self.assertEqual(error,('Expecting a STRING as input, surround your input with quotes starting at '
 "'lgjsldjf' expecting {'{', 'f', '(', '[', 'true', 't', 'false', 'null', 'n'"))

    #again searching for game but by id 0 and making sure none is returned for data, and the exception is also returned
    # def test_get_game_info_number_0(self):

    #     example_search = 0

    #     response data, error = game_API.get_game_info(example_search)

    #     self.assertIsNone(response_data)
    #     self.assertIsNotNone(error)






        

    
