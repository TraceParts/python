from unittest import TestCase

from src.cadFileDelivery.requestACadFile import request_a_cad_file
from src.utils.ApiResponse import ApiResponse
from tests.utils.TestToken import TestToken


# documentation : https://developers.traceparts.com/v2/reference/post_v3-product-cadrequest
# 📘 Warning! Any tries will be recorded in the Production data.
class Test(TestCase):
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.optional_parameters: dict = {
            "partFamilyCode": "",  # your part family code
            "selectionPath": "",  # your selection path
            "classificationCode": "",  # your classification code
            "partNumber": "",  # your part number

            "cadDetailLevelId": "",  # your cad detail level id
            "languageId": "",  # [DEPRECATED] your language ID
        }
        self.cad_format_id: int = 0  # your cad format list
        self.culture_info: str = ""  # your culture info
        self.user_email: str = ""  # your user email

    def test_request_a_cad_file(self):
        response = ApiResponse(
            request_a_cad_file(token=TestToken, user_email=self.user_email, culture_info=self.culture_info,
                               cad_format_id=self.cad_format_id, optional_parameters=self.optional_parameters))
        print(response)
        self.assertEqual(200, response.status_code)

    def test_request_a_cad_file_with_invalid_user_email(self):
        response = ApiResponse(
            request_a_cad_file(token=TestToken, user_email="invalid_user_email", culture_info=self.culture_info,
                               cad_format_id=self.cad_format_id, optional_parameters=self.optional_parameters))
        print(response)
        self.assertEqual(400, response.status_code)

    def test_request_a_cad_file_with_incorrect_user_email(self):
        response = ApiResponse(
            request_a_cad_file(token=TestToken, user_email="incorrectUserEmail@incorrect.com",
                               culture_info=self.culture_info,
                               cad_format_id=self.cad_format_id, optional_parameters=self.optional_parameters))
        print(response)
        self.assertEqual(404, response.status_code)

    def test_request_a_cad_file_with_invalid_culture_info(self):
        response = ApiResponse(
            request_a_cad_file(token=TestToken, user_email=self.user_email, culture_info="invalid_culture_info",
                               cad_format_id=self.cad_format_id, optional_parameters=self.optional_parameters))
        print(response)
        self.assertEqual(500, response.status_code)

    def test_request_a_cad_file_with_empty_culture_info(self):
        response = ApiResponse(
            request_a_cad_file(token=TestToken, user_email=self.user_email, culture_info="",
                               cad_format_id=self.cad_format_id, optional_parameters=self.optional_parameters))
        print(response)
        self.assertEqual(400, response.status_code)

    def test_request_a_cad_file_with_incorrect_cad_format_id(self):
        response = ApiResponse(
            request_a_cad_file(token=TestToken,
                               user_email=self.user_email,
                               culture_info=self.culture_info,
                               cad_format_id=-1,
                               optional_parameters=self.optional_parameters))
        print(response)
        self.assertEqual(500, response.status_code)

    def test_request_a_cad_file_with_no_optional_parameters(self):
        response = ApiResponse(
            request_a_cad_file(token=TestToken,
                               user_email=self.user_email,
                               culture_info=self.culture_info,
                               cad_format_id=self.cad_format_id,
                               optional_parameters={}))
        print(response)
        self.assertEqual(400, response.status_code)

    def test_request_a_cad_file_with_empty_optional_parameters(self):
        response = ApiResponse(
            request_a_cad_file(token=TestToken,
                               user_email=self.user_email,
                               culture_info=self.culture_info,
                               cad_format_id=self.cad_format_id,
                               optional_parameters=
                               {
                                   "partFamilyCode": "",
                                   "selectionPath": "",
                                   "classificationCode": "",
                                   "partNumber": "",
                               }))
        print(response)
        self.assertEqual(400, response.status_code)

    def test_request_a_cad_file_with_incorrect_optional_parameters(self):
        response = ApiResponse(
            request_a_cad_file(token=TestToken,
                               user_email=self.user_email,
                               culture_info=self.culture_info,
                               cad_format_id=self.cad_format_id,
                               optional_parameters=
                               {
                                   "partFamilyCode": "00-00000000-000000",
                                   "selectionPath": "0|0|0|0|0|0|0|0|0|=0|",
                                   "classificationCode": "INCORRECT",
                                   "partNumber": "00000",
                               }))
        print(response)
        self.assertEqual(404, response.status_code)
