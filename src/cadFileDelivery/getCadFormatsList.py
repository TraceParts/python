import argparse

import requests

from src.utils.ApiResponse import ApiResponse
from src.utils.myUrlFormater import my_url_formater
from src.utils.rootApiUrl import ROOT_API_URL


def get_possible_options():
    return {
        "partFamilyCode": str,
        "selectionPath": str,
        "classificationCode": str,
        "partNumber": str,
    }


# documentation : https://developers.traceparts.com/v2/reference/get_v3-product-caddataavailability

def get_cad_formats_list(token: str, optional_parameters: dict, culture_info: str):
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

    url = ROOT_API_URL + "v3/Product/CadDataAvailability?" + optional_parameters_string + "&cultureInfo=" + my_url_formater(
        culture_info)
    headers = {
        "accept": "application/json",
        "authorization": "Bearer " + token
    }
    return requests.get(url, headers=headers)


parser = argparse.ArgumentParser()
# Token
parser.add_argument("token", help="Token generated with the Tenant Unique ID and the API key")
# Required pairs (one of those pairs must be given)
pair1 = parser.add_argument_group(
    title="Pair 1 : partFamilyCode and selectionPath (without selectionPath, the default configuration is used)")
pair1.add_argument("--partFamilyCode", help="TraceParts code of the product family.")
pair1.add_argument("--selectionPath",
                   help="Selected configuration (it is used in combination with partFamilyCode if not provided part will be loaded with default configuration)")
pair2 = parser.add_argument_group(
    title="Pair 2 : classificationCode and partNumber (both parameters are required with this way)")
pair2.add_argument("--classificationCode",
                   help="TraceParts code of the classification (to use in combination with partNumber).")
pair2.add_argument("--partNumber",
                   help="Identifier of a product (to use in combination with classificationCode). Part number as stored in the TraceParts database.")
# Required
parser.add_argument("cultureInfo", help="Language for the labels of the CAD formats.")

if __name__ == '__main__':
    args = parser.parse_args()
    print(ApiResponse(get_cad_formats_list(args.token, args.__dict__, args.cultureInfo)))
