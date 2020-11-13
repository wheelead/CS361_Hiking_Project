import json

with open('static/hiking_recs.json') as f:
    data = json.load(f)

# function takes in instance of hiking trail information 
# decides which recommendations to return to display on recommendations page
def getHikingRecs(len, condition, elevation):
    highElevation = False
    if len < 2.0:
        length = "short"
    elif len > 2.0 and len < 5.0:
        length = "medium"
    else:
        length = "long"
    
    if elevation > 5000:
        highElevation = True

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

# temp - float
# windCondition - miles/hour
# weatherCondition - Clear, Rain, Snow, Extreme
def getWeatherRecs(temp, windCondition, weatherCondition):
    windy = False
    cold = False

    if windCondition > 5:
        windy = True
    if temp < 65:
        cold = True
    recs = []
    weatherRecs = []
    weatherDict = dict()
    weatherDict["recs"] = []
    for rec in data["clothing_recs"]:
        if rec["windCondition"] == True:
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
    # print(weatherDict)
    return weatherDict

# getHikingRecs(7.1, "Dry", 1000)
# getWeatherRecs(40, 4, "Rain")