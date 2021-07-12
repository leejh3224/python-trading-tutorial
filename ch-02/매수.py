import jwt
import uuid
import hashlib
from urllib.parse import urlencode

import requests

access_key = ""
secret_key = ""
server_url = "https://api.upbit.com"

"""
# 시장가 매수
query = {
    "market": "KRW-BTC",
    "side": "bid",
    "price": "5000.0",
    "ord_type": "price",
}

# 시장가 매도
query = {
    "market": "KRW-BTC",
    "side": "ask",
    "volume": "0.01",
    "ord_type": "market",
}
"""
query = {
    "market": "KRW-BTC",
    "side": "bid",
    "volume": "1",
    "price": "5000.0",
    "ord_type": "limit",
}
query_string = urlencode(query).encode()

m = hashlib.sha512()
m.update(query_string)
query_hash = m.hexdigest()

payload = {
    "access_key": access_key,
    "nonce": str(uuid.uuid4()),
    "query_hash": query_hash,
    "query_hash_alg": "SHA512",
}

jwt_token = jwt.encode(payload, secret_key)
authorize_token = "Bearer {}".format(jwt_token)
headers = {"Authorization": authorize_token}

res = requests.post(server_url + "/v1/orders", params=query, headers=headers)

print(res.json())
