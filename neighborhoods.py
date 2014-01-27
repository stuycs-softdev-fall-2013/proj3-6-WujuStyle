import urllib2
from bs4 import BeautifulSoup


def get_neighborhoods():
    r = []
    for x in open("pop.csv").read().split("\n"):
        y = x.split(",")
        if len(y) == 6 and y[5] != "Population":
            s = int(y[5])
            if s > 50000:
                n = y[4].split("-")[0]
                if n not in r:
                    r.append(n)
    return sorted(r)

if __name__ == "__main__":
    for x in get_neighborhoods():
        print x
