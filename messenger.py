# Twilio API
# https://www.twilio.com/en-us
# https://console.twilio.com/?frameUrl=%2Fconsole%3Fx-target-region%3Dus1
#
# You need to connect to Twilio WhatsUp sandbox to be able to receive a messages. How to do it?
# Open
# https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn?frameUrl=%2Fconsole%2Fsms%2Fwhatsapp%2Flearn%3Fx-target-region%3Dus1
# and open your WhatsUp mobile app and scan QR code from the page above.
# Check logs here:
# https://console.twilio.com/us1/monitor/logs/sms

import os
from twilio.rest import Client

class Messenger:
    def __init__(self):
        account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
        auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
        self.client = Client(account_sid, auth_token)

    def send_message(self, text):
        message = self.client.messages.create(
            from_=os.environ.get('TWILIO_WHATSAPP_FROM'),
            body=text,
            to=os.environ.get('TWILIO_WHATSAPP_TO')
        )

        message_details = (message.sid, message.status)

        return message_details