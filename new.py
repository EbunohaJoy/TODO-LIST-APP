import requests

# import api_key


headers = {
    'X-CMC_PRO_API_KEY': 'b83111ae-a2c1-4d37-bb64-db3146abdde0',
    'Accepts': 'application/json',
}
params = {
    'start': '1',
    'limit': '5',
    'convert': 'USD'
}
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

r = requests.get(url, params=params, headers=headers).json()

coins = r['data']
for x in coins:
    print(x['symbol'], x['quote']['USD']['price'])
print(x)
# print(r)


