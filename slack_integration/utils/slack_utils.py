import slack
from django.conf import settings


def send_message(msg):
    client = slack.WebClient(token=settings.SLACK_TOKEN)
    client.chat_postMessage(channel='#aws_details', text=msg)

