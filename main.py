import requests
import re
from bs4 import BeautifulSoup as bs
import smtplib, ssl

class CheckInventory:

    def get_status(self):
        r = requests.get("https://www.microcenter.com/product/601213/corsair-sf750-750-watt-80-plus-platinum-sfx-fully-modular-power-supply?storeid=141")
        src = r.content
        soup = bs(src, features="html.parser")
        inventory = soup.find("span", {"class" : "inventoryCnt"})
        return inventory.text

    def get_connection(self):
        port = 465  # For SSL
        password = input("Type your password and press enter: ")
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login("development@hunterholland.com", password)

def main():
    test = CheckInventory()
    if test.get_status() != 'Sold Out':
        test.get_connection()

if __name__ == '__main__': main()
        

        