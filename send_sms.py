# we import the Twilio client from the dependency we just installed
from twilio.rest import Client

# the following line uses your Twilio Account SID and Auth Token
client = Client("ACbe61ee2181e6cbe1334a7885c363dca8","afe4103687a7691025db12e10012335d")

# "from_" number is your Twilio number and the "to" number
# is the phone number you signed up for Twilio with, or upgrade your 
# account to send SMS to any phone number

def call(capacity, spots):
	message = "Reached capacity"
	sms = client.messages.create(to="+16476252949", 
						   from_ ="+15717770102",
						   body=message)  
	return sms

call(50,0)