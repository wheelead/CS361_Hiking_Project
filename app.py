import requests, json
from flask import Flask, render_template, request
from geopy.geocoders import Nominatim
from recs import getHikingRecs, getWeatherRecs

app = Flask(__name__)

API_KEY = "200965658-b1cfd20b05f2212f32f16c23ff4a7c3c"
WEATHER_API_KEY = "5dc2540a0d627e4840439a258adeb337"



@app.route("/")
def home():
    return render_template("home.html")



@app.route("/fitness")
def fitness():
    return render_template("fitnessTest.html")
if request.method == "GET":
    level = request.form.get('level');


@app.route("/Trail_List", methods=["GET", "POST"])
def trail_list():
    tableDict = { "blank" : "blank" }
    radius = 0
    if request.method == "POST":
        code = request.form.get('input') # user zip or address
        radius = request.form.get('radius') # miles radius
        geoGen = Nominatim(user_agent="hikingproject") # set up system for geocode
        place = geoGen.geocode(code)  # get lat and lon

        # make url for get to hiking project API.
        urlString = "http://www.hikingproject.com/data/get-trails?"
        # maxDistance upper bound is 300
        # maxResults upper bound is 500
        urlString += "lat={}&lon={}&maxDistance={}&key={}&sort=distance&maxResults=500"
        finalUrl = urlString.format(place.latitude, place.longitude, radius, API_KEY)

        # dictionary holding response data
        tableDict = json.loads(requests.get(finalUrl).content)

    return render_template("trail_list.html", tableDict = tableDict, radius = radius)



@app.route("/recs/<int:trailID>", methods=["GET", "POST"])
def recommendations(trailID):
    # print(trailID)

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

    # print(length, hikingCondition, elevation, lat, lon)

    # get weather data using hiking coords
    weatherUrlString = "http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}&units=imperial"
    weatherFinalUrl = weatherUrlString.format(lat, lon, WEATHER_API_KEY)
    weatherData = json.loads(requests.get(weatherFinalUrl).content)
    # print(weatherData)

    main = weatherData["main"]
    temp = main["temp"] # degrees fahrenheit 

    wind = weatherData["wind"]
    windCondition = wind["speed"] # miles/hour

    for i in weatherData["weather"]:
        weatherCondition = i["main"] # Rain, Snow, Extreme

    hikingRecs = getHikingRecs(length, hikingCondition, elevation) # returned dict
    weatherRecs = getWeatherRecs(temp, windCondition, weatherCondition) # returned dict 
#    print(hikingRecs)
#    print(weatherRecs)
    return render_template("recs.html", hikingRecs=hikingRecs, weatherRecs=weatherRecs)
