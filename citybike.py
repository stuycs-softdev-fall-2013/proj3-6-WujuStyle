import urllib2, minDistance, gdirections, json, calendar, time, math

def citybikeTime(start,end):
    ff = open("bikeLocations.txt","r")
    ff = ff.read()
    ff = ff.split()
    f = []
    for i in ff:
        f.append([float(i.split(',')[0]),float(i.split(',')[1])])
    i = minDistance.indexOfMinDist(f,start)
    j = minDistance.indexOfMinDist(f,end)
    startCitybikeLoc = f[i]
    endCitybikeLoc = f[j]
    bikingTime = gdirections.getInfo(startCitybikeLoc, endCitybikeLoc)['biking_time']
    startWalkingTime = gdirections.getInfo(startCitybikeLoc, start)['walking_time']
    endWalkingTime = gdirections.getInfo(endCitybikeLoc, end)['walking_time']
    return startWalkingTime+bikingTime+endWalkingTime
    
print citybikeTime(["40.8004774","-73.9697269"],["40.7179985","-74.0138245"])
