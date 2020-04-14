import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

SENDGRID_API_KEY = ""
MY_EMAIL_ADDRESS = "myd10@georgetown.edu"

SENDGRID_TEMPLATE_ID = os.environ.get(SENDGRID_API_KEY)
MY_ADDRESS = os.environ.get(MY_EMAIL_ADDRESS)

#print("API KEY:", SENDGRID_API_KEY)
#print("TEMPLATE ID:", SENDGRID_TEMPLATE_ID)
#print("EMAIL ADDRESS:", MY_ADDRESS)

template_data = {
    "total_price_usd": "$14.95",
    "human_friendly_timestamp": "June 1st, 2019 10:00 AM",
    "products":[
        {"id":1, "name": "Product 1"},
        {"id":2, "name": "Product 2"},
        {"id":3, "name": "Product 3"},
        {"id":2, "name": "Product 2"},
        {"id":1, "name": "Product 1"}
    ]
} # or construct this dictionary dynamically based on the results of some other process :-D

client = SendGridAPIClient(SENDGRID_API_KEY)
print("CLIENT:", type(client))

message = Mail(from_email=MY_ADDRESS, to_emails=MY_ADDRESS)
print("MESSAGE:", type(message))

message.template_id = SENDGRID_TEMPLATE_ID

message.dynamic_template_data = template_data

try:
    response = client.send(message)
    print("RESPONSE:", type(response))
    print(response.status_code)
    print(response.body)
    print(response.headers)

except Exception as e:
    print("OOPS", e)