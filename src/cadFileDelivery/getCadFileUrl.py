import argparse
from time import sleep

import requests

from src.utils.ApiResponse import ApiResponse
from src.utils.rootApiUrl import ROOT_API_URL


# documentation : https://developers.traceparts.com/v2/reference/get_v2-product-cadfileurl

def get_cad_file_url(token: str, cad_request_id: int):
    print("📘 Warning! Any tries will be recorded in the Production data.")
    url = ROOT_API_URL + "v2/Product/cadFileUrl?cadRequestId=" + str(cad_request_id)
    headers = {
        "accept": "application/json",
        "authorization": "Bearer " + token
    }
    return requests.get(url, headers=headers)


def loop_get_cad_file_url_request(token: str, cad_request_id: int):
    print("📘 Warning! Any tries will be recorded in the Production data.")
    timeout = 10  # in minutes
    interval = 2  # in seconds

    result_message = "Timeout reached (" + str(timeout) + " minutes with " + str(
        interval) + " seconds interval). Your model couldn't be generated."
    last_response = None

    nbr_of_iterations = int(timeout * 60 / interval)
    for i in range(nbr_of_iterations):
        print("Request " + str(i + 1) + "/" + str(nbr_of_iterations))
        last_response = ApiResponse(get_cad_file_url(token, cad_request_id))
        # status code 204 means wait
        if last_response.status_code == 204:
            sleep(interval)
        else:
            if 200 <= last_response.status_code <= 299:
                result_message = "Success, results arrived !"
            else:
                result_message = "An error occurred. Please refer to the status code to know what append."

            break

    print(result_message)
    return last_response


parser = argparse.ArgumentParser()
# Token
parser.add_argument("token", help="Token generated with the Tenant Unique ID and the API key")
# Required
parser.add_argument("cadRequestId", type=int, help="ID of the request provided by the cadRequest end point")
# Optional
parser.add_argument("-l", "--loopRequest", action="store_true",
                    help="Loop request until there is a definitive answer (can take a while)")

if __name__ == '__main__':
    args = parser.parse_args()
    if args.loopRequest:
        print(loop_get_cad_file_url_request(args.token, args.cadRequestId))
    else:
        response = ApiResponse(get_cad_file_url(args.token, args.cadRequestId))
        if response.status_code == 204:
            print("Status code 204 means the file is generating. "
                  "You must repeat this request periodically to see if the file ends its generation. "
                  "If you want, you can add the option '-l' or '--loopRequest' to repeat automatically the request and "
                  "get a definitive answer.")
        print(response)
