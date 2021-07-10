import requests
import json

url = "https://api.upbit.com/v1/candles/days"

symbol = "DOGE"
count = 10

querystring = {
    # 원화 도지코인 마켓의 일봉 데이터
    "market": f"KRW-{symbol}",
    # 일봉 데이터의 개수 (일)
    "count": count,
}

headers = {"Accept": "application/json"}

response = requests.request("GET", url, headers=headers, params=querystring)

json_str = json.dumps(json.loads(response.text), indent=2)

print(json_str)
