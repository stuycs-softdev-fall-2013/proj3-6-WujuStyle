a = "http://maps.googleapis.com/maps/api/directions/json?origin=" 
b = "&destination="
c = "&mode="
d = "OK&sensor=false"

def getUrl(start, end, modeoftravel) {
    return a+start+b+end+c+modeoftravel+d
}
    
