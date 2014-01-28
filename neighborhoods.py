import urllib2
from bs4 import BeautifulSoup
from operator import itemgetter


def get_neighborhoods():
    r = []
    nei = []
    for x in open("pop.csv").read().split("\n"):
        y = x.split(",")
        if len(y) == 6 and y[5] != "Population":
            s = int(y[5])
            if s > 50000:
                n = y[4].split("-")[0]
                if n not in nei:
                    r.append([y[0],n])
                    nei.append(n)
    an = sorted(r,key=itemgetter(0,1),reverse=True)
    for x in range(0,len(an)):
        if an[x][0] == "Manhattan":
            an.insert(0,an.pop(x))
    return an

if __name__ == "__main__":
    for x in get_neighborhoods():
        print x
