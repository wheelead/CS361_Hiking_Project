import json, os

# added to remove relative only behaviour
script_path = os.path.dirname(__file__)

with open(script_path + "/static/hiking_recs.json") as f:
    data = json.load(f)

""" 
Name: getHikingRecs
Called by: app.py
Calls: setHikingElevation, setHikingDistance, getHikingDict
Passed: len, condition, elevation
Returns: hikingDict

Function takes in instance of hiking trail information and 
decides which recommendations to return to display on recommendations page """
def getHikingRecs(trailDistance, condition, elevation):
    hikingElevation = setHikingElevation(elevation)
    length = setHikingDistance(trailDistance)
    hikingDict = getHikingDict(length, hikingElevation, condition)

    return hikingDict

def setHikingElevation(elevation):
    # if elevation is more than 5000 ft, set highElevation to true and recommend high elevation item[s]
    if elevation > 5000:
        highElevation = True
    else:
        highElevation = False
    return highElevation

def setHikingDistance(trailDistance):
    if trailDistance < 2.0: # in miles
            length = "short"
    elif trailDistance > 2.0 and trailDistance < 5.0:
        length = "medium"
    else:
        length = "long"
    return length

def getHikingDict(length, highElevation, condition):
    # create empty array to hold list of recs
    recs = []
    hikingRecs = []
    hikingDict = dict()
    hikingDict["recs"] = []
    for rec in data["gear_recs"]:
        # append each rec to the list
        if rec["essential"] == True: # by default, you need water and sunscreen for your hikes
            recs.append(rec)
        if rec["length"] == length:
            recs.append(rec)
        if rec["condition"] == condition:
            recs.append(rec)
        if highElevation == True:
            recs.append(rec)

    # check and remove dups
    for i in recs:
        if i not in hikingRecs:
            hikingRecs.append(i)

    hikingDict["recs"] = hikingRecs
    return hikingDict

""" 
Name: getWeatherRecs
Called by: app.py
Calls: setWindCondition, setTemp, getWeatherDict
Passed: temp, windCondition, weatherCondition
Returns: weatherDict

temp - float
windCondition - miles/hour
weatherCondition - Clear, Rain, Snow, Extreme """
def getWeatherRecs(temp, windCondition, weatherCondition):
    windy = setWindCondition(windCondition)
    cold = setTemp(temp)
    weatherDict = getWeatherDict(weatherCondition)
    # print(weatherDict)
    return weatherDict

def setWindCondition(windCondition):
    windy = False
    if windCondition > 5:
        windy = True
    return windy

def setTemp(temp):
    cold = False
    if temp < 65:
        cold = True

def getWeatherDict(weatherCondition):
    recs = []
    weatherRecs = []
    weatherDict = dict()
    weatherDict["recs"] = []
    for rec in data["clothing_recs"]:
        if rec["windCondition"] == True:
            recs.append(rec)
        if rec["cold"] == True:
            recs.append(rec)

    # check for weatherCondition 
    # weatherCondition value is in array format
    for rec in data["clothing_recs"]:
        num_weatherConditions = len(rec["weatherCondition"])
        for i in range(num_weatherConditions):
            # print(rec["weatherCondition"][i])
            if rec["weatherCondition"][i] == weatherCondition:
                recs.append(rec)
    
    # check for dups and remove them
    for i in recs:
        if i not in weatherRecs:
            weatherRecs.append(i)
    
    weatherDict["recs"] = weatherRecs
    return weatherDict
