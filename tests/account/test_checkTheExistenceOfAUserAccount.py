from unittest import TestCase

from src.account.checkTheExistenceOfAUserAccount import check_the_existence_of_a_user_account
from src.utils.ApiResponse import ApiResponse
from tests.utils.TestToken import TestToken


# documentation : https://developers.traceparts.com/v2/reference/get_v2-account-checklogin-useremail

class Test(TestCase):
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.user_email: str = ""  # your user email

    def test_check_the_existence_of_a_user_account(self):
        response = ApiResponse(check_the_existence_of_a_user_account(token=TestToken,
                                                                     user_email=self.user_email))
        print(response)
        self.assertEqual(200, response.status_code)

    def test_check_the_existence_of_a_user_account_with_invalid_user_email(self):
        response = ApiResponse(check_the_existence_of_a_user_account(token=TestToken,
                                                                     user_email="invalid_user_email"))
        print(response)
        self.assertEqual(400, response.status_code)

    def test_check_the_existence_of_a_user_account_with_incorrect_user_email(self):
        response = ApiResponse(
            check_the_existence_of_a_user_account(token=TestToken,
                                                  user_email="incorrectUserEmail@incorrect.com"))
        print(response)
        self.assertEqual(404, response.status_code)
