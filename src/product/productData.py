import argparse

import requests

from src.utils.ApiResponse import ApiResponse
from src.utils.myUrlFormater import my_url_formater
from src.utils.rootApiUrl import ROOT_API_URL


def get_possible_options():
    return {
        "selectionPath": str,
        "cadDetailLevel": str,
        "currentStepNumber": int,
    }


# documentation : https://developers.traceparts.com/v2/reference/get_v3-product-configure

def product_data(token: str, part_family_code: str, culture_info: str, optional_parameters: dict):
    print("📘 Warning! Any tries will be recorded in the Production data.")
    optional_parameters_string = ""
    # Gathering all possible options
    possible_options = get_possible_options()
    for parameter_key in optional_parameters.keys():
        # Checking for each option if the value is usable (not None)
        if parameter_key in possible_options and optional_parameters[parameter_key] is not None:
            # Format all usable options and adding them ones after others
            optional_parameters_string += "&{0}={1}".format(parameter_key,
                                                            my_url_formater(
                                                                str(optional_parameters[parameter_key])))

    url = ROOT_API_URL + "v3/Product/Configure?partFamilyCode=" + my_url_formater(
        part_family_code) + "&cultureInfo=" + my_url_formater(culture_info) + optional_parameters_string
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
parser.add_argument("cultureInfo", help="Language of the texts.")
# Optional
parser.add_argument("--selectionPath",
                    help="Selected configuration (to use in combination with partFamilyCode. If not provided, the product is loaded with default configuration).")
parser.add_argument("--cadDetailLevel", help="Integer related to the level of detail included in the CAD model.")
# Deprecated
parser.add_argument("--currentStepNumber", help="[DEPRECATED] Current step of configuration.")

if __name__ == '__main__':
    args = parser.parse_args()
    print(ApiResponse(product_data(args.token, args.partFamilyCode, args.cultureInfo, args.__dict__)))
