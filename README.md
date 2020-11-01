# CS361_Hiking_Project
<!-- 
Links I used to to get started: 
https://flask.palletsprojects.com/en/1.1.x/installation/
https://flask.palletsprojects.com/en/1.1.x/tutorial/layout/ 

Feel free to delete anything that you don't think belongs in the README 

What I pasted to get my env ready: 

python3 -m venv venv
. venv/bin/activate
pip install Flask
-->

To run the flask application: 
<pre><code>
flask run
</code></pre>

<ul>
<li>Update 10/31/2020: Made system a multi page setup instead of single and created 2 primitive pages.
Next step for Feature 2 is to add an api call.  This is proving more complicated than expected.
Looking into using geopy to get lat and lon to feed into trails api.</li>

<li>Update 2 10/31/2020: geopy worked.  To use the updated system you will need to install:<br>
pip install requests<br>
pip install geopy<br><br>
reqests is for GET and POST handling<br>
geopy is used to convert addresses or zips to latitude and longitude (can also be used for maps if google costs money)</li>