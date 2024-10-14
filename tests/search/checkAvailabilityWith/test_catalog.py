from unittest import TestCase

from src.search.checkAvailabilityWith.catalog import check_availability_with_catalog
from src.utils.ApiResponse import ApiResponse
from tests.utils.TestToken import TestToken


# documentation : https://developers.traceparts.com/v2/reference/get_v2-search-catalog-availability


class Test(TestCase):
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.catalog_label: str = ""  # your catalog label

    def test_check_availability_with_catalog(self):
        response = ApiResponse(check_availability_with_catalog(token=TestToken,
                                                               catalog_label=self.catalog_label))
        print(response)
        self.assertEqual(200, response.status_code)

    def test_check_availability_with_catalog_with_empty_catalog_label(self):
        response = ApiResponse(check_availability_with_catalog(token=TestToken,
                                                               catalog_label=""))
        print(response)
        self.assertEqual(400, response.status_code)

    def test_check_availability_with_catalog_with_incorrect_catalog_label(self):
        response = ApiResponse(check_availability_with_catalog(token=TestToken,
                                                               catalog_label="INCORRECT"))
        print(response)
        self.assertEqual(404, response.status_code)
