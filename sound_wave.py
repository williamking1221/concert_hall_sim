import numpy as np
from utils import Point, Line, intersection


class SoundParticle:

    def __init__(self, point, theta):
        self.tail = point
        self.r = 0
        self.theta = theta
        self.energy = 1        # Volume Percentage, reduces after every wall hit
        self.speed = 343       # meters per sec

    def move(self, room, dt):
        dist = self.speed * dt
        
        r = self.r + dist
        tip = Point(self.tail.x + r * np.cos(self.theta), self.tail.y + r * np.sin(self.theta))

        for edge in room.edges:
            intersection = intersection(self.tail, tip, edge[0], edge[1])
            if intersection:
                
            else:
                self.r = r