import urllib2
import json


def getCoordinates(d):
    url = "http://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false"%(d.replace(" ","+"))
    

    result = urllib2.urlopen(url)
    a = {}
    try: 
        g = json.loads(result.read())["results"][0]

        a["borough"] = g["address_components"][3]["long_name"]
        a["neighborhood"] = g["address_components"][2]["long_name"]
        a["lat"] = g["geometry"]["location"]["lat"]
        a["long"] = g["geometry"]["location"]["long"]
    
        
    except:
        return -1;

    return a 

def getDirections(e,f): 
    url = "http://maps.googleapis.com/maps/api/directions/json?origin=%s&destination=%s&sensor=false"%(e.replace(" "," "),f.replace(" "," "))
    
    result = urllib2.urlopen(url);
    
    r = {}
    try: 
        k = json.loads(result.read())["results"][0]

        r["how_to_get_there"]=k["directions"][3]["routes"]

    except:
        return -1
    
    return r

if __name__ == "__main__":
    print getDirections("Upper East Side","Upper West Side")
