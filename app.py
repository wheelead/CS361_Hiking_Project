# Created for CS 361 by team "To Be Determined"
# Chelsea Satterwhite, Adam Wheeler, Diane Nguyen, Colin Kasowski, and Nick Dal

import requests, json
from flask import Flask, render_template, request, session
from flask_session import Session
from geopy.geocoders import Nominatim
from recs import getHikingRecs, getWeatherRecs
from sort import sortIt

app = Flask(__name__)

# server side sessions to stor table data
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# external API keys
API_KEY = "200965658-b1cfd20b05f2212f32f16c23ff4a7c3c"
WEATHER_API_KEY = "5dc2540a0d627e4840439a258adeb337"

# global variables
LEVEL = "test"
INITIAL = "start"

# routing logic for the home page
@app.route("/", methods=["GET", "POST"])
def home():
    global INITIAL
    if INITIAL == "start":
        INITIAL = "started"
        session.clear()
        session['table'] = "empty"
        session['radius'] = 0

    if request.method == "POST":
        level = request.form.get('level')
        global LEVEL
        LEVEL = level

    return render_template("home.html")

# routing logic for the fitness test page
@app.route("/fitness")
def fitness():
    return render_template("fitnessTest.html")

# routing logic for the trail list page
@app.route("/trail_List", methods=["GET", "POST"])
def trail_list():

    if request.method == "GET" and (request.args.get('jfy') or request.args.get('lvl')) and not (session['table'] == "empty"):
        session['table'] = sortIt(request.args.get('jfy'), request.args.get('lvl'), session['table'], LEVEL)

    if request.method == "POST" and request.form.get('input'):
        code = request.form.get('input') # user zip or address
        if request.form.get('radius'):
            session['radius'] = request.form.get('radius') # miles radius
        else:
            session['radius'] = 30
        geoGen = Nominatim(user_agent="hikingproject") # set up system for geocode
        place = geoGen.geocode(code)  # get lat and lon

        # make url for get to hiking project API.
        urlString = "http://www.hikingproject.com/data/get-trails?"
        # maxDistance upper bound is 300
        # maxResults upper bound is 500
        urlString += "lat={}&lon={}&maxDistance={}&key={}&sort=distance&maxResults=500"
        finalUrl = urlString.format(place.latitude, place.longitude, session['radius'], API_KEY)

        # session dictionary holding response data
        session['table'] = json.loads(requests.get(finalUrl).content)

    return render_template("trail_list.html", tableDict = session['table'], radius = session['radius'])

# routing logic for the details page
@app.route("/details/<int:trailID>", methods=["GET", "POST"])
def details(trailID):
    
    # trail_id = 7017772 # potato chip rock
    hikingUrlString = "https://www.hikingproject.com/data/get-trails-by-id?ids={}&key={}"
    hikingFinalURL = hikingUrlString.format(trailID, API_KEY)
    trailData = json.loads(requests.get(hikingFinalUrl).content)
    
    for trail in trailData["trails"]:
        name = trail["name"]
        length = trail["length"]
        description = trail["summary"]
        lat = trail["latitude"]
        lon = trail["longitude"]
        elevation = trail["high"] - trail["low"]
        conditions = trail["conditionDetails"]
        
    trailDetails = getTrailDetails(name, length, description, lat, lon, elevation, conditions)
        
    return render_template("details.html")

# routing logic for recomendations page
@app.route("/recs/<int:trailID>", methods=["GET", "POST"])
def recommendations(trailID):

    # trail_id = 7017772 # potato chip rock
    hikingUrlString = "https://www.hikingproject.com/data/get-trails-by-id?ids={}&key={}"
    hikingFinalUrl = hikingUrlString.format(trailID, API_KEY)
    trailData = json.loads(requests.get(hikingFinalUrl).content)

    for trail in trailData["trails"]:
        length = trail["length"] # already a float - no need to convert
        hikingCondition = trail["conditionDetails"]
        elevation = trail["high"] - trail["low"]
        lat = trail["latitude"]
        lon = trail["longitude"]

    # get weather data using hiking coords
    weatherUrlString = "http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}&units=imperial"
    weatherFinalUrl = weatherUrlString.format(lat, lon, WEATHER_API_KEY)
    weatherData = json.loads(requests.get(weatherFinalUrl).content)

    main = weatherData["main"]
    temp = main["temp"] # degrees fahrenheit 

    wind = weatherData["wind"]
    windCondition = wind["speed"] # miles/hour

    for i in weatherData["weather"]:
        weatherCondition = i["main"] # Rain, Snow, Extreme

    hikingRecs = getHikingRecs(length, hikingCondition, elevation) # returned dict
    weatherRecs = getWeatherRecs(temp, windCondition, weatherCondition) # returned dict 

    return render_template("recs.html", hikingRecs=hikingRecs, weatherRecs=weatherRecs)
