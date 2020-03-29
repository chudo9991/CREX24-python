import ast
import datetime
import base64
import hmac
from hashlib import sha512
from urllib.request import urlopen, Request
from urllib.error import HTTPError
import json

def checkExistingOrders():
    baseUrl = "https://api.crex24.com"
    apiKey = "0515be61-853e-48ad-b6fa-424d768e2d6a"
    secret = "mCHnfAWVU+Q8V5yZQHaaAaaGIF+eIjn4joDQAFWIPUKPzsOFBbH18uWchNPOiPBL7L015YJDuLL3KYL9Lqb7RQ=="
    path = "/v2/trading/activeOrders"  # ETH-BTC,BTC-ETH,CREX-BTC,BTC-ETH"
    nonce = round(datetime.datetime.now().timestamp() * 1000)

    key = base64.b64decode(secret)
    message = str.encode(path + str(nonce), "utf-8")
    hmac3 = hmac.new(key, message, sha512)
    signature = base64.b64encode(hmac3.digest()).decode()

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

    arr = json.loads(body)
    # print("ТВОИ ОРДЕРА:")
    # print(arr)
    # print(type(arr))

    data = 0
    for key in arr:  # key это dict
        for i in key:
            if i == "id":
                data = key[i]

    return data

def cancelExistingOrders():
    baseUrl = "https://api.crex24.com"
    apiKey = "0515be61-853e-48ad-b6fa-424d768e2d6a"
    secret = "mCHnfAWVU+Q8V5yZQHaaAaaGIF+eIjn4joDQAFWIPUKPzsOFBbH18uWchNPOiPBL7L015YJDuLL3KYL9Lqb7RQ=="
    path = "/v2/trading/cancelAllOrders"
    nonce = round(datetime.datetime.now().timestamp() * 1000)

    key = base64.b64decode(secret)
    message = str.encode(path + str(nonce), "utf-8")
    hmac3 = hmac.new(key, message, sha512)
    signature = base64.b64encode(hmac3.digest()).decode()

    request = Request(baseUrl + path)
    request.method = "POST"
    request.add_header("X-CREX24-API-KEY", apiKey)
    request.add_header("X-CREX24-API-NONCE", nonce)
    request.add_header("X-CREX24-API-SIGN", signature)
    try:
        response = urlopen(request)
    except HTTPError as e:
        response = e

    status = response.getcode()
    body = bytes.decode(response.read())

    #arr2 = ast.literal_eval(body)
    print("ОТМЕНЕНЫ ОРДЕРА:")
    print(body)

def getExistingOrders():
    baseUrl = "https://api.crex24.com"
    apiKey = "0515be61-853e-48ad-b6fa-424d768e2d6a"
    secret = "mCHnfAWVU+Q8V5yZQHaaAaaGIF+eIjn4joDQAFWIPUKPzsOFBbH18uWchNPOiPBL7L015YJDuLL3KYL9Lqb7RQ=="
    path = "/v2/trading/activeOrders?instrument=CREX-BTC"
    nonce = round(datetime.datetime.now().timestamp() * 1000)

    key = base64.b64decode(secret)
    message = str.encode(path + str(nonce), "utf-8")
    hmac3 = hmac.new(key, message, sha512)
    signature = base64.b64encode(hmac3.digest()).decode()

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

    #arr = ast.literal_eval(body)
    arr=json.loads(body)
    # print("ТВОИ ОРДЕРА:")
    # print(arr)
    # print(type(arr))

    data = 0
    for key in arr:  # key это dict
        for i in key:
            if i == "id":
                data=key[i]

    return data

# cancelExistingOrders()
# print(getExistingOrders())