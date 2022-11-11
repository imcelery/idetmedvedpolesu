import requests

import time

url = "https://yandex.ru/pogoda/"
response = requests.get(url)
find_text = """<a class="link fact__basic fact__basic_size_wide day-anchor i-bem" tabindex="0" href="/pogoda/details?lat=56.838011&amp;lon=60.597465&amp;via=mf#11" aria-label="""
n = response.text.find(find_text)

print(response.text[n+ len(find_text) + 1: n + response.text[n + len(find_text):].find(" data-bem") + len(find_text) - 1])