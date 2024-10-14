from unittest import TestCase

from src.product.productConfiguration import product_configuration
from src.utils.ApiResponse import ApiResponse
from tests.utils.TestToken import TestToken


# documentation : https://developers.traceparts.com/v2/reference/post_v3-product-updateconfiguration
# 📘 Warning! Any tries will be recorded in the Production data.

class Test(TestCase):
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.optional_parameters: dict = {
            "cadDetailLevel": "",  # your cad detail level
            "currentStepNumber": -1,  # [DEPRECATED] your current step number
        }
        self.value: str = ""  # your value
        self.symbol: str = ""  # your symbol
        self.initial_selection_path: str = ""  # your initial selection path
        self.culture_info: str = ""  # culture info
        self.part_family_code: str = ""  # part family code

    def test_product_configuration(self):
        response = ApiResponse(product_configuration(token=TestToken,
                                                     part_family_code=self.part_family_code,
                                                     culture_info=self.culture_info,
                                                     initial_selection_path=self.initial_selection_path,
                                                     symbol=self.symbol,
                                                     value=self.value,
                                                     optional_parameters=self.optional_parameters))
        print(response)
        self.assertEqual(200, response.status_code)

    def test_product_configuration_with_empty_parameters(self):
        # all parameters react the same way to an empty value
        response = ApiResponse(product_configuration(token=TestToken,
                                                     part_family_code="",
                                                     culture_info="",
                                                     initial_selection_path="",
                                                     symbol="",
                                                     value="",
                                                     optional_parameters=self.optional_parameters))
        print(response)
        self.assertEqual(400, response.status_code)

    def test_product_configuration_with_incorrect_part_family_code(self):
        response = ApiResponse(product_configuration(token=TestToken,
                                                     part_family_code="00-00000000-000000",
                                                     culture_info=self.culture_info,
                                                     initial_selection_path=self.initial_selection_path,
                                                     symbol=self.symbol,
                                                     value=self.value,
                                                     optional_parameters=self.optional_parameters))
        print(response)
        self.assertEqual(404, response.status_code)

    def test_product_configuration_with_incorrect_symbol(self):
        response = ApiResponse(product_configuration(token=TestToken,
                                                     part_family_code=self.part_family_code,
                                                     culture_info=self.culture_info,
                                                     initial_selection_path=self.initial_selection_path,
                                                     symbol="incorrectSymbol",
                                                     value="incorrectValue",
                                                     optional_parameters=self.optional_parameters))
        print(response)
        #  status code 200 but comport an error message in the returned JSON
        self.assertEqual(200, response.status_code)
        # check if the JSON have the associated error message
        # bellow JSON path should lead to a "Parameter with symbol "incorrectSymbol" not found!" message
        self.assertIs(True, bool(response.body["globalInfo"]["configurationErrors"]))
