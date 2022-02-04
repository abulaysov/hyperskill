import requests
import json

cod = input().lower()
req = requests.get(f'http://www.floatrates.com/daily/{cod}.json')
json_data = json.loads(req.content)

cache = {}
if cod == 'usd':
    cache['eur'] = json_data['eur']['inverseRate']
elif cod == 'eur':
    cache['usd'] = json_data['usd']['inverseRate']
else:
    cache['eur'] = json_data['eur']['inverseRate']
    cache['usd'] = json_data['usd']['inverseRate']

currency = input()
while currency != '':
    money = float(input())
    print('Checking the cache...')
    if cache.get(currency, None):
        print('Oh! It is in the cache!')
        print(f'You received {round(money / cache[currency], 2)} {currency}.')
    else:
        cache[currency] = json_data[currency]['inverseRate']
        print('Sorry, but it is not in the cache!')
        print(f'You received {round(money / cache[currency], 2)} {currency}.')
    currency = input().lower()
