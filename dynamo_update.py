import json

print('Loading function')

def lambda_handler(event, context):
	print('------------------------')
	print(event)
	#1. Iterate over each record
	try:
		for record in event['Records']:
			#2. Handle event by type
			if record['eventName'] == 'INSERT':
				handle_insert(record)
		print('------------------------')
		return "Success!"
	except Exception as e: 
		print(e)
		print('------------------------')
		return "Error"


def handle_insert(record):
	print("Handling INSERT Event")
	
	#3a. Get newImage content
	newImage = record['dynamodb']['NewImage']
	
	#3b. Parse values
	newid = newImage['id']['S']
	newdate = newImage['date']['N']
	newsoil_moisture = newImage['soil_moisture']['S']
	newwind_speed = newImage['wind_speed']['S']

	#3c. Print it
	print ('id=' + newid)
	print('date=' + newdate)
	print('New soil moisture=' + newsoil_moisture)
	print('New wind speed=' + newwind_speed)

	print("Done handling INSERT Event")
