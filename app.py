

from flask import Flask, render_template
import neighborhoods
import json

app = Flask(__name__)


@app.route("/")
def index():
    r = ""
    script = "neighborhoods = %s"%(json.dumps(neighborhoods.getNeighborhoods()))

    return render_template("index.html",script=script)


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0",port=5000)
