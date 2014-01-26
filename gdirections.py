import urllib2
import json
import calendar
import time

def get_all(start,end):
    driving = get_info2(start,end,"driving")
    transit = get_info2(start,end,"transit")
    return {
        "driving_distance":driving[0],
        "driving_time":int(driving[1]/60),
        "transit_distance":transit[0],
        "transit_time":int(transit[1]/60)
        }

def get_info2(start,end,mode):
    url = "http://maps.googleapis.com/maps/api/directions/json?origin=%s&destination=%s&sensor=false&departure_time=%s&mode=%s"%(start.replace(" ","+"),end.replace(" ","+"),calendar.timegm(time.gmtime()),mode)
    a = json.loads(urllib2.urlopen(url).read())
    
    if a["status"] == "OVER_QUERY_LIMIT":
        time.sleep(1)
        return get_info2(start,end,mode)
    else:
        return [a["routes"][0]["legs"][0]["distance"]["value"],a["routes"][0]["legs"][0]["duration"]["value"]]

if __name__ == "__main__":
    print str(get_all("Stuyvesant High School","Upper East Side"))
