var a = "http://maps.googleapis.com/maps/api/directions/json?origin=" 
var b = "&destination="
var c = "&mode="
var d = "OK&sensor=false"

directions = function(start, end, modeoftravel) {
    return getjson(a+start+b+end+c+modeoftravel+d)
}
    