import smtplib
import requests
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

# Twilio SID & TOKEN, from https://www.twilio.com/
TWILIO_SID = "*************************"
TWILIO_TOKEN = "*************************"
TWILIO_NUMBER = "*************************"
TARGET_NUMBER = "*************************"

 
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "***********************"
MY_PASSWORD = "*********"

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_TOKEN)

    def send_sms(self, flight):
        """Takes a flight object and sends the details as an SMS to the defined number."""
        message = f"Low Price alert! Only {flight.price} to fly from {flight.origin_city}-{flight.origin_airport} " \
                  f"to {flight.destination_city}-{flight.destination_airport}, " \
                  f"from {flight.leave_date} to {flight.return_date}."

        try:
            message = self.client.messages.create(body=message, from_=TWILIO_NUMBER, to=TARGET_NUMBER)
        except TwilioRestException as ex:
            print(ex)
            print("Make sure the TWILIO_SID, TWILIO_TOKEN, TWILIO_NUMBER and TARGET_NUMBER are set properly.")
        else:
            print(message.status)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )