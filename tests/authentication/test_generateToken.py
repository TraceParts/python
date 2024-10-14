from unittest import TestCase

from src.authentication.generateToken import get_a_token
from src.utils.ApiResponse import ApiResponse


# documentation : https://developers.traceparts.com/v2/reference/post_v2-requesttoken


class Test(TestCase):
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.api_key: str = ""  # your api key
        self.tenant_uid: str = ""  # your tenant_uid

    def test_get_a_token(self):
        response = ApiResponse(get_a_token(tenant_uid=self.tenant_uid,
                                           api_key=self.api_key))
        print(response)
        self.assertEqual(200, response.status_code)

    def test_get_a_token_with_invalid_tenant_uid(self):
        response = ApiResponse(get_a_token(tenant_uid="incorrect_tenant_uid",
                                           api_key=self.api_key))
        print(response)
        self.assertEqual(400, response.status_code)

    def test_get_a_token_with_invalid_api_key(self):
        response = ApiResponse(get_a_token(tenant_uid=self.tenant_uid,
                                           api_key="incorrect_api_key"))
        print(response)
        self.assertEqual(401, response.status_code)
