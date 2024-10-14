from unittest import TestCase

from src.dataIndexing.catalogContactDetails import catalog_contact_details
from src.utils.ApiResponse import ApiResponse
from tests.utils.TestToken import TestToken


# documentation : https://developers.traceparts.com/v2/reference/get_v1-contact-catalog

class Test(TestCase):
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.classification_code: str = ""  # you classification code

    def test_catalog_contact_details(self):
        response = ApiResponse(catalog_contact_details(token=TestToken,
                                                       classification_code=self.classification_code))
        print(response)
        self.assertEqual(200, response.status_code)

    def test_catalog_contact_details_with_incorrect_classification_code(self):
        response = ApiResponse(catalog_contact_details(token=TestToken,
                                                       classification_code="INCORRECT"))
        print(response)
        self.assertEqual(404, response.status_code)

    def test_catalog_contact_details_with_empty_classification_code(self):
        response = ApiResponse(catalog_contact_details(token=TestToken,
                                                       classification_code=""))
        print(response)
        self.assertEqual(400, response.status_code)
