import argparse

import requests

from src.utils.ApiResponse import ApiResponse
from src.utils.myUrlFormater import my_url_formater
from src.utils.rootApiUrl import ROOT_API_URL


# documentation : https://developers.traceparts.com/v2/reference/get_v2-search-productlist

def list_of_products(token: str, culture_info: str, classification_code: str, category_code: str, ):
    print("📘 Warning! Any tries will be recorded in the Production data.")

    # As category_code is optional, if it is None it is just ignored
    category_code_string = "&categoryCode=" + my_url_formater(category_code) if category_code is not None else ""

    url = ROOT_API_URL + "v2/Search/ProductList?cultureInfo=" + culture_info + "&classificationCode=" + my_url_formater(
        classification_code) + category_code_string
    headers = {
        "accept": "application/json",
        "authorization": "Bearer " + token
    }
    return requests.get(url, headers=headers)


parser = argparse.ArgumentParser()
# Token
parser.add_argument("token", help="Token generated with the Tenant Unique ID and the API key")
# Required
parser.add_argument("cultureInfo", help="Language of the labels.")
parser.add_argument("classificationCode",
                    help="TraceParts code of the classification (to use in combination with partNumber).")
# Optional
parser.add_argument("--categoryCode", help="Unique category code in the related classification.")

if __name__ == '__main__':
    args = parser.parse_args()
    print(ApiResponse(
        list_of_products(args.token, args.cultureInfo, args.classificationCode, args.categoryCode)))
