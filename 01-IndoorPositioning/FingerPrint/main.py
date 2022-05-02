from Fingerprint import RSSVector, Location, newCell, KNeighbors

Tf = []
testSample = RSSVector(-26, -42, -13, -46)

Tf = [[newCell(-38, -27, -54, -13, 2, 2), newCell(-74, -62, -48, -33, 2, 6), newCell(-13, -28, -12, -40, 2, 10)],
      [newCell(-34, -27, -38, -41, 6, 2), newCell(-64, -48, -72, -35, 6, 6), newCell(-45, -37, -20, -15, 6, 10)],
      [newCell(-17, -50, -44, -33, 10, 2), newCell(-27, -28, -32, -45, 10, 6), newCell(-30, -20, -60, -40, 10, 10)]]


def main():
    print("\nK-neighbors of test sample : ")
    neighborsCells = KNeighbors(Tf, testSample)
    for k in neighborsCells:
        print("(x=", k.location.x, ";y=", k.location.y, ")")
        print("\nDistances : " + str(testSample.distances))


if __name__ == '__main__':
    main()
