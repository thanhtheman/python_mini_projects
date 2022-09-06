import urllib.request as urllib

print('Welcome to the site connection checker!')
input_url = input('Please input the url: ')

def checker(url):
    print('Checking your url...')
    response = urllib.urlopen(url)
    print('The response code is ', response.getcode())
       
checker(input_url)

