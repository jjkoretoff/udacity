#send a text using twilio

from twilio import rest
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC9ca4f8f92fd9cf0e107a874428985eab"
auth_token  = "f111e5a73bcc6806b3fd9cc92fcaef7f"
client = rest.TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(
    body="Test",
    to="+15598928360",    # Replace with your phone number
    from_="+15596680146") # Replace with your Twilio number
print message.sid

