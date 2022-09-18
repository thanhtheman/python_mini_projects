from bs4 import BeautifulSoup
import requests

with open('index.html', 'r') as file:
    doc = BeautifulSoup(file, 'html.parser')

tags = doc.find_all('p')[0]

# print(tags.find_all('b')[1].find_all('i'))

#access nested tags in the html DOM

url ='https://www.newegg.ca/msi-geforce-rtx-3060-rtx-3060-ventus-3x-12g-oc/p/N82E16814137631?Description=gpu&cm_re=gpu-_-14-137-631-_-Product'

result = requests.get(url)

doc = BeautifulSoup(result.text, 'html.parser')
dollar_sign = doc.find_all(text="$")
parent_tag = dollar_sign[0].parent
price = parent_tag.find('strong')
decimals = parent_tag.find('sup')
# we will use get the parent tag of the dollar sign to see what tags are nested within it
print(price.text + decimals.text)