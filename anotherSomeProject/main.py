import requests

from bs4 import BeautifulSoup
import lxml


url = "https://yandex.ru/pogoda/"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

print(soup.find(class_="temp__value temp__value_with-unit").text)
print(soup.find(class_="fact__temp-wrap").find("a").label)
