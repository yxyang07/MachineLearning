from math import sqrt
from numpy import arange


class Position:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def toString(self):
        return "(" + str(self.x) + " ; " + str(self.y) + " ; " + str(self.z) + ")"

    def distanceTo(self, loc):
        return sqrt(pow(self.x - loc.x, 2) + pow(self.y - loc.y, 2) + pow(self.z - loc.z, 2))


def NLateration(data, xSize=0.0, ySize=0.0, zSize=0.0):
    minLoc = Position()
    minDist = 0.0
    for k in data:
        minDist += abs(k[0].distanceTo(Position()) - k[1])
        xSize = k[0].x if k[0].x > xSize else xSize
        ySize = k[0].y if k[0].y > ySize else ySize
        zSize = k[0].z if k[0].z > zSize else zSize

    for k in arange(0, xSize, .1):
        for l in arange(0, ySize, .1):
            for m in arange(0, zSize, .1):
                d = .0
                for n in data:
                    d += abs(n[0].distanceTo(Position(k, l, m)) - n[1])
                if d < minDist:
                    minDist = d
                    minLoc = Position(k, l, m)

    return minLoc, minDist
