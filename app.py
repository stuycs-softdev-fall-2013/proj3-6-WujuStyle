
from flask import Flask, render_template, request
import neighborhoods
import json
import gdirections

app = Flask(__name__)


@app.route("/")
def index():
    r = ""

    #script = "neighborhoods = %s"%(json.dumps(n))
    #script = "neighborhoods = ['Midtown','Upper East Side','Upper West Side','Harlem']"
    a = neighborhoods.get_neighborhoods()
    na =  []
    for x in range(0,len(a)):
        na.append(a[x][1])
    script = "neighborhoods = %s"%(json.dumps(na))

    return render_template("index.html",script=script)


@app.route("/info")
def js():
    start = request.args.get("start")
    end = request.args.get("end")
    
    ret = gdirections.get_all(start,end)
    ret["id"] = request.args.get("id")
    return json.dumps(ret)
    #return "%s,%d,%d"%(request.args.get("id"),ret["driving_time"],ret["transit_time"])

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0",port=5000)
