import ast
import datetime
import base64
import hmac
from hashlib import sha512
from urllib.request import urlopen, Request
from urllib.error import HTTPError

def checkAmountOnWallet():
    baseUrl = "https://api.crex24.com"
    apiKey = "0515be61-853e-48ad-b6fa-424d768e2d6a"
    secret = "mCHnfAWVU+Q8V5yZQHaaAaaGIF+eIjn4joDQAFWIPUKPzsOFBbH18uWchNPOiPBL7L015YJDuLL3KYL9Lqb7RQ=="

    path = "/v2/account/balance?currency=BTC&nonZeroOnly=True"
    nonce = round(datetime.datetime.now().timestamp() * 1000)

    key = base64.b64decode(secret)
    message = str.encode(path + str(nonce), "utf-8")
    hmac2 = hmac.new(key, message, sha512)
    signature = base64.b64encode(hmac2.digest()).decode()

    request = Request(baseUrl + path)
    request.method = "GET"
    request.add_header("X-CREX24-API-KEY", apiKey)
    request.add_header("X-CREX24-API-NONCE", nonce)
    request.add_header("X-CREX24-API-SIGN", signature)

    try:
        response = urlopen(request)
    except HTTPError as e:
        response = e

    status = response.getcode()
    body = bytes.decode(response.read())

    arr = ast.literal_eval(body)
    data = 0
    for A in arr:  # key это dict
        for key in A:
            if key=="available":
                data=A[key]

    return data

def checkAmountOnWalletCREX():
    baseUrl = "https://api.crex24.com"
    apiKey = "0515be61-853e-48ad-b6fa-424d768e2d6a"
    secret = "mCHnfAWVU+Q8V5yZQHaaAaaGIF+eIjn4joDQAFWIPUKPzsOFBbH18uWchNPOiPBL7L015YJDuLL3KYL9Lqb7RQ=="

    path = "/v2/account/balance?currency=CREX&nonZeroOnly=True"
    nonce = round(datetime.datetime.now().timestamp() * 1000)

    key = base64.b64decode(secret)
    message = str.encode(path + str(nonce), "utf-8")
    hmac2 = hmac.new(key, message, sha512)
    signature = base64.b64encode(hmac2.digest()).decode()

    request = Request(baseUrl + path)
    request.method = "GET"
    request.add_header("X-CREX24-API-KEY", apiKey)
    request.add_header("X-CREX24-API-NONCE", nonce)
    request.add_header("X-CREX24-API-SIGN", signature)

    try:
        response = urlopen(request)
    except HTTPError as e:
        response = e

    status = response.getcode()
    body = bytes.decode(response.read())

    arr = ast.literal_eval(body)
    data = 0
    for A in arr:  # key это dict
        for key in A:
            if key=="available":
                data=A[key]

    return data