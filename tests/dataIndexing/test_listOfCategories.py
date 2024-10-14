from unittest import TestCase

from src.dataIndexing.listOfCategories import list_of_categories
from src.utils.ApiResponse import ApiResponse
from tests.utils.TestToken import TestToken


# documentation : https://developers.traceparts.com/v2/reference/get_v2-search-categorylist

class Test(TestCase):
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.culture_info: str = ""  # your culture info
        self.classification_code: str = ""  # your culture info

    def test_list_of_categories(self):
        response = ApiResponse(list_of_categories(token=TestToken,
                                                  classification_code=self.classification_code,
                                                  culture_info=self.culture_info))
        print(response)
        self.assertEqual(200, response.status_code)

    def test_list_of_categories_with_empty_classification_code(self):
        response = ApiResponse(list_of_categories(token=TestToken,
                                                  classification_code="",
                                                  culture_info=self.culture_info))
        print(response)
        self.assertEqual(400, response.status_code)

    def test_list_of_categories_with_incorrect_classification_code(self):
        response = ApiResponse(list_of_categories(token=TestToken,
                                                  classification_code="INCORRECT",
                                                  culture_info=self.culture_info))
        print(response)
        self.assertEqual(404, response.status_code)

    def test_list_of_categories_with_empty_culture_info(self):
        response = ApiResponse(list_of_categories(token=TestToken,
                                                  classification_code=self.classification_code,
                                                  culture_info=""))
        print(response)
        self.assertEqual(400, response.status_code)

    def test_list_of_categories_with_invalid_culture_info(self):
        response = ApiResponse(list_of_categories(token=TestToken,
                                                  classification_code=self.classification_code,
                                                  culture_info="invalid_culture_info"))
        print(response)
        self.assertEqual(500, response.status_code)
