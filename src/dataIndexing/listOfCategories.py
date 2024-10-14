import argparse

import requests

from src.utils.ApiResponse import ApiResponse
from src.utils.myUrlFormater import my_url_formater
from src.utils.rootApiUrl import ROOT_API_URL


# documentation : https://developers.traceparts.com/v2/reference/get_v2-search-categorylist

def list_of_categories(token: str, classification_code: str, culture_info: str, ):
    print("📘 Warning! Any tries will be recorded in the Production data.")
    url = ROOT_API_URL + "v2/Search/CategoryList?classificationCode=" + my_url_formater(
        classification_code) + "&cultureInfo=" + my_url_formater(culture_info)
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
parser.add_argument("cultureInfo", help="Language of the labels.")

if __name__ == '__main__':
    args = parser.parse_args()
    print(ApiResponse(list_of_categories(args.token, args.classificationCode, args.cultureInfo)))
