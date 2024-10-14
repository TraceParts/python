import re
import unittest

from src.common.getLanguagesList import get_languages_list
from src.utils.ApiResponse import ApiResponse

TestToken = ""  # you can enter here a token so all other tests will use it instead of rewritten it everytime


def get_incorrect_test_token():
    last_char = TestToken[-1]
    if re.match(r"^\d$", last_char):
        # last char is a digit
        new_last_char = "A"
    else:
        # last char is NOT a digit
        new_last_char = "1"
    incorrect_test_token = TestToken[:-1] + new_last_char
    return incorrect_test_token


class MyTestCase(unittest.TestCase):
    def test_token_format(self):
        self.assertRegex(TestToken, r"^[\w-]+\.[\w-]+\.[\w-]+$")

    def test_token(self):
        response = ApiResponse(get_languages_list(token=TestToken))
        print(response)
        self.assertEqual(200, response.status_code)

    def test_incorrect_token(self):
        response = ApiResponse(get_languages_list(token=get_incorrect_test_token()))
        print(response)
        self.assertEqual(401, response.status_code)
