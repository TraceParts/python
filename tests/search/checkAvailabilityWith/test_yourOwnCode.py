from unittest import TestCase

from src.search.checkAvailabilityWith.yourOwnCode import check_availability_with_your_own_code
from src.utils.ApiResponse import ApiResponse
from tests.utils.TestToken import TestToken


# documentation : https://developers.traceparts.com/v2/reference/get_v2-search-yourowncode-availability

class Test(TestCase):
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.catalog_label: str = ""  # your catalog label
        self.your_own_code: str = ""  # your own code

    def test_check_availability_with_your_own_code(self):
        response = ApiResponse(check_availability_with_your_own_code(token=TestToken,
                                                                     your_own_code=self.your_own_code,
                                                                     catalog_label=self.catalog_label))
        print(response)
        self.assertEqual(200, response.status_code)

    def test_check_availability_with_your_own_code_with_empty_your_own_code(self):
        response = ApiResponse(check_availability_with_your_own_code(token=TestToken,
                                                                     your_own_code="",
                                                                     catalog_label=self.catalog_label))
        print(response)
        self.assertEqual(400, response.status_code)

    def test_check_availability_with_your_own_code_with_incorrect_your_own_code(self):
        response = ApiResponse(check_availability_with_your_own_code(token=TestToken,
                                                                     your_own_code="incorrect_your_own_code",
                                                                     catalog_label=self.catalog_label))
        print(response)
        self.assertEqual(404, response.status_code)

    def test_check_availability_with_your_own_code_with_empty_catalog_label(self):
        response = ApiResponse(check_availability_with_your_own_code(token=TestToken,
                                                                     your_own_code=self.your_own_code,
                                                                     catalog_label=""))
        print(response)
        self.assertEqual(400, response.status_code)

    def test_check_availability_with_your_own_code_with_incorrect_catalog_label(self):
        response = ApiResponse(check_availability_with_your_own_code(token=TestToken,
                                                                     your_own_code=self.your_own_code,
                                                                     catalog_label="INCORRECT"))
        print(response)
        self.assertEqual(404, response.status_code)
