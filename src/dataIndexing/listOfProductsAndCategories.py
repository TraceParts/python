import argparse

import requests

from src.utils.ApiResponse import ApiResponse
from src.utils.myUrlFormater import my_url_formater
from src.utils.rootApiUrl import ROOT_API_URL


# documentation : https://developers.traceparts.com/v2/reference/get_v2-search-productandcategorylist

def list_of_products_and_categories(token: str, classification_code: str, part_family_code: str, ):
    print("📘 Warning! Any tries will be recorded in the Production data.")

    # As part_family_code is optional, if it is None it is just ignored
    part_family_code_string = "&partFamilyCode=" + my_url_formater(
        part_family_code) if part_family_code is not None else ""

    url = ROOT_API_URL + "v2/Search/ProductAndCategoryList?classificationCode=" + my_url_formater(
        classification_code) + part_family_code_string
    headers = {
        "accept": "application/json",
        "authorization": "Bearer " + token
    }
    return requests.get(url, headers=headers)


parser = argparse.ArgumentParser()
# Token
parser.add_argument("token", help="Token generated with the Tenant Unique ID and the API key")
# Required
parser.add_argument("classificationCode",
                    help="TraceParts code of the classification (to use in combination with partNumber).")
# Optional
parser.add_argument("--partFamilyCode", help="TraceParts code of the product family.")

if __name__ == '__main__':
    args = parser.parse_args()
    print(ApiResponse(list_of_products_and_categories(args.token, args.classificationCode, args.partFamilyCode)))
