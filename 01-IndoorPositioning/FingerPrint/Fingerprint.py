from operator import itemgetter as ig
from math import floor, sqrt, ceil


class RSSVector:
    distances = []

    def __init__(self, n1, n2, n3, n4):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4


class Location:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z


class Cell:
    def __init__(self, v_, loc):
        self.v = v_
        self.location = loc


def newCell(n1, n2, n3, n4, l1, l2):
    return Cell(RSSVector(n1, n2, n3, n4), Location(l1, l2))


def KNeighbors(fingerprints, sample):
    distances = []
    for row in fingerprints:
        for currentItem in row:
            dist = abs(currentItem.v.n1 - sample.n1) \
                   + abs(currentItem.v.n2 - sample.n2) \
                   + abs(currentItem.v.n3 - sample.n3) \
                   + abs(currentItem.v.n4 - sample.n4)
            distances.append((dist, currentItem))
    distances = sorted(distances, key=ig(0))
    sample.distances = [x[0] for x in distances][:4]
    return [x[1] for x in distances][:4]
