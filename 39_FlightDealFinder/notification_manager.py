
from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv('../.env')
TWILLIO_ACCOUNT_SID = os.getenv('TWILLIO_ACCOUNT_SID')
TWILLIO_AUTH_TOKEN = os.getenv('TWILLIO_AUTH_TOKEN')
NUMBER = os.getenv('NUMBER')
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self, flight_info):
        self.flight_info = flight_info
    def send_msg(self):
        account_sid = TWILLIO_ACCOUNT_SID
        auth_token = TWILLIO_AUTH_TOKEN
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f'Low price alert! Only {} to fly from {}-{} to {}-{}, from {} to {}.',
            from_='+12055393232',
            to=NUMBER
        )