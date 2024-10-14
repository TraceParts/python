from unittest import TestCase

from src.search.checkAvailabilityWith.partNumber import check_availability_with_part_number
from src.utils.ApiResponse import ApiResponse
from tests.utils.TestToken import TestToken


# documentation : https://developers.traceparts.com/v2/reference/get_v2-search-partnumber-availability

class Test(TestCase):
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.remove_char: bool = False  # your choice for remove char
        self.catalog_label: str = ""  # your catalog label
        self.part_number: str = ""  # your part number

    def test_check_availability_with_part_number(self):
        response = ApiResponse(check_availability_with_part_number(token=TestToken,
                                                                   part_number=self.part_number,
                                                                   catalog_label=self.catalog_label,
                                                                   remove_char=self.remove_char))
        print(response)
        self.assertEqual(200, response.status_code)

    def test_check_availability_with_part_number_with_empty_part_number(self):
        response = ApiResponse(check_availability_with_part_number(token=TestToken,
                                                                   part_number="",
                                                                   catalog_label=self.catalog_label,
                                                                   remove_char=self.remove_char))
        print(response)
        self.assertEqual(400, response.status_code)

    def test_check_availability_with_part_number_with_incorrect_part_number(self):
        response = ApiResponse(check_availability_with_part_number(token=TestToken,
                                                                   part_number="00000",
                                                                   catalog_label=self.catalog_label,
                                                                   remove_char=self.remove_char))
        print(response)
        self.assertEqual(404, response.status_code)

    def test_check_availability_with_part_number_with_empty_catalog_label(self):
        response = ApiResponse(check_availability_with_part_number(token=TestToken,
                                                                   part_number=self.part_number,
                                                                   catalog_label="",
                                                                   remove_char=self.remove_char))
        print(response)
        self.assertEqual(400, response.status_code)

    def test_check_availability_with_part_number_with_incorrect_catalog_label(self):
        response = ApiResponse(check_availability_with_part_number(token=TestToken,
                                                                   part_number=self.part_number,
                                                                   catalog_label="INCORRECT",
                                                                   remove_char=self.remove_char))
        print(response)
        self.assertEqual(404, response.status_code)
