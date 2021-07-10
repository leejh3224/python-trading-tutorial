import requests

url = "https://api.upbit.com/v1/candles/days"

querystring = {
    # 원화 비트코인 마켓의 일봉 데이터
    "market": "KRW-BTC",
    # 일봉 데이터의 개수 (일)
    "count": "1",
}

headers = {"Accept": "application/json"}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
