import os
import smtplib

from twilio.rest import Client
# Set environment variables
os.environ["TWILIO_SID"] = "AC3d342c8c9f10edadb2cfc6eaeac7fccc"
os.environ["TWILIO_AUTH_TOKEN"] = "d0822d7644982ceb0d5eb58c2b9fe2da"
os.environ["TWILIO_VIRTUAL_NUMBER"] = "+15185046063"
os.environ["TWILIO_VERIFIED_NUMBER"] = "+9720505427551"




# TWILIO_SID = "AC3d342c8c9f10edadb2cfc6eaeac7fccc"
# TWILIO_AUTH_TOKEN = "d0822d7644982ceb0d5eb58c2b9fe2da"
# TWILIO_VIRTUAL_NUMBER = "+15185046063"
# TWILIO_VERIFIED_NUMBER = "+9720505427551"

# Get environment variables
TWILIO_SID = os.getenv('TWILIO_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_VIRTUAL_NUMBER = os.getenv('TWILIO_VIRTUAL_NUMBER')
TWILIO_VERIFIED_NUMBER = os.getenv('TWILIO_VERIFIED_NUMBER')

class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, massage):
        message = self.client.messages.create(
            body=massage,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER, # put the phone number we want to sent the massage
        )

        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        ###################################################
        MY_EMAIL = "tomtest75@yahoo.com"
        MY_PASSWORD = "iqqdvqotipaliuuv"
        EMAIL_PROVIDER_SMTP_ADDRESS = "smtp.mail.yahoo.com"
        with smtplib.SMTP(EMAIL_PROVIDER_SMTP_ADDRESS, port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )
