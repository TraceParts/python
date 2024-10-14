import argparse

import requests

from src.utils.ApiResponse import ApiResponse
from src.utils.myUrlFormater import my_url_formater
from src.utils.rootApiUrl import ROOT_API_URL


def get_possible_options():
    return {
        "cadDetailLevel": str,
        "currentStepNumber": int,
    }


# documentation : https://developers.traceparts.com/v2/reference/post_v3-product-updateconfiguration
# 📘 Warning! Any tries will be recorded in the Production data.

def product_configuration(token: str, part_family_code: str, culture_info: str, initial_selection_path: str,
                          symbol: str,
                          value: str, optional_parameters: dict):
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

    url = ROOT_API_URL + "v3/Product/UpdateConfiguration?partFamilyCode=" + my_url_formater(
        part_family_code) + "&cultureInfo=" + my_url_formater(
        culture_info) + "&initialSelectionPath=" + my_url_formater(
        initial_selection_path) + "&symbol=" + my_url_formater(symbol) + "&value=" + my_url_formater(value)
    headers = {
        "accept": "application/json",
        "authorization": "Bearer " + token
    }
    return requests.post(url, headers=headers)


parser = argparse.ArgumentParser()
# Token
parser.add_argument("token", help="Token generated with the Tenant Unique ID and the API key")
# Required
parser.add_argument("partFamilyCode", help="TraceParts code of the product family.")
parser.add_argument("cultureInfo", help="Language of the texts.")

parser.add_argument("initialSelectionPath", help="Current SelectionPath from partFamilyInfo.")
parser.add_argument("symbol", help="Parameter code to update.")
parser.add_argument("value",
                    help="New value to set for the related symbol. When the parameter 'editable' is set to 'true', the value must start with =")
# Optional
parser.add_argument("--cadDetailLevel", help="Integer related to the level of detail included in the CAD model.")
# Deprecated
parser.add_argument("--currentStepNumber", type=int, help="[DEPRECATED] Current step of configuration.")

if __name__ == '__main__':
    args = parser.parse_args()
    print(ApiResponse(
        product_configuration(args.token, args.partFamilyCode, args.cultureInfo, args.initialSelectionPath, args.symbol,
                              args.value, args.__dict__)))
