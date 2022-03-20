import requests

from bs4 import BeautifulSoup

url = 'https://www.ceneo.pl/95365253#tab=reviews'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

print(soup.prettify)