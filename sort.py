# Created for CS 361 by team "To Be Determined"
# Chelsea Satterwhite, Adam Wheeler, Diane Nguyen, Colin Kasowski, and Nick Dal
# File creater and owner: Chelsea Satterwhite

import json

def sortByDifficulty(trailsDict, trailsList, calcDifficulty):
	
	#get a single trail from the trails dictionary 
	for trail in trailsDict['trails']:
		if trail['difficulty'] == calcDifficulty:
			#only add the trails that match the difficulty color given
			trailsList.append(trail)

	#add our new filtered list to the dictionary 
	trailsDict['trails'] = trailsList
	
	return trailsDict

def sortIt(jfy, lvl, tableDict, fitLevel):
	#fitness level = begginer by default
	fitnessLevel = 1

	#calculate the hike difficulty
	if fitLevel == "Begginer":
		fitnessLevel = 1
	elif fitLevel == "Intermediate":
		fitnessLevel = 2
	elif fitLevel == "Advanced":
		fitnessLevel = 3
	
	hikeDifficulty = fitnessLevel + int(lvl)
	#print(hikeDifficulty) 

	#create an empty list to hold filtered trails
	filtered_trails = []

	#see if toggle for filter is turned on
	if jfy == "checked":

		#use the hike difficulty calculation from above to match with given trail difficulty
		if hikeDifficulty == 2:
			tableDict = sortByDifficulty(tableDict, filtered_trails, 'green')
		elif hikeDifficulty == 3:
			tableDict = sortByDifficulty(tableDict, filtered_trails, 'greenBlue')
		elif hikeDifficulty == 4:
			tableDict = sortByDifficulty(tableDict, filtered_trails, 'blue')
		elif hikeDifficulty == 5:
			tableDict = sortByDifficulty(tableDict, filtered_trails, 'blueBlack')
		elif hikeDifficulty == 6:
			tableDict = sortByDifficulty(tableDict, filtered_trails, 'black')
		else:
			print("OVER 9000!")
			
	#else toggle for filter is turned off
	#do nothing

	return tableDict