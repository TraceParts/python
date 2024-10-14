from unittest import TestCase

from src.dataIndexing.listOfProductsAndCategories import list_of_products_and_categories
from src.utils.ApiResponse import ApiResponse
from tests.utils.TestToken import TestToken


# documentation : https://developers.traceparts.com/v2/reference/get_v2-search-productandcategorylist

class Test(TestCase):
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.part_family_code: str = ""  # your part family code
        self.classification_code: str = ""  # your classification code

    def test_list_of_products_and_categories(self):
        response = ApiResponse(
            list_of_products_and_categories(token=TestToken,
                                            classification_code=self.classification_code,
                                            part_family_code=self.part_family_code))
        print(response)
        self.assertEqual(200, response.status_code)

    def test_list_of_products_and_categories_with_empty_part_family_code(self):
        response = ApiResponse(
            list_of_products_and_categories(token=TestToken,
                                            classification_code=self.classification_code,
                                            part_family_code=""))
        print(response)
        self.assertEqual(200, response.status_code)

    def test_list_of_products_and_categories_with_empty_classification_code(self):
        response = ApiResponse(
            list_of_products_and_categories(token=TestToken,
                                            classification_code="",
                                            part_family_code=self.part_family_code))
        print(response)
        self.assertEqual(400, response.status_code)

    def test_list_of_products_and_categories_with_incorrect_classification_code(self):
        response = ApiResponse(
            list_of_products_and_categories(token=TestToken,
                                            classification_code="INCORRECT",
                                            part_family_code=self.part_family_code))
        print(response)
        self.assertEqual(404, response.status_code)

    def test_list_of_products_and_categories_with_incorrect_part_family_code(self):
        response = ApiResponse(
            list_of_products_and_categories(token=TestToken,
                                            classification_code=self.classification_code,
                                            part_family_code="00-00000000-000000"))
        print(response)
        self.assertEqual(404, response.status_code)
