from Makrov import MarkovModel, Location, newCell
from random import random
from math import floor

Tf = []

Tf = [[newCell(-38, -27, -54, -13, 2, 2), newCell(-74, -62, -48, -33, 2, 6), newCell(-13, -28, -12, -40, 2, 10)], \
      [newCell(-34, -27, -38, -41, 6, 2), newCell(-64, -48, -72, -35, 6, 6), newCell(-45, -37, -20, -15, 6, 10)], \
      [newCell(-17, -50, -44, -33, 10, 2), newCell(-27, -28, -32, -45, 10, 6), newCell(-30, -20, -60, -40, 10, 10)]]


def main():
    MM = MarkovModel(Tf)

    # small set fixed definition
    MM.path(
        [8, 7, 8, 7, 8, 7, 8, 5, 8, 2, 9, 8, 1, 9, 8, 9, 5, 4, 3, 2, 3, 2, 4, 5, 4, 5, 6, 6, 7, 6, 9, 5, 9, 3, 2, 4, 3,
         5, 3, 4, 3, 3, 5, 6, 7, 6, 7, 6, 5, 4, 3, 4, 3, 4])

    # larger set random generation
    for k in range(0, 100):
        MM.moveToCellID(floor(random() * 9 + 1))

    print("\r\n")
    MM.printValues()
    print("\r\nPERCENTAGES : \r\n")
    MM.printPercentages()

    print("\r\ncurrent cell is " + str(MM.previousCell))
    print("most likely next cell is " + str(MM.getMostLikely()))

    while 1:
        print("Input next location ID (between 1 and 9)\r\n>>", end='')
        in_char = int(input())
        if 0 < in_char < 10:
            MM.moveToCellID(in_char)
            MM.printValues()
            print("\r\nPERCENTAGES : \r\n")
            MM.printPercentages()
            print("\r\ncurrent cell is #" + str(
                MM.previousCell) + " , most likely next cell is " + str(
                MM.getMostLikely()) + "  which is located at " + str(
                Location.fromID(MM.getMostLikely()).toString()) + " ")
        else:
            print("invalid ID")
            break


if __name__ == '__main__':
    main()
