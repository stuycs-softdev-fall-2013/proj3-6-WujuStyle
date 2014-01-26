

from flask import Flask, render_template, request
import neighborhoods
import json
import gdirections

app = Flask(__name__)


@app.route("/")
def index():
    r = ""

    n = neighborhoods.getNeighborhoods()
    #script = "neighborhoods = %s"%(json.dumps(n))
    script = "neighborhoods = ['Midtown','Upper East Side','Upper West Side','Harlem']"

    return render_template("index.html",script=script)


@app.route("/info")
def js():
    start = request.args.get("start")
    end = request.args.get("end")
    return gdirections.getInfo(start,end,"driving")

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0",port=5000)
