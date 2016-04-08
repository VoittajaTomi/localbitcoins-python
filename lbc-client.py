import hmac
import requests
import hashlib
import time
import sys
import json

import settings


def print_response(response):
    if response:
        print(json.dumps(response.json()['data'], sort_keys=True, indent=4, separators=(',', ': ')))
    else:
        print(response.text)


def make_api_call(method, url, params={}, stream=False):
    hmac_key = settings.HMAC_KEY
    hmac_secret = settings.HMAC_SECRET
    lbc_url = settings.LBC_URL

    # Convert parameters into ordered form
    params = params.items()

    nonce = long(time.time() * 1000)

    params_urlencoded = requests.models.RequestEncodingMixin._encode_params(params)
    message = str(nonce) + hmac_key + url + params_urlencoded
    signature = hmac.new(str(hmac_secret), msg=message, digestmod=hashlib.sha256).hexdigest().upper()

    headers = {
        "Apiauth-Key": hmac_key,
        "Apiauth-Nonce": str(nonce),
        "Apiauth-Signature": signature
    }


    if method == 'GET':
        return requests.get(lbc_url + url, params=params, headers=headers, stream=stream)
    elif method == 'POST':
        return requests.post(lbc_url + url, data=params, headers=headers, stream=stream)
    else:
        raise Exception('Invalid method ' + method + '!')

def got_args(count):
    return len(sys.argv)>count+1

def error(msg):
    print("Error: " + msg)


def process_arguments(arguments):
    if arguments[1] == "account_info":
        if got_args(1):
            print_response(make_api_call("GET","/api/account_info/"+arguments[2]+"/"))
        else:
            error("No username specified")

    elif arguments[1] == "myself":
        print_response(make_api_call("GET","/api/myself/"))

    elif arguments[1]=="dashboard":
        print_response(make_api_call("GET","/api/dashboard/"))

    elif arguments[1]=="dashboard/released":
        print_response(make_api_call("GET","/api/dashboard/released/"))

    elif arguments[1]=="dashboard/canceled":
        print_response(make_api_call("GET","/api/dashboard/canceled/"))

    elif arguments[1]=="contact_messages":
        print_response(make_api_call("GET","/api/contact_messages/"+arguments[2]+"/"))

    elif arguments[1]=="contact_info":
        print_response(make_api_call("GET","/api/contact_info/", params={ "contacts" : arguments[2] if got_args(1) else None}))

    elif arguments[1]=="recent_messages":
        print_response(make_api_call("GET","/api/recent_messages/",params={ "before" : arguments[2] if got_args(1) else None}))

    elif arguments[1]=="wallet":
        print_response(make_api_call("GET", "/api/wallet/"))

    elif arguments[1]=="wallet-balance":
        print_response(make_api_call("GET", "/api/wallet-balance/"))

    elif arguments[1]=="wallet-send":
        if(got_args(2)):
            print_response(make_api_call("POST","/api/wallet-send/", params={"address" : arguments[2], "amount" : arguments[3]}))
        else:
            error("This command requires two arguments")

    else:
        error("Invalid argument " + arguments[1])

process_arguments(sys.argv)
