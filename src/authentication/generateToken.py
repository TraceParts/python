import argparse

import requests

from src.utils.ApiResponse import ApiResponse
from src.utils.rootApiUrl import ROOT_API_URL


# documentation : https://developers.traceparts.com/v2/reference/post_v2-requesttoken

def get_a_token(tenant_uid: str, api_key: str):
    print("📘 Warning! Any tries will be recorded in the Production data.")
    url = ROOT_API_URL + "v2/RequestToken"

    payload = {"tenantUid": tenant_uid, "apiKey": api_key}

    headers = {
        "accept": "application/json",
        "content-type": "application/*+json"
    }
    return requests.post(url, json=payload, headers=headers)


parser = argparse.ArgumentParser()
# Required
parser.add_argument("tenantUid", help="Tenant Unique ID provided in the email giving you access to our API")
parser.add_argument("apiKey", help="API key provided in the email giving you access to our API")

if __name__ == '__main__':
    args = parser.parse_args()
    print(ApiResponse(get_a_token(args.tenantUid, args.apiKey)))
