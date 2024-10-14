import argparse

import requests

from src.utils.ApiResponse import ApiResponse
from src.utils.rootApiUrl import ROOT_API_URL


# documentation : https://developers.traceparts.com/v2/reference/get_v2-supportedlanguages

def get_languages_list(token: str):
    print("📘 Warning! Any tries will be recorded in the Production data.")
    url = ROOT_API_URL + "v2/SupportedLanguages"
    headers = {
        "accept": "application/json",
        "authorization": "Bearer " + token
    }
    return requests.get(url, headers=headers)


parser = argparse.ArgumentParser()
# Token
parser.add_argument("token", help="Token generated with the Tenant Unique ID and the API key")

if __name__ == '__main__':
    args = parser.parse_args()
    print(ApiResponse(get_languages_list(args.token)))
