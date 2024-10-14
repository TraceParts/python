import json
from typing import Any

import requests
from requests import Response


class ApiResponse:
    def __init__(self, response: Response):
        self.status_code: int = response.status_code
        try:
            self.body: Any = response.json()
        except requests.exceptions.JSONDecodeError:
            # This prevents errors linked to an empty body
            self.body: Any = None

    def __str__(self):
        return json.dumps({
            "status_code": str(self.status_code),
            "body": self.body
        }, indent=4)
