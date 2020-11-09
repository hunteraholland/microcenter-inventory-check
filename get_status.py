import requests
import re
from bs4 import BeautifulSoup as bs

def get_status(site):
        r = requests.get(site)
        src = r.content
        soup = bs(src, features="html.parser")
        inventory = soup.find("span", {"class" : "inventoryCnt"})
        return inventory.text