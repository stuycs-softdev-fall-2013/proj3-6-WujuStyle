import json
import urllib2


url = 'http://citibikenyc.com/stations/json'

response = urllib2.urlopen(url)
x = response.read()
data = json.loads(x)
print data.keys()

def getdirections()
long = data['longitude']
lat = data['latitude']

[ [34.12312312,-345421534], [2342341, 2544], [123.45436, -32443] ... ]
 
