import unittest

from main import get_joke
from unittest.mock import patch, MagicMock


class TestSuite(unittest.TestCase):

    # test happy path where response is 200
    @patch('main.requests')
    def x_get_joke(self, mock_requests):
        # then set up magicmock object with mocked values to return
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'value': {'joke': 'hello world'}}

        # first - need to set mock request of get method set to an object
        mock_requests.get.return_value = mock_response

        self.assertEqual(get_joke(), "hello world")

    # test sad path where response > 200
    @patch('main.requests')
    def test_sad_path_get_joke(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_requests.get.return_value = mock_response

        self.assertEqual(get_joke(), "No jokes")


if __name__ == "__main__":
    unittest.main(verbosity=2)  # pragma: no cover
