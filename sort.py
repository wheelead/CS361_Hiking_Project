import json

def sortByDifficulty(trailsDic, value):
	listOfKeys = list()
	listOfItems = trailsDic.items()
	for item in listOfItems:
		if item[1] == value:
			listOfKeys.append(item[0])
	return listOfKeys

def sortIt(jfy, lvl, tableDict):
	# logic to sort data
	if jfy == "checked":
		if lvl == "1":
			#makes it easier to read the info about the trails
			json_object = json.dumps(tableDict, indent = 2)
			print(json_object)
			#print(type(json_object))			#string
			#print(type(tableDict))				#dict
			#print(type(tableDict['trails']))	#list

			#create an empty dictonary to hold filtered results
			filtered_trails = []

			#iterate through tableDict to get individual trails
			for trail in tableDict['trails']:
				if trail['difficulty'] == 'green':
				    filtered_trails.append(trail) 		#only one match gets added
					#filtered_trails.update(trail)	#only last match gets added

			print("filtered trails")
			print(filtered_trails)


			##print dict
			#for item in tableDict.items():
			#	print(item)
			
			##print dict
			#for k, v in tableDict.items():
			#	print(k, v)
			
			##print dict
			#for key, value in sorted(tableDict.items(), key=lambda x: x):
			#	print(key, value)

			##returns true
			#print(any(trails['difficulty'] == 'green' for trails in tableDict['trails']))
			tableDict['trails'] = filtered_trails

		elif lvl == "2":
			print("sort Match my Level")
		else:
			print("sort Challenge Me!")
	else:
		print("NO!")

#	tableDict['trails'] = filtered_trails # to be done after sorting implementd in all methods
	return tableDict