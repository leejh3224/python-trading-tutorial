import jwt
import uuid

import requests

access_key = ""
secret_key = ""
server_url = "https://api.upbit.com"

payload = {
    "access_key": access_key,
    "nonce": str(uuid.uuid4()),
}

jwt_token = jwt.encode(payload, secret_key)
authorize_token = "Bearer {}".format(jwt_token)
headers = {"Authorization": authorize_token}

res = requests.get(server_url + "/v1/accounts", headers=headers)

print(res.json())
