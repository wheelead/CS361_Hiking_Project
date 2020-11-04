import requests, json
from flask import Flask, render_template, request
from geopy.geocoders import Nominatim

app = Flask(__name__)

API_KEY = "200965658-b1cfd20b05f2212f32f16c23ff4a7c3c"

@app.route("/")
def index():
    return render_template("index.html")

#@app.route("/Trail_List")
#def trail_list():
#       return render_template("trail_list.html")

@app.route("/Trail_List", methods=["GET", "POST"])
def trail_list():
    tableDict = { "blank" : "blank" }
    if request.method == "POST":
        code = request.form.get('input') # user input
        geoGen = Nominatim(user_agent="hikingproject") # set up system for geocode
        place = geoGen.geocode(code)  # get lat and lon
        # print("Latitude = {}, Longitude = {}".format(place.latitude, place.longitude))

        # make url for get to hiking project API
        urlString = "http://www.hikingproject.com/data/get-trails?"
        # maxDistance upper bound is 300
        # maxResults upper bound is 500
        urlString += "lat={}&lon={}&maxDistance={}&key={}&sort=distance"
        finalUrl = urlString.format(place.latitude, place.longitude, 10, API_KEY)
        #print(finalUrl)

        # dictionary holding response data
        tableDict = json.loads(requests.get(finalUrl).content)

    return render_template("trail_list.html", tableDict = tableDict)

