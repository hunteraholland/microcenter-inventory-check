import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()


def send_email():
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = "hunterhollandev@gmail.com"  # Enter your address
        from_email = "development@hunterholland.com"
        receiver_email = "huntholland@gmail.com"  # Enter receiver address
        password = os.getenv("GMAIL_PASSWORD")

        message = MIMEMultipart("alternative")
        message["Subject"] = "Get yo powasupply"
        message["From"] = sender_email
        message["To"] = receiver_email


        text = """\
        Greetings Hunter,
        You're a beast and your program worked. Welcome to the sff pc game.
        Sincerely,
        Hunter Holland LLC Dev Team"""
        html = """\
        <html>
        <body>
            <p>Greetings Hunter,<br>
            You're a beast and your program worked. Welcome to the sff pc game.<br>
            Sincerely,<br>
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
            server.sendmail(sender_email, receiver_email, message.as_string())