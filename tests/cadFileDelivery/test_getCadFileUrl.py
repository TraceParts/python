from unittest import TestCase

from src.cadFileDelivery.getCadFileUrl import get_cad_file_url
from src.utils.ApiResponse import ApiResponse
from tests.utils.TestToken import TestToken


# documentation : https://developers.traceparts.com/v2/reference/get_v2-product-cadfileurl

class Test(TestCase):
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.cad_request_id: int = 0  # your cad request id

    def test_get_cad_file_url(self):
        response = ApiResponse(get_cad_file_url(token=TestToken,
                                                cad_request_id=self.cad_request_id))
        print(response)
        self.assertTrue((200 == response.status_code | 204 == response.status_code))

    def test_get_cad_file_url_with_incorrect_cad_request_id(self):
        response = ApiResponse(get_cad_file_url(token=TestToken,
                                                cad_request_id=-1))
        print(response)
        self.assertEqual(404, response.status_code)
