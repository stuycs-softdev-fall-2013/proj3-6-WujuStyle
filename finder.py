from flask import Flash
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/")
def googlemaps(a):
    x = a.replace(" ", "+")
    return "http://maps.googleapis.com/maps/api/staticmap?center="+x + "http://maps.googleapis.com/maps/api/staticmap?center="+x+"&zoom=15&size=650x350&maptype=roadmap&markers=color:red%7Clabel:A%7C"+x+"&sensor=false"


    return render_template("index.html")


if __name__ == "__main__":
    curr = raw_input("Where are you now/Where do you want to start from:")
    area= raw_input("Enter area:")
    travel_style= raw_input("Are you driving, walking, or taking public transportation:")
    data = gmap(area, travel_style)
    print("maps.googleapis.com/maps/api/staticmap?center=" + curr + area + travel_style + "&markers=color:blue%7Clabel:C%7C"+ curr + area + travel_style + "&zoom=16&size=640x640&sensor=false&key=AIzaSyAEH1zvTqgnRGLX8WIerdMnjZiB2Scyys0"

    app.debug=True
    app.run(host="0.0.0.0",port=5000)

