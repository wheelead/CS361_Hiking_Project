from flask import Flask, render_template, request

app = Flask(__name__)

#API_KEY =

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/Trail_List")
def trail_list():
#    if request.form.get('zip')
#        zip = request.form.get('zip')
#
#        r = requests.get(
#            'https://www.hikingproject.com/data/get-trails?lat=40.0274&amp;lon=-105.2519&amp;maxDistance=10&amp;key=')
    return render_template("trail_list.html")

