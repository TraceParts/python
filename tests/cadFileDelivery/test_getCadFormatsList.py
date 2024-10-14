from unittest import TestCase

from src.cadFileDelivery.getCadFormatsList import get_cad_formats_list
from src.utils.ApiResponse import ApiResponse
from tests.utils.TestToken import TestToken


# documentation : https://developers.traceparts.com/v2/reference/get_v3-product-caddataavailability

class Test(TestCase):
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.culture_info: str = ""  # your culture info
        self.optional_parameters: dict = {
            "partFamilyCode": "",  # your part family code
            "selectionPath": "",  # your selection path
            "classificationCode": "",  # your classification code
            "partNumber": "",  # your part number
        }

    def test_get_cad_formats_list(self):
        response = ApiResponse(get_cad_formats_list(token=TestToken,
                                                    optional_parameters=self.optional_parameters,
                                                    culture_info=self.culture_info))
        print(response)
        self.assertEqual(200, response.status_code)

    def test_get_cad_formats_list_with_no_optional_parameters(self):
        response = ApiResponse(get_cad_formats_list(token=TestToken,
                                                    optional_parameters={},
                                                    culture_info=self.culture_info))
        print(response)
        self.assertEqual(400, response.status_code)

    def test_get_cad_formats_list_with_empty_optional_parameters(self):
        response = ApiResponse(get_cad_formats_list(token=TestToken,
                                                    optional_parameters={
                                                        "partFamilyCode": "",
                                                        "selectionPath": "",
                                                        "classificationCode": "",
                                                        "partNumber": "",
                                                    },
                                                    culture_info=self.culture_info))
        print(response)
        self.assertEqual(400, response.status_code)

    def test_get_cad_formats_list_with_incorrect_optional_parameters(self):
        response = ApiResponse(get_cad_formats_list(token=TestToken,
                                                    optional_parameters={
                                                        "partFamilyCode": "00-00000000-000000",
                                                        "selectionPath": "0|0|0|0|0|0|0|0|0|=0|",
                                                        "classificationCode": "INCORRECT",
                                                        "partNumber": "00000",
                                                    },
                                                    culture_info=self.culture_info))
        print(response)
        self.assertEqual(404, response.status_code)

    def test_get_cad_formats_list_with_invalid_culture_info(self):
        response = ApiResponse(get_cad_formats_list(token=TestToken,
                                                    optional_parameters=self.optional_parameters,
                                                    culture_info="invalid_culture_info"))
        print(response)
        self.assertEqual(400, response.status_code)
