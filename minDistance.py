import math

def Distance(coor1, coor2):
    x=((coor1[0]-coor2[0])*(coor1[0]-coor2[0]))
    y=((coor1[1]-coor2[1])*(coor1[1]-coor2[1]))
    d=math.sqrt(x+y)
    return d

def indexOfMinDist(coordinates, coordinate):
    try:
        coordinate[0][1]
        coordinate[0] = float(coordinate[0])
        coordinate[1] = float(coordinate[1])

    except:
        pass
    minn = 1000000.0
    index = -1
    for i in range(len(coordinates)):
        d = Distance(coordinates[i],coordinate)
        if d < minn:
            minn = d
            index = i
    return index
