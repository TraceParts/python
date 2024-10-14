from unittest import TestCase

from src.dataIndexing.listOfCatalogs import list_of_catalogs
from src.utils.ApiResponse import ApiResponse
from tests.utils.TestToken import TestToken


# documentation : https://developers.traceparts.com/v2/reference/get_v2-search-cataloglist


class Test(TestCase):
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.culture_info: str = ""  # your culture info

    def test_list_of_catalogs(self):
        response = ApiResponse(list_of_catalogs(token=TestToken,
                                                culture_info=self.culture_info))
        print(response)
        self.assertEqual(200, response.status_code)

    def test_list_of_catalogs_with_invalid_culture_info(self):
        response = ApiResponse(list_of_catalogs(token=TestToken,
                                                culture_info="invalid_culture_info"))
        print(response)
        self.assertEqual(500, response.status_code)

    def test_list_of_catalogs_with_empty_culture_info(self):
        response = ApiResponse(list_of_catalogs(token=TestToken,
                                                culture_info=""))
        print(response)
        self.assertEqual(400, response.status_code)
