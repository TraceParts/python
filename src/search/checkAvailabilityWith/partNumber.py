import argparse

import requests

from src.utils.ApiResponse import ApiResponse
from src.utils.myUrlFormater import my_url_formater
from src.utils.rootApiUrl import ROOT_API_URL


# documentation : https://developers.traceparts.com/v2/reference/get_v2-search-partnumber-availability

def check_availability_with_part_number(token: str, part_number: str, catalog_label: str, remove_char: bool):
    print("📘 Warning! Any tries will be recorded in the Production data.")

    # As the default value is false, if remove_char is false it is just ignored
    remove_char_string = "&removeChar=true" if remove_char else ""

    url = ROOT_API_URL + "v2/Search/PartNumber/Availability?partNumber=" + my_url_formater(
        part_number) + "&catalog=" + my_url_formater(catalog_label) + remove_char_string
    headers = {
        "accept": "application/json",
        "authorization": "Bearer " + token
    }
    return requests.get(url, headers=headers)


parser = argparse.ArgumentParser()
# Token
parser.add_argument("token", help="Token generated with the Tenant Unique ID and the API key")
# Required
parser.add_argument("partNumber", help="Part Number as you have in your own data.")
parser.add_argument("catalog", help="Catalog label as you have in your own data.")
# Optional
parser.add_argument("--removeChar", action="store_true",
                    help="The following characters are not evaluating (' ', '.', '-', '/', '+').")

if __name__ == '__main__':
    args = parser.parse_args()
    print(ApiResponse(check_availability_with_part_number(args.token, args.partNumber, args.catalog, args.removeChar)))
