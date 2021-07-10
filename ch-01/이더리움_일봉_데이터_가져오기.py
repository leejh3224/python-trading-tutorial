import requests
import json

url = "https://api.upbit.com/v1/candles/days"

querystring = {
    # 원화 이더리움 마켓의 일봉 데이터
    "market": "KRW-ETH",
    # 일봉 데이터의 개수 (일)
    "count": "1",
}

headers = {"Accept": "application/json"}

response = requests.request("GET", url, headers=headers, params=querystring)

json_str = json.dumps(json.loads(response.text), indent=2)

print(json_str)
