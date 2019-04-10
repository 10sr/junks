#!/usr/bin/env python3

from twilio.rest import Client

from ast import literal_eval

# Your Account Sid and Auth Token from twilio.com/console

with open("./secret.py") as f:
    secret = literal_eval(f.read())

account_sid = secret["sid"]
auth_token = secret["token"]

client = Client(account_sid, auth_token)

with open("main.py") as f:
    body = f.read()

message = client.messages.create(
                              from_=secret["from"],
                              body="\n\n" + body,
                              to=secret["to"]
                          )

print(message.sid)
