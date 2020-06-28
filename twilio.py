try : 
    from twilio.rest import Client
except : 
    import pip 
    pip.main(["install",'twilio'])
    from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACbd03c11c38e1e1b5a96c626e64d5753f'
auth_token = 'f245a79ff578022dcfa07fc2bd277e7d'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+15017122661',
                     to='+15558675310'
                 )

print(message.sid)