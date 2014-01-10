from flask import Flash
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/")
def googlemaps(a):
    x = a.replace(" ", "+")
    return "http://maps.googleapis.com/maps/api/staticmap?center="+


    return render_template("index.html")


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0",port=5000)
