import math

def Distance(coor1, coor2):
    x=((coor1[0]-coor2[0])*(coor1[0]-coor2[0]))
    y=((coor1[1]-coor2[1])*(coor1[1]-coor2[1]))
    d=math.sqrt(x+y)
    return d

def indexOfMinDist(coordinates, coordinate):
    min = 1000000.000
    index = -1
    for i in range(len(coordinates)):
        d = Distance(coordinates[i],coordinate)
        if d < min:
            min = d
            index = i
    return index
