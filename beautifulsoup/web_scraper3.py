from bs4 import BeautifulSoup
import requests

#getting crypto-currency price
url ='https://coinmarketcap.com/'
result = requests.get(url).text
doc = BeautifulSoup(result, 'html.parser')
tbody = doc.tbody
trs = tbody.contents

prices = {}
name = trs[0].find('a').find('p').text
for tr in trs[:10]:
    name, price = tr.contents[2:4]
    fixed_name = name.p.string
    fixed_price = price.a.string
    prices[fixed_name] = fixed_price

print(prices)

