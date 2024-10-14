import argparse

import requests

from src.utils.ApiResponse import ApiResponse
from src.utils.myUrlFormater import my_url_formater
from src.utils.rootApiUrl import ROOT_API_URL


# documentation : https://developers.traceparts.com/v2/reference/get_v1-contact-catalog

def catalog_contact_details(token: str, classification_code: str, ):
    print("📘 Warning! Any tries will be recorded in the Production data.")
    url = ROOT_API_URL + "v1/Contact/Catalog?classificationCode=" + my_url_formater(
        classification_code)
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

if __name__ == '__main__':
    args = parser.parse_args()
    print(ApiResponse(catalog_contact_details(args.token, args.classificationCode)))
