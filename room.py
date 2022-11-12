import numpy as np
import math


class Room:

    def __init__(self, corners):
        """
        Initializes corners, angles. Corners listed in a clockwise order. Angles is a list of angles in radians.
        Terms of angles are angles of line from corner[0] --> corner[1], corner[1] --> corner[2] ...,
        corner[len(corner)-1] --> corner[0]
        :param corners:
        """
        self.corners = corners
        self.angles = []

        for i in range(len(corners)-1):
            if corners[i+1][0] - corners[i][0] == 0:
                if corners[i+1][1] < corners[i][1]:
                    angle = -np.pi/2
                else:
                    angle = np.pi/2
            else:
                angle = math.atan2((corners[i+1][1] - corners[i][1]), (corners[i+1][0] - corners[i][0]))
            self.angles.append(angle)

        if corners[len(corners)-1][1] == corners[0][1]:
            if corners[0][1] < corners[len(corners)-1][1]:
                self.corners.append(-np.pi/2)
            else:
                self.corners.append(np.pi/2)
        else:
            self.angles.append(math.atan2((corners[0][1] - corners[len(corners)-1][1]),
                                           (corners[0][0] - corners[len(corners)-1][0])))


if __name__ == "__main__":
    room = Room(corners=[[0,0],[-1,15],[5,12],[5,1]])