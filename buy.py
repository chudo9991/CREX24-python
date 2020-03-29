import datetime
import base64
import hmac
import json
from hashlib import sha512
from urllib.request import urlopen, Request
from urllib.error import HTTPError

def placeOrder(price):

    order = {
            "instrument": "CREX-BTC",
            "side": "buy",
            "volume": 0.0002,
            "price": price
        }

    baseUrl = "https://api.crex24.com"
    apiKey = "0515be61-853e-48ad-b6fa-424d768e2d6a"
    secret = "mCHnfAWVU+Q8V5yZQHaaAaaGIF+eIjn4joDQAFWIPUKPzsOFBbH18uWchNPOiPBL7L015YJDuLL3KYL9Lqb7RQ=="

    path = "/v2/trading/placeOrder"
    body = json.dumps(order, separators=(',', ':'))
    nonce = round(datetime.datetime.now().timestamp() * 1000)

    key = base64.b64decode(secret)
    message = str.encode(path + str(nonce) + body, "utf-8")
    hmac2 = hmac.new(key, message, sha512)
    signature = base64.b64encode(hmac2.digest()).decode()

    request = Request(baseUrl + path)
    request.method = "POST"
    request.data = str.encode(body, "utf-8")
    request.add_header("Content-Length", len(body))
    request.add_header("X-CREX24-API-KEY", apiKey)
    request.add_header("X-CREX24-API-NONCE", nonce)
    request.add_header("X-CREX24-API-SIGN", signature)

    try:
        response = urlopen(request)
    except HTTPError as e:
        response = e

    status = response.getcode()
    body = bytes.decode(response.read())

    # print("Status code: " + str(status))
    # print(body)

