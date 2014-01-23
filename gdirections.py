import urllib2
import json
import calendar
import time

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def getUrl(start, end):
    start,end=start.replace(" ","+"),end.replace(" ","+")
    if is_number(start[:9]):
        a="http://maps.googleapis.com/maps/api/directions/json?origin=%s&destination=%s&sensor=true&departure_time=%s&mode=%s"
    else:
        a="http://maps.googleapis.com/maps/api/directions/json?origin=%s&destination=%s&sensor=false&departure_time=%s&mode=%s"
    url = a % (start, end, calendar.timegm(time.gmtime()), "driving",)
    jsonurl = urllib2.urlopen(url)
    text = json.load(jsonurl)
    text = text['routes'][0]['legs'][-1]
    dt = 0
    dd = 0
    tt = 0
    dt,dd = text['duration']['value'],text['distance']['value']
    url = a % (start, end, calendar.timegm(time.gmtime()), "transit")
    jsonurl = urllib2.urlopen(url)
    text = json.load(jsonurl)
    text = text['routes'][0]['legs'][-1]
    tt = text['duration']['value']
    dict={'driving_time':dt, 'driving_distance':dd, 'transit_time':tt}
    return dict

if __name__ == "__main__":
    getUrl("345 Chambers street nyc","309 west 104th street nyc")
