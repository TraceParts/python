import argparse

import requests

from src.utils.ApiResponse import ApiResponse
from src.utils.myUrlFormater import my_url_formater
from src.utils.rootApiUrl import ROOT_API_URL


# documentation : https://developers.traceparts.com/v2/reference/get_v2-search-catalog-availability

def check_availability_with_catalog(token: str, catalog_label: str):
    print("📘 Warning! Any tries will be recorded in the Production data.")
    url = ROOT_API_URL + "v2/Search/Catalog/Availability?catalog=" + my_url_formater(catalog_label)
    headers = {
        "accept": "application/json",
        "authorization": "Bearer " + token
    }
    return requests.get(url, headers=headers)


parser = argparse.ArgumentParser()
# Token
parser.add_argument("token", help="Token generated with the Tenant Unique ID and the API key")
# Required
parser.add_argument("catalog", help="Catalog label as you have in your own data.")

if __name__ == '__main__':
    args = parser.parse_args()
    print(ApiResponse(check_availability_with_catalog(args.token, args.catalog)))
