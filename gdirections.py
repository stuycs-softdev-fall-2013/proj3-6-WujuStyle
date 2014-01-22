import urllib2
<<<<<<< HEAD
import json

a = "http://maps.googleapis.com/maps/api/directions/json?origin=%s&destination=%s&mode=%sOK&sensor=false"

def getUrl(start, end):
    url = a % (start, end, "driving")
    jsonurl = urllib2.urlopen(url)
    text = json.loads(jsonurl.read())
    return text

q = getUrl("Chicago", "NYC")
print q
=======

a = "http://maps.googleapis.com/maps/api/directions/json?origin=" 
b = "&destination="
c = "&mode="
d = "OK&sensor=false"

def getUrl(start, end, modeoftravel) {
    url = a+start+b+end+c+modeoftravel+d
    json = urllib2.urlopen(url).read()
    return json
}
    
>>>>>>> master
