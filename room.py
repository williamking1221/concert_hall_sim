import matplotlib.pyplot as plt
import numpy as np
import math

from utils import Point
from people import People
from sound_wave import SoundParticle
from sound_source import Source

class Room:

    def __init__(self, corners, materials, loc_source, loc_source_vols, loc_people):
        """
        Initializes corners, angles. Corners listed in a clockwise order. Angles is a list of angles in radians.
        Terms of angles are angles of line from corner[0] --> corner[1], corner[1] --> corner[2] ...,
        corner[len(corner)-1] --> corner[0]
        :param corners:
        """
        self.corners = corners
        self.materials = materials
        self.edges = []
        self.angles = []
        self.sources = []
        self.people = []
        self.rays = []

        for corner in corners:
            self.edges.append(Point(corner[0], corner[1]))

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

        for i in range(len(loc_source)):
            self.sources.append(Source(loc=loc_source[i], volume=loc_source_vols[i]))

        for i in range(len(loc_people)):
            self.people.append(People(center_coord=loc_people[i]))

    def plot_room(self):
        fig = plt.figure(num=1, clear=True)
        ax = fig.add_subplot(1,1,1)
        for i in range(len(self.corners)-1):
            xs = [self.corners[i][0], self.corners[i+1][0]]
            ys = [self.corners[i][1], self.corners[i+1][1]]
            ax.plot(xs, ys, 'b')
        ax.plot([self.corners[len(self.corners)-1][0], self.corners[0][0]],
                [self.corners[len(self.corners)-1][1], self.corners[0][1]], 'b')

        for i in range(len(self.people)):
            ax.plot(self.people[i].center.x, self.people[i].center.y, 'ko')

        for i in range(len(self.sources)):
            ax.plot(self.sources[i].loc.x, self.sources[i].loc.y, 'go')

        for i in range(len(self.rays)):
            ax.plot(self.rays[i].tail.x, self.rays[i].tail.y, 'r-')

        ax.set_xlim([-1, 6])
        ax.set_ylim([-1, 16])
        plt.show()

    def simulate(self, num_rays=10):
        time = 5                # seconds
        freq = 343             # freq of updates per second
        curr_step = 0
        while curr_step < (time * freq):
            if curr_step == 0:
                for i in range(len(self.sources)):
                    self.rays.append(self.sources[i].emit_sound(num_rays=num_rays))
            #room.plot_room()
            print(self.rays[i].tail.x, self.rays[i].tail.y)
            for i in range(len(self.rays)):
                self.rays[i].move(room, 1 / freq)
            curr_step += 1




if __name__ == "__main__":
    # room = Room(corners=[[0, 0], [-1, 15], [5, 12], [5, 1]],
    #             materials=[0.14, 0.15, 0.15, 0.14],
    #             loc_source=[[1, 1], [2, 1], [3, 1], [4, 1]],
    #             loc_source_vols=[100, 50, 50, 100],
    #             loc_people=[[x, y] for x in range(1, 5) for y in range(3, 12)])
    # room.plot_room()
    room = Room(corners=[[0, 0], [-1, 15], [5, 12], [5, 1]],
                materials=[0.14, 0.15, 0.15, 0.14],
                loc_source=[[1, 1]],
                loc_source_vols=[100],
                loc_people=[[1, 3]])
    room.simulate(num_rays=1)
    room.plot_room()
