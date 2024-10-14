from unittest import TestCase

from src.product.productData import product_data
from src.utils.ApiResponse import ApiResponse
from tests.utils.TestToken import TestToken


# documentation : https://developers.traceparts.com/v2/reference/get_v3-product-configure

class Test(TestCase):
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.optional_parameters: dict = {
            "selectionPath": "",  # your selection path
            "cadDetailLevel": "",  # your cad detail level
            "currentStepNumber": -1,  # [DEPRECATED] your current step number
        }
        self.culture_info: str = ""  # your culture info
        self.part_family_code: str = ""  # your part family code

    def test_product_data(self):
        response = ApiResponse(
            product_data(token=TestToken,
                         part_family_code=self.part_family_code,
                         culture_info=self.culture_info,
                         optional_parameters=self.optional_parameters))
        print(response)
        self.assertEqual(200, response.status_code)

    def test_product_data_with_empty_parameters(self):
        # both parameters react the same when thy are empty
        response = ApiResponse(
            product_data(token=TestToken,
                         part_family_code="",
                         culture_info="",
                         optional_parameters=self.optional_parameters))
        print(response)
        self.assertEqual(400, response.status_code)
