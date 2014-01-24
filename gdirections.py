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

def getInfo(start2, end2, type):
    start,end = "",""
    if isinstance(start2, str):
        start = start2.replace(" ","+")
        end = end2.replace(" ","+")
    elif isinstance(start2, list):
        if isinstance(start2[0], str):
            start = start2[0]+","+start2[1]
            end = end2[0]+","+end2[1]
        else:
            start = str(start2[0])+","+str(start2[1])
            end = str(end2[0])+","+str(end2[1])
    start,end=start.replace(" ","+"),end.replace(" ","+")
    if is_number(start[:9]):
        a="http://maps.googleapis.com/maps/api/directions/json?origin=%s&destination=%s&sensor=true&departure_time=%s&mode=%s"
    else:
        a="http://maps.googleapis.com/maps/api/directions/json?origin=%s&destination=%s&sensor=false&departure_time=%s&mode=%s"
    dt,dd,tt,bt,wt = 0,0,0,0,0
    if type=='all' or type=='driving':
        url = a % (start, end, calendar.timegm(time.gmtime()), "driving",)
        jsonurl = urllib2.urlopen(url)
        text2 = json.load(jsonurl)
        try:
            text = text2['routes'][0]['legs'][-1]
        except:
            try:
                text = text2['routes'][0]['legs'][0]
            except:
                print text2['status']
        dt,dd = text['duration']['value'],text['distance']['value']

    if type=='all' or type=='transit':
        url = a % (start, end, calendar.timegm(time.gmtime()), "transit")
        jsonurl = urllib2.urlopen(url)
        text2 = json.load(jsonurl)
        try:
            text = text2['routes'][0]['legs'][-1]
        except:
            try:
                text = text2['routes'][0]['legs'][0]
            except:
                print text2['status']
        tt = text['duration']['value']
    
    if type=='all' or type=='bicycling' or type=='biking':
        url = a % (start, end, calendar.timegm(time.gmtime()), "bicycling")
        jsonurl = urllib2.urlopen(url)
        text2 = json.load(jsonurl)
        try:
            text = text2['routes'][0]['legs'][-1]
        except:
            try:
                text = text2['routes'][0]['legs'][0]
            except:
                print text2['status']
        bt = text['duration']['value']

    if type=='all' or type=='walking':
        url = a % (start, end, calendar.timegm(time.gmtime()), "walking")
        jsonurl = urllib2.urlopen(url)
        text2 = json.load(jsonurl)
        try:
            text = text2['routes'][0]['legs'][-1]
        except:
            try:
                text = text2['routes'][0]['legs'][0]
            except:
                print text2['status']
        wt = text['duration']['value']
    
    dict={'driving_time':dt, 'driving_distance':dd, 'transit_time':tt, 'biking_time':bt, 'walking_time':wt}
    return dict

if __name__ == "__main__":
    getInfo("345 Chambers street nyc","309 west 104th street nyc", 'driving')
    getInfo("40.76915505,-73.98191841","40.71754834,-74.01322069", 'transit')

