from lateration import NLateration, Position


def main():
    InputData = [(Position(0.5, 0.5, 0.5), 3.0),
                 (Position(4.0, 0.0, 0.0), 2.0),
                 (Position(4.0, 5.0, 5.0), 4.2),
                 (Position(3.0, 3.0, 3.0), 2.5)]
    Nlat = NLateration(InputData)
    print("Computed location : " + Nlat[0].toString())
    print("With distance = " + str(round(Nlat[1], 2)) + " m")


if __name__ == '__main__':
    main()
