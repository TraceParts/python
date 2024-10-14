import argparse

import requests

from src.utils.ApiResponse import ApiResponse
from src.utils.rootApiUrl import ROOT_API_URL


def get_possible_options():
    return {
        "partFamilyCode": str,
        "selectionPath": str,
        "classificationCode": str,
        "partNumber": str,

        "cadDetailLevelId": str,

        "languageId": str
    }


# documentation : https://developers.traceparts.com/v2/reference/post_v3-product-cadrequest
# 📘 Warning! Any tries will be recorded in the Production data.

def request_a_cad_file(token: str, user_email: str, culture_info: str, cad_format_id: int, optional_parameters: dict):
    print("📘 Warning! Any tries will be recorded in the Production data.")
    url = ROOT_API_URL + "v3/Product/cadRequest"

    payload = {}
    possible_options = get_possible_options()
    for parameter_key in optional_parameters.keys():
        if parameter_key in possible_options and optional_parameters[parameter_key] is not None:
            payload[parameter_key] = optional_parameters[parameter_key]
    payload["userEmail"] = user_email
    payload["cultureInfo"] = culture_info
    payload["cadFormatId"] = cad_format_id

    headers = {
        "accept": "application/json",
        "content-type": "application/*+json",
        "authorization": "Bearer " + token
    }
    return requests.post(url, json=payload, headers=headers)


parser = argparse.ArgumentParser()
# Token
parser.add_argument("token", help="Token generated with the Tenant Unique ID and the API key")
# Required
parser.add_argument("userEmail", help="Email address associated to the CAD request event.")
parser.add_argument("cultureInfo", help="Language for the labels of the CAD formats.")
parser.add_argument("cadFormatId", type=int, help="TraceParts ID of the CAD format.")
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
# Optional
parser.add_argument("--cadDetailLevel",
                    help="Integer related to the level of detail included in the CAD model.")
# Deprecated
parser.add_argument("--languageId",
                    help="[DEPRECATED] TraceParts ID of the language (obsolete - please use cultureInfo).")

if __name__ == '__main__':
    args = parser.parse_args()
    response = ApiResponse(
        request_a_cad_file(args.token, args.userEmail, args.cultureInfo, args.cadFormatId, args.__dict__))
    if response.status_code == 200:
        print(
            "CAD file request succeed ! You will be given an ID in the response bellow. "
            "You will use it to get the CAD file URL so don't forget it.")
    else:
        print("CAD file request failed.")
    print(response)
