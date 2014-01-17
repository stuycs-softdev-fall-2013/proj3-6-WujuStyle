from urllib2 import urlopen
import json

a = "http://maps.googleapis.com/maps/api/directions/json?origin=" 
b = "&destination="
"""c = "&mode="""
d = "OK&sensor=false"

def getUrl(start, end):
    url = a+start+b+end+d
    jsonurl = urlopen(url)
    text = json.loads(jsonurl.read())
    return text

q =  getUrl("Chicago","New York City")
print q
