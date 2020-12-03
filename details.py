# Created for CS 361 by team "To Be Determined"
# Chelsea Satterwhite, Adam Wheeler, Diane Nguyen, Colin Kasowski, and Nick Dal
import requests, json


app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# API KEYS
API_KEY = "200965658-b1cfd20b05f2212f32f16c23ff4a7c3c"

"""
Name: getTrailDetails
Called by: app.py
Calls: none
Passed: name, length, description, lat, lon, elevation, conditions
Returns: detailsDict

Function to help display details of specific trails because I have no
clue what I am doing. """
def getTrailDetails(name, length, description, lat, lon, elevation, conditions):
    detailsDict = getDetailsDict(name, length, description, lat, lon, elevation, conditions)
    
    return detailsDict
    
def getDetailsDict(name, length, description, lat, lon, elevation, conditions):
    # Create empty array to hold details
    details = []
    detailsDict = dict()
    for details in 
