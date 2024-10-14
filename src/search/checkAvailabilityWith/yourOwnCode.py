import argparse

import requests

from src.utils.ApiResponse import ApiResponse
from src.utils.myUrlFormater import my_url_formater
from src.utils.rootApiUrl import ROOT_API_URL


# documentation : https://developers.traceparts.com/v2/reference/get_v2-search-yourowncode-availability

def check_availability_with_your_own_code(token: str, your_own_code: str, catalog_label: str):
    print("📘 Warning! Any tries will be recorded in the Production data.")
    url = ROOT_API_URL + "v2/Search/YourOwnCode/Availability?yourOwnCode=" + my_url_formater(
        your_own_code) + "&catalog=" + my_url_formater(catalog_label)
    headers = {
        "accept": "application/json",
        "authorization": "Bearer " + token
    }
    return requests.get(url, headers=headers)


parser = argparse.ArgumentParser()
# Token
parser.add_argument("token", help="Token generated with the Tenant Unique ID and the API key")
# Required
parser.add_argument("yourOwnCode",
                    help="Non public string to call a configuration in the TraceParts database (i.e.: SKU, internal_code, Part_ID).")
parser.add_argument("catalog", help="Catalog label as you have in your own data.")

if __name__ == '__main__':
    args = parser.parse_args()
    print(ApiResponse(check_availability_with_your_own_code(args.token, args.yourOwnCode, args.catalog)))
