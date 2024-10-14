import argparse

import requests

from src.utils.ApiResponse import ApiResponse
from src.utils.myUrlFormater import my_url_formater
from src.utils.rootApiUrl import ROOT_API_URL


# documentation : https://developers.traceparts.com/v2/reference/get_v2-account-checklogin-useremail

def check_the_existence_of_a_user_account(token: str, user_email: str):
    print("📘 Warning! Any tries will be recorded in the Production data.")
    url = ROOT_API_URL + "v2/Account/CheckLogin/" + my_url_formater(user_email)
    headers = {
        "accept": "application/json",
        "authorization": "Bearer " + token
    }
    return requests.get(url, headers=headers)


parser = argparse.ArgumentParser()
# Token
parser.add_argument("token", help="Token generated with the Tenant Unique ID and the API key")
# Required
parser.add_argument("userEmail", help="Email address linked to the account.")

if __name__ == '__main__':
    args = parser.parse_args()
    response = ApiResponse(check_the_existence_of_a_user_account(args.token, args.userEmail))
    if response.status_code == 200:
        print(args.userEmail + " exist !")
    else:
        print(args.userEmail + " DO NOT exist")
    print(response)
