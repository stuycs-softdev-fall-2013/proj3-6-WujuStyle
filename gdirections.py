import urllib2
import simplejson

a = "http://maps.googleapis.com/maps/api/directions/json?origin=" 
b = "&destination="
c = "&mode="
d = "OK&sensor=false"

def getUrl(start, end, modeoftravel) {
    url = a+start+b+end+c+modeoftravel+d
    json = urllib2.urlopen(url).read()
    return json
}
    
