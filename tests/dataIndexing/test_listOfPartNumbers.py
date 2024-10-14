from unittest import TestCase

from src.dataIndexing.listOfPartNumbers import list_of_part_numbers
from src.utils.ApiResponse import ApiResponse
from tests.utils.TestToken import TestToken


# documentation : https://developers.traceparts.com/v2/reference/get_v1-search-partnumberlist

class Test(TestCase):
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.return_your_own_codes: bool = False  # your choice for return your own codes
        self.part_family_code: str = ""  # your part family code

    def test_list_of_part_numbers(self):
        response = ApiResponse(list_of_part_numbers(token=TestToken,
                                                    part_family_code=self.part_family_code,
                                                    return_your_own_codes=self.return_your_own_codes))
        print(response)
        self.assertEqual(200, response.status_code)

    def test_list_of_part_numbers_with_empty_part_family_code(self):
        response = ApiResponse(list_of_part_numbers(token=TestToken,
                                                    part_family_code="",
                                                    return_your_own_codes=self.return_your_own_codes))
        print(response)
        self.assertEqual(400, response.status_code)

    def test_list_of_part_numbers_with_incorrect_part_family_code(self):
        response = ApiResponse(list_of_part_numbers(token=TestToken,
                                                    part_family_code="00-00000000-000000",
                                                    return_your_own_codes=self.return_your_own_codes))
        print(response)
        self.assertEqual(404, response.status_code)

    def test_list_of_part_numbers_with_invalid_part_family_code(self):
        response = ApiResponse(list_of_part_numbers(token=TestToken,
                                                    part_family_code="invalid_part_family_code",
                                                    return_your_own_codes=self.return_your_own_codes))
        print(response)
        self.assertEqual(400, response.status_code)
