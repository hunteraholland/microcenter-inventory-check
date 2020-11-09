import requests
import re
from bs4 import BeautifulSoup as bs
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv
import send_email as se

load_dotenv()

site = "https://www.microcenter.com/product/601213/corsair-sf750-750-watt-80-plus-platinum-sfx-fully-modular-power-supply?storeid=141"

class CheckInventory:

    def get_status(self, site):
        r = requests.get(site)
        src = r.content
        soup = bs(src, features="html.parser")
        inventory = soup.find("span", {"class" : "inventoryCnt"})
        return inventory.text

def main():
    check = CheckInventory()
    # if check.get_status() == 'Sold Out':
    se.send_email()
    #check.send_email()

if __name__ == '__main__': main()
        

        