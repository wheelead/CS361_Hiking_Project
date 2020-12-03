# Created for CS 361 by team "To Be Determined"
# Chelsea Satterwhite, Adam Wheeler, Diane Nguyen, Colin Kasowski, and Nick Dal

"""
Name: getTrailDetails
Called by: app.py
Calls: none
Passed: name, length, description, lat, lon, elevation, conditions
Returns: detailsDict

Function to help display details of specific trails because I have no
clue what I am doing. """
def getTrailDetails(ID, name, length, description, lat, lon, elevation, conditions, location):
    detailsDict = { "ID":ID, "name": name, "length":length, "description":description, "lat":lat, "lon":lon, "elevation":elevation, "conditions":conditions, "location":location }
    
    return detailsDict
    

