import requests
import re
from bs4 import BeautifulSoup as bs
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class CheckInventory:

    def get_status(self):
        r = requests.get("https://www.microcenter.com/product/601213/corsair-sf750-750-watt-80-plus-platinum-sfx-fully-modular-power-supply?storeid=141")
        src = r.content
        soup = bs(src, features="html.parser")
        inventory = soup.find("span", {"class" : "inventoryCnt"})
        return inventory.text

    def send_email(self):
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = "hunterhollandev@gmail.com"
        from_email = "development@hunterholland.com"
        receiver_email = "huntholland@gmail.com"
        password = input("Type your password and press enter: ")

        message = MIMEMultipart("alternative")
        message["Subject"] = "Get Yo Powasupply"
        message["From"] = from_email
        message["To"] = receiver_email
        text = """\
        Greetings Hunter,
        You're a beast and your program worked. Welcome to the sff pc game.
        Sincerely,
        Hunter Holland LLC Dev Team
        """
        html = """\
        <html>
        <body>
            <p>Greetings Hunter,<br>
            You're a beast and your program worked. Welcome to the sff pc game.<br>
            Sincerely, <br>
            Hunter Holland LLC Dev Team
            </p>
        </body>
        </html>
        """

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)


        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)

def main():
    test = CheckInventory()
    if test.get_status() == 'Sold Out':
        test.send_email()

if __name__ == '__main__': main()
        

        