from unittest import TestCase

from src.dataIndexing.listOfProducts import list_of_products
from src.utils.ApiResponse import ApiResponse
from tests.utils.TestToken import TestToken


# documentation : https://developers.traceparts.com/v2/reference/get_v2-search-productlist


class Test(TestCase):
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.category_code: str = ""  # your category code
        self.classification_code: str = ""  # your classification code
        self.culture_info: str = ""  # your culture info

    def test_list_of_products(self):
        response = ApiResponse(list_of_products(token=TestToken,
                                                culture_info=self.culture_info,
                                                classification_code=self.classification_code,
                                                category_code=self.category_code))
        print(response)
        self.assertEqual(200, response.status_code)
        self.assertIsNotNone(response.body)

    def test_list_of_products_with_empty_culture_info(self):
        response = ApiResponse(list_of_products(token=TestToken,
                                                culture_info="",
                                                classification_code=self.classification_code,
                                                category_code=self.category_code))
        print(response)
        self.assertEqual(400, response.status_code)

    def test_list_of_products_with_invalid_culture_info(self):
        response = ApiResponse(list_of_products(token=TestToken,
                                                culture_info="invalid_culture_info",
                                                classification_code=self.classification_code,
                                                category_code=self.category_code))
        print(response)
        self.assertEqual(200, response.status_code)
        self.assertIsNone(response.body)

    def test_list_of_products_with_empty_classification_code(self):
        response = ApiResponse(list_of_products(token=TestToken,
                                                culture_info=self.culture_info,
                                                classification_code="",
                                                category_code=self.category_code))
        print(response)
        self.assertEqual(400, response.status_code)

    def test_list_of_products_with_incorrect_classification_code(self):
        response = ApiResponse(list_of_products(token=TestToken,
                                                culture_info=self.culture_info,
                                                classification_code="INCORRECT",
                                                category_code=self.category_code))
        print(response)
        self.assertEqual(200, response.status_code)
        self.assertIsNone(response.body)

    def test_list_of_products_with_empty_category_code(self):
        response = ApiResponse(list_of_products(token=TestToken,
                                                culture_info=self.culture_info,
                                                classification_code=self.classification_code,
                                                category_code=""))
        print(response)
        self.assertEqual(200, response.status_code)
        self.assertIsNone(response.body)

    def test_list_of_products_with_incorrect_category_code(self):
        response = ApiResponse(list_of_products(token=TestToken,
                                                culture_info=self.culture_info,
                                                classification_code=self.classification_code,
                                                category_code="INCORRECT.10.010"))
        print(response)
        self.assertEqual(200, response.status_code)
        self.assertIsNone(response.body)
