# N-Lateration

import math
import numpy as np
import datetime

class Position:
    """
    Class representing a position in a 3D space
    """
    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getZ(self):
        return self.__z

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def setZ(self, z):
        self.__z = z

    def __str__(self):
        return f"X: { self.getX() } Y: { self.getY() } Z: { self.getZ() } "


class Emitter:
    """
    Class representing an emitter. It has a position and an id
    """
    def __init__(self, id, position):
        self.__id = id
        self.__position = position

    def getPosition(self):
        return self.__position

    def getID(self):
        return self.__id


class Receiver:
    """
    Class representing the device we want to locate. It has a position and a list of distances to each emitters
    """
    def __init__(self):
        self.__distanceToEmitter = {}
        self.__position = Position(0, 0, 0)

    def setDistance(self, emitter, distance):
        self.__distanceToEmitter[emitter] = distance

    def getDistance(self, emitter):
        return self.__distanceToEmitter[emitter]

    def getPosition(self):
        return self.__position

    def setPosition(self, position):
        self.__position = position

    def __str__(self):
        return "X: {:.2f} Y: {:.2f} Z: {:.2f} ".format(self.__position.getX(),self.__position.getY(),self.__position.getZ())


def distance(position1, position2):
    """
    Method that simply compute the euclidian distance between two positions
    """
    return math.sqrt(pow(position1.getX() - position2.getX(), 2)+pow(position1.getY() - position2.getY(), 2)+pow(position1.getZ() - position2.getZ(), 2))


def main():
    # Creating a receiver
    receiver = Receiver()
    
    # Creating 4 emitters according to the lab work subject
    emitter0 = Emitter(0, Position(0.5, 0.5, 0.5))
    emitter1 = Emitter(1, Position(4.0, 0.0, 0.0))
    emitter2 = Emitter(2, Position(4.0, 5.0, 5.0))
    emitter3 = Emitter(3, Position(3.0, 3.0, 3.0))
    
    # Putting the created emitters in a list to manipulate them more easily
    emitters = {emitter0, emitter1, emitter2, emitter3}

    # Registering in the receiver object all the distance to the previously created emitters
    receiver.setDistance(emitter0, 3)
    receiver.setDistance(emitter1, 2)
    receiver.setDistance(emitter2, 4.2)
    receiver.setDistance(emitter3, 2.5)
    
    # Init research space variable
    dMin = 0
    dMax = Position(0, 0, 0)
    
    # Establishing the research space
    # First we compute dMin, the basic sum of all distance to each emitter
    for emitter in emitters:
        dMin += abs(receiver.getDistance(emitter) -
                    distance(emitter.getPosition(), receiver.getPosition()))
        
        # Finding the upper bound of the research space by finding the most distant emitters
        if dMax.getX() < emitter.getPosition().getX():
            dMax.setX(emitter.getPosition().getX())
        if dMax.getY() < emitter.getPosition().getY():
            dMax.setY(emitter.getPosition().getY())
        if dMax.getZ() < emitter.getPosition().getZ():
            dMax.setZ(emitter.getPosition().getZ())

    print(f"dMin: {dMin}")
    print(f'dMax: {dMax}')
    
    # Then, we iterate through the research space on each dimension to minimize the sum of the distance
    pas = 0.1 # Setting the step to 0.1, that is computing the sum of distance each 0.1 unit
    for i in np.arange(pas, dMax.getX(), pas):
        for j in np.arange(pas, dMax.getY(), pas):
            for k in np.arange(pas, dMax.getZ(), pas):
                # At each point, we compute the sum of distance, so the value we want to minimize
                d = 0
                for emitter in emitters:
                    d += abs(receiver.getDistance(emitter) -
                             distance(emitter.getPosition(), Position(i, j, k)))
                    
                 # If the computed sum is lower than the previous one, we change the position of the receiver and
                # dMin take the value computed just before
                if d < dMin:
                    dMin = d
                    receiver.setPosition(Position(i, j, k))

    print(receiver)


if __name__ == "__main__":
    start_time = datetime.datetime.now() #Starting timer
    main() # Lauching main resolution script
    end_time = datetime.datetime.now() #Ending timer
    # Compute execution time to compare performances
    time_diff = (end_time - start_time)
    execution_time = time_diff.total_seconds() * 1000
    print("Execution time: {:.3f}".format(execution_time))
