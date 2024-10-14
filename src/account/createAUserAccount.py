import argparse

import requests

from src.utils.ApiResponse import ApiResponse
from src.utils.rootApiUrl import ROOT_API_URL


def get_possible_options():
    return {
        "company": str,
        "country": str,
        "name": str,
        "fname": str,
        "addr1": str,
        "addr2": str,
        "addr3": str,
        "city": str,
        "state": str,
        "zipCode": str,
        "phone": str,
        "fax": str,
        "tpOptIn": bool,
        "partnersOptIn": bool
    }


# documentation : https://developers.traceparts.com/v2/reference/post_v2-account-signup
# 📘 Warning! Any tries will be recorded in the Production data.

def create_a_user_account(token: str, user_email: str, optional_parameters: dict):
    print("📘 Warning! Any tries will be recorded in the Production data.")
    url = ROOT_API_URL + "v2/Account/SignUp"

    payload = {}
    # Gathering all possible options
    possible_options = get_possible_options()
    for parameter_key in optional_parameters.keys():
        # Checking for each option if the value is usable (not None)
        if parameter_key in possible_options and optional_parameters[parameter_key] is not None:
            payload[parameter_key] = optional_parameters[parameter_key]
    payload["userEmail"] = user_email

    headers = {
        "accept": "application/json",
        "content-type": "application/*+json",
        "authorization": "Bearer " + token
    }

    # The dictionary is serialized in a JSON object in the function
    return requests.post(url, json=payload, headers=headers)


parser = argparse.ArgumentParser()
# Token
parser.add_argument("token", help="Token generated with the Tenant Unique ID and the API key")
# Required
parser.add_argument("userEmail", help="Email address linked to the account.")
# Optional
parser.add_argument("--company", help="User company.")
parser.add_argument("--country", help="User country. ISO 3166-2 characters.")
parser.add_argument("--name", help="User last name.")
parser.add_argument("--fname", help="User first name.")
parser.add_argument("--addr1", help="First field for the user address.")
parser.add_argument("--addr2", help="Second field for the user address.")
parser.add_argument("--addr3", help="Third field for the user address.")
parser.add_argument("--city", help="User city.")
parser.add_argument("--state", help="User state, for North America.")
parser.add_argument("--zipCode", help="User ZIP code.")
parser.add_argument("--phone", help="User phone number.")
parser.add_argument("--fax", help="User FAX number.")
parser.add_argument("--tpOptIn", action="store_true",
                    help="Consent to receive information sent by TraceParts by email about TraceParts services.")
parser.add_argument("--partnersOptIn", action="store_true",
                    help="Consent to receive information sent by TraceParts by email about TraceParts’ partners’ services.")

if __name__ == '__main__':
    args = parser.parse_args()
    response = ApiResponse(create_a_user_account(args.token, args.userEmail, args.__dict__))
    if response.status_code == 201:
        print(args.userEmail + " user created !")
    else:
        print(args.userEmail + " ERROR in the creation")
    print(response)
