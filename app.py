

from flask import Flask, render_template
import neighborhoods
import locator
import json


app = Flask(__name__)


@app.route("/")
def index():
    r = ""

    n = neighborhoods.getNeighborhoods()
    nei = []
    script = "neighborhoods = %s"%(json.dumps(n))

    for x in range(0,5):
        nei.append(locator.getCoordinates(n[x]+", New York City"))

    print str(nei)

    return render_template("index.html",script=script)


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0",port=5000)
