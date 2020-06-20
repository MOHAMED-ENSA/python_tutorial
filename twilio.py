from twilio.rest import Client 
 
account_sid = 'ACbd03c11c38e1e1b5a96c626e64d5753f' 
auth_token = 'f245a79ff578022dcfa07fc2bd277e7d' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+212762357814',  
                              body='Is just a test!',      
                              to='whatsapp:+212642216140' 
                          ) 
 
print(message.sid)
