import requests
import json
import re

#ask user for input
origin = raw_input("Start: ")
destination = raw_input("Finish: ")
mode = raw_input("walking, biking, driving, or transit? ")

#set parameters
parameters = {'origin': origin, 'destination': destination, 'mode': mode,\
 'key':'AIzaSyDN8B9TBohP8TDSqDBYUghxA3mta-8RoZQ'}

#send request to google
r = requests.get("https://maps.googleapis.com/maps/api/directions/json", params=parameters)

#turn response into a dictionary/list
parsed = json.loads(r.text)

#get information about total trip
legs = parsed['routes'][0]['legs'][0]
totalDistance = legs['distance']['text']
totalDuration = legs['duration']['text']
start_address = legs['start_address']
end_address = legs['end_address']

#print information to user
print "Directions from", start_address, "to", end_address
print "Distance:", totalDistance
print "Duration:", totalDuration

#get and print individual steps
steps = legs['steps']
numSteps = len(steps)
stepNum = 1
for step in steps:
	print "Step", stepNum
	stepNum += 1
	instructions = step["html_instructions"]
	instructions = re.sub(r'<.*?>', "", instructions)
	print instructions,"for", step['distance']['text'], "for approximately", step['duration']['text']
