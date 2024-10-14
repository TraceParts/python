from unittest import TestCase

from src.common.getLanguagesList import get_languages_list
from src.utils.ApiResponse import ApiResponse
from tests.utils.TestToken import TestToken


# documentation : https://developers.traceparts.com/v2/reference/get_v2-supportedlanguages


class Test(TestCase):
    def test_get_languages_list(self):
        response = ApiResponse(get_languages_list(token=TestToken))
        print(response)
        self.assertEqual(200, response.status_code)
