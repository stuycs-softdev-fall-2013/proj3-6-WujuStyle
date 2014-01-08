import urllib2


def getNeighborhoods()
response = urllib.urlopen("http://en.wikipedia.org/wiki/Neighborhoods_in_New_York_City")
html = response.read()
string = html.find(
