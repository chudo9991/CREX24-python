# coding=utf-8

import ccxt

# crex24   = ccxt.CREX24({
#         'apiKey': '0515be61-853e-48ad-b6fa-424d768e2d6a',
#         'secret': 'mCHnfAWVU+Q8V5yZQHaaAaaGIF+eIjn4joDQAFWIPUKPzsOFBbH18uWchNPOiPBL7L015YJDuLL3KYL9Lqb7RQ==',
#     })

bitmex   = ccxt.bitmex()
print(bitmex.id, bitmex.load_markets())
print(bitmex.fetch_ticker('BTC/USD'))