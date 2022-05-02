from math import floor


class Location:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, loc2):
        return bool(self.x == loc2.x and self.y == loc2.y and self.z == loc2.z)

    def __mul__(self, multiplier):
        returnValue = Location(self.x, self.y, self.z)
        returnValue.x *= multiplier
        returnValue.y *= multiplier
        returnValue.z *= multiplier
        return returnValue

    def __rmul__(self, multiplier):
        return self * multiplier

    def __add__(self, added):
        returnValue = Location(self.x, self.y, self.z)
        returnValue.x += added.x
        returnValue.y += added.y
        returnValue.z += added.z
        return returnValue

    def __isub__(self, value):
        return self + -1 * value

    @staticmethod
    def fromID(origin_id, arraySize=3):
        origin_id -= 1
        y = origin_id % 3
        x = floor((origin_id - y) / 3)
        returnValue = Location(x, y)
        returnValue *= 2
        returnValue += Location(1, 1)
        returnValue *= 2
        return returnValue

    def toString(self):
        return "(" + str(self.x) + " ; " + str(self.y) + " ; " + str(self.z) + ")"


class RSSVector:
    distances = []

    def __init__(self, n1, n2, n3, n4):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4


class Cell:
    def __init__(self, v_, loc):
        self.v = v_
        self.location = loc


def newCell(n1, n2, n3, n4, l1, l2):
    return Cell(RSSVector(n1, n2, n3, n4), Location(l1, l2))


class MarkovValue:
    def __init__(self, nb=0, percentage=0.0):
        self.nb = nb
        self.percentage = percentage


class MarkovModel:
    def __init__(self, cells):
        self.MarkovValues = []
        self.cells = cells
        self.previousCell = 0
        for i in range(0, 11):
            self.MarkovValues.append([])
            for _ in range(0, 10):
                self.MarkovValues[i].append(MarkovValue())
        self.MarkovValues[10][0].nb = 1

    def moveToCellID(self, nextCell):
        self.MarkovValues[nextCell][self.previousCell].nb += 1
        self.MarkovValues[10][nextCell].nb += 1
        self.refreshPercentage(self.previousCell)
        self.previousCell = nextCell

    def moveToCell(self, nextCell):
        self.moveToCellID(nextCell.location.getPositionInArray() + 1)

    def refreshPercentage(self, col):
        if self.MarkovValues[10][col].nb:
            for k in range(0, 10):
                self.MarkovValues[k][col].percentage = self.MarkovValues[k][col].nb / self.MarkovValues[10][col].nb

    def printValues(self):
        print("\t? \t1 \t2 \t3\t4 \t5 \t6 \t7 \t8 \t9")
        print("---------------------------------------------------------------------------------", end='')

        for i in range(0, 11):
            print("\r\n", end='')
            if i == 10 or i == 1:
                print("---------------------------------------------------------------------------------\r\n", end='')

            print(i, end='\t')
            for k in range(0, 10):
                if not self.MarkovValues[i][k].nb:
                    print("", end='')
                else:
                    print("", end='')
                print(self.MarkovValues[i][k].nb, end='\t')
                print("", end='')
        print("")

    def printPercentages(self):
        print("\t? \t1 \t2 \t3\t4 \t5 \t6 \t7 \t8 \t9")
        print("---------------------------------------------------------------------------------", end='')

        for i in range(1, 10):
            print("\r\n", i, end='\t')
            for k in range(0, 10):
                if not self.MarkovValues[i][k].percentage:
                    print("", end='')
                elif k != self.previousCell or self.getMostLikely() != i:
                    print("", end='')
                else:
                    print("", end='')
                print(str(floor(self.MarkovValues[i][k].percentage * 100)), end='%')
                print("\t", end='')
        print("")

    def getMostLikely(self):
        return self.getMostLikelyFromCell(self.previousCell)

    def getMostLikelyFromCell(self, currentCell):
        max_value = 0
        max_id = 0
        for k in range(1, 10):
            if self.MarkovValues[k][currentCell].nb > max_value:
                max_value = self.MarkovValues[k][currentCell].nb
                max_id = k
        return max_id

    def path(self, locationIDs):
        for loc in locationIDs:
            self.moveToCellID(loc)
