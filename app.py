from flask import Flask, render_template, request
from geopy.geocoders import Nominatim

app = Flask(__name__)

#API_KEY =

@app.route("/")
def index():
    return render_template("index.html")

#@app.route("/Trail_List")
#def trail_list():
#       return render_template("trail_list.html")

@app.route("/Trail_List", methods=["GET", "POST"])
def trail_list():
    tableString = ""
    if request.method == "POST":
        zip = request.form.get('zip')
        address = request.form.get('address')
        geoGen = Nominatim(user_agent="hikingproject")
        if zip:
            place = geoGen.geocode(zip)
        else:
            place = geoGen.geocode(address)
        print("Latitude = {}, Longitude = {}".format(place.latitude, place.longitude))

    return render_template("trail_list.html", tableString = tableString)

