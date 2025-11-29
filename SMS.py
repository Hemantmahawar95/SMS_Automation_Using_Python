from twilio.rest import Client

account_sid = "Enter _ Your _ account_sid"
auth_token = "Enter Your auth_token"
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Hello from my Python SMS automation!",
    from_="+1XXXXXXXXXX",   
    to="+91XXXXXXXXX"      
)

print("Message SID:", message.sid)
