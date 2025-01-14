import requests
import json
import sys
r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
r = r.json()
bpi = r['bpi']
for currency in bpi:
    if currency == 'USD':
        details = bpi[currency]
        rate = details['rate']
        a = rate.split(',')
        rate = a[0] + a[1]
        rate = float(rate)
try:
    if len(sys.argv) == 2:
        a = float(sys.argv[1])
        total = a * rate
        total = f"${total:,.4f}"
        print(total)

    else:
        sys.exit('Missing command-line argument')
except ValueError:
    sys.exit('Command-line argument is not a number')
