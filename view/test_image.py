import os
from unittest import TestCase
from unittest.mock import patch, call
from image import cloudinary_id, cloudinary_url, create_image_link, make_it_small

test_igdb_url = '//images.igdb.com/igdb/image/upload/t_thumb/co1trg.jpg'
test_cloud_url = f'http://this-is-made-up.abc/{cloudinary_id}/image/fetch/w_300,f_auto/https://'

@patch('image.cloudinary_url', new=test_cloud_url)
class TestImage(TestCase):

    def test_image_good_data(self):
        self.assertEqual(f'{test_cloud_url}images.igdb.com/igdb/image/upload/t_720p/co1trg.jpg', create_image_link(test_igdb_url))

    def test_image_bad_data(self):
        bad_data = [123456789, '😃🧘🏻‍♂️🌍🍞🚗📞', 'asdflkjl;']
        for item in bad_data:
            self.assertEqual((None, 'Url must be from IGDB'), create_image_link(item))

    def test_create_link_none_data(self):
        self.assertEqual((None, 'Original url was empty'), create_image_link(None))
        self.assertEqual((None, 'IGDB url was empty'), make_it_small(None))

    @patch('image.cloudinary_id', side_effect=[''])
    def test_no_cloud_id(self, mock_input):
        self.assertEqual((None, 'Need cloudinary ID'), create_image_link(test_igdb_url))