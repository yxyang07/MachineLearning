# Fingerprinting

import math
import numpy as np
import datetime


class Position:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def __mul__(self, scalar):
        x = self.__x * scalar
        y = self.__y * scalar
        return Position(x, y)

    def __add__(self, other):
        x = self.__x + other.getX()
        y = self.__y + other.getY()
        return Position(x, y)

    def __floordiv__(self, scalar):
        return(Position(self.__x // scalar, self.__y // scalar))

    def __truediv__(self, scalar):
        return(Position(self.__x / scalar, self.__y / scalar))

    def __str__(self):
        return f"X: { self.getX() } Y: { self.getY() }"


class Cell:
    def __init__(self, position, rssi):
        self.__position = position
        self.__rssi = rssi

    def getRSSIList(self):
        return self.__rssi

    def getPosition(self):
        return self.__position

    def setPosition(self, position):
        self.__position = position

    def getSomme(self):
        powersomme = 0
        for power in self.__rssi:
            powersomme += power
        return powersomme

    def __str__(self):
        return f"X: { self.getPosition().getX() } Y: { self.getPosition().getY() } RSSI: {self.__rssi}"


class Mobile(Cell):
    def __init__(self, position, rssi):
        super().__init__(position, rssi)


class Grid:
    def __init__(self):
        self.__cells = []

    def addCell(self, cell):
        print(cell)
        self.__cells.append(cell)

    def getCells(self):
        return self.__cells

    def getCell(self, position):
        for cell in self.getCells():
            if cell.getPosition() == position:
                return cell

        return Position(0, 0)

    # Compute the K shortest cell and return them with their weight

    def getKShortest(self, k, terminalMobile):
        cellanddistances = dict()

        weight = []

        for cell in self.getCells():
            distance = 0
            # We compute the rssi difference (distance) and add them to a dictrionnary of : (distance, cell)
            for rssi1, rssi2 in zip(cell.getRSSIList(), terminalMobile.getRSSIList()):
                distance += abs(rssi1 - rssi2)
            cellanddistances[distance] = cell

        # We sort the distances from smaller to higher
        shortestdistance = list(cellanddistances.keys())
        shortestdistance.sort()

        kShortestreturn = []

        # We get the k shortest distances and get the corresponding cell
        for i in range(0, k):
            kShortestreturn.append(cellanddistances[shortestdistance[i]])
            weight.append(1/shortestdistance[i])

        return kShortestreturn, weight


def main():
    # We add all the cell with their position and RSSI values
    grid = Grid()
    grid.addCell(Cell(Position(0, 0), [-38, -27, -54, -13]))
    grid.addCell(Cell(Position(0, 1), [-74, -62, -48, -33]))
    grid.addCell(Cell(Position(0, 2), [-13, -28, -12, -40]))
    grid.addCell(Cell(Position(1, 0), [-34, -27, -38, -41]))
    grid.addCell(Cell(Position(1, 1), [-64, -48, -72, -35]))
    grid.addCell(Cell(Position(1, 2), [-45, -37, -20, -15]))
    grid.addCell(Cell(Position(2, 0), [-17, -50, -44, -33]))
    grid.addCell(Cell(Position(2, 1), [-27, -28, -32, -45]))
    grid.addCell(Cell(Position(2, 2), [-30, -20, -60, -40]))

    # The mobile terminal with his RSSIs
    terminalMobile = Mobile(Position(0, 0), [-26, -42, -13, -46])

    # We call the function getKShortest to get the K shortest cell from ou mobile terminal
    kshortest = grid.getKShortest(4, terminalMobile)
    # Kshortest also return the weight of each shortest cell
    weight = kshortest[1]

    center = Position(0, 0)

    print("")

    # We print the K shortest and multiply the coordinate by the weight
    for cell, weightvalue in zip(kshortest[0], weight):
        position = cell.getPosition()
        position.setX(position.getX()*4+2)
        position.setY(position.getY()*4+2)

        center += position * weightvalue
        print(f"Nearby K: {cell.getPosition()} weight: {weightvalue}")

        # We devide the coordinate by the sum of the weights
    print(f"\nUsing weighted KNN:\nGravity Center: {center/sum(weight)}")


if __name__ == "__main__":
    main()
