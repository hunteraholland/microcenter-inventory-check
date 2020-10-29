import requests
import re
from bs4 import BeautifulSoup as bs

r = requests.get("https://www.microcenter.com/product/601213/corsair-sf750-750-watt-80-plus-platinum-sfx-fully-modular-power-supply?storeid=141")

src = r.content

soup = bs(src, features="html.parser")

inventory = soup.find("span", {"class" : "inventoryCnt"})

if inventory.text == "Sold Out":
    print("true")
else:
    print("false")