import argparse

import requests

from src.utils.ApiResponse import ApiResponse
from src.utils.myUrlFormater import my_url_formater
from src.utils.rootApiUrl import ROOT_API_URL


# documentation : https://developers.traceparts.com/v2/reference/get_v1-search-partnumberlist

def list_of_part_numbers(token: str, part_family_code: str, return_your_own_codes: bool):
    print("📘 Warning! Any tries will be recorded in the Production data.")

    # As the default value is false, if return_your_own_codes is false it is just ignored
    return_your_own_codes_string = "&returnYourOwnCodes=true" if return_your_own_codes else ""

    url = ROOT_API_URL + "v1/Search/PartNumberList?&partFamilyCode=" + my_url_formater(
        part_family_code) + return_your_own_codes_string
    headers = {
        "accept": "application/json",
        "authorization": "Bearer " + token
    }
    return requests.get(url, headers=headers)


parser = argparse.ArgumentParser()
# Token
parser.add_argument("token", help="Token generated with the Tenant Unique ID and the API key")
# Required
parser.add_argument("partFamilyCode", help="TraceParts code of the product family.")
# Optional
parser.add_argument("--returnYourOwnCodes", action="store_true",
                    help="If available, your own codes (i.e.: SKU, internal_code, Part_ID) are returned.")

if __name__ == '__main__':
    args = parser.parse_args()
    print(ApiResponse(list_of_part_numbers(args.token, args.partFamilyCode, args.returnYourOwnCodes)))
