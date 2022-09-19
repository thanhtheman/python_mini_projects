from bs4 import BeautifulSoup
import re

with open('index2.html', 'r') as file:
    doc = BeautifulSoup(file, 'html.parser')

# tag = doc.find('option')
# print(tag)
# to access/change the tag attribute, we just treat this element as a dictionary: key - value pair

# print(tag['value'])

# tag['value'] = 'new-course'
# print(tag)

# find things with condition, or find multiple tag
# multiple_tags = doc.find_all(['option', 'h1'])
# tags = doc.find_all(['option'], text='Undergraduate')
# print(tags)

#find things pased on class name, class is a reserved word in Python to write class - OPP
# tags = doc.find_all(class_ = 'btn-item')

#regular expresion
tags = doc.find_all(text = re.compile("\$.*"), limit=1)
for i in tags:
    print(i.strip())