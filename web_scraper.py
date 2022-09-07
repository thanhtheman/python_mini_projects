import requests
from bs4 import BeautifulSoup

url = 'https://www.codewithtomi.com/'

# get the DOM
r = requests.get(url)

#parse the content with the html.parser tool
soup = BeautifulSoup(r.content, 'html.parser')

#find the content we need
result = soup.find_all('h2', {'class': 'post-title'})

for i in result:
    print(i.getText())
