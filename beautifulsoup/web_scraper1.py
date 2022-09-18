from bs4 import BeautifulSoup
import requests

with open('index.html', 'r') as file:
    doc = BeautifulSoup(file, 'html.parser')

tags = doc.find_all('p')[0]

# print(tags.find_all('b')[1].find_all('i'))

#access nested tags in the html DOM

