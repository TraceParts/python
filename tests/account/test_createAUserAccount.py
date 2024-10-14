from unittest import TestCase

from src.account.createAUserAccount import create_a_user_account
from src.utils.ApiResponse import ApiResponse
from tests.utils.TestToken import TestToken


# documentation : https://developers.traceparts.com/v2/reference/post_v2-account-signup
# 📘 Warning! Any tries will be recorded in the Production data.
class Test(TestCase):
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.options: dict = {"company": "python_unittest",
                              "country": "python_unittest",
                              "name": "python_unittest",
                              "fname": "python_unittest",
                              "addr1": "python_unittest",
                              "addr2": "python_unittest",
                              "addr3": "python_unittest",
                              "city": "python_unittest",
                              "state": "python_unittest",
                              "zipCode": "python_unittest",
                              "phone": "python_unittest",
                              "fax": "python_unittest",
                              "tpOptIn": False,
                              "partnersOptIn": False}
        self.user_email: str = ""  # your user email

    def test_create_a_user_account(self):
        response = ApiResponse(create_a_user_account(token=TestToken,
                                                     user_email=self.user_email,
                                                     optional_parameters=self.options))
        print(response)
        self.assertEqual(201, response.status_code)

    def test_create_a_user_account_with_invalid_user_email(self):
        response = ApiResponse(create_a_user_account(token=TestToken,
                                                     user_email="invalid_user_email",
                                                     optional_parameters=self.options))
        print(response)
        self.assertEqual(500, response.status_code)
