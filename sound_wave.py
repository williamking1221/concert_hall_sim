import numpy as np
from utils import Point, intersection, reflect


class SoundParticle:

    def __init__(self, point, theta, volume):
        self.tail = point
        self.r = 0
        self.theta = theta
        self.volume = volume   # Volume reduces after every wall hit
        self.speed = 343       # meters per sec

    def move(self, room, dt):
        dist = self.speed * dt
        r = self.r + dist
        tip = Point(self.tail.x + r * np.cos(self.theta), self.tail.y + r * np.sin(self.theta))

        for i in range(len(room.edges)):
            if i != len(room.edges)-1:
                does_intersect, intersect = intersection(self.tail, tip, room.edges[i], room.edges[i+1])
            else:
                does_intersect, intersect = intersection(self.tail, tip, room.edges[i], room.edges[0])
            if does_intersect == True:
                self.volume *= room.materials[i]
                print('Intersection = ' + str(intersect.x) + ',' + str(intersect.y))
                dist_to_intersection = ((intersect.y - self.tail.y) ** 2 + (intersect.x - self.tail.x) ** 2) \
                                        ** 0.5
                if i != len(room.edges)-1:
                    self.theta = reflect(self.tail, tip,
                                        room.edges[i], room.edges[i+1])
                else:
                    self.theta = reflect(self.tail, tip,
                                        room.edges[i], room.edges[0])
                r = dist - dist_to_intersection
                tip = Point(self.tail.x + r * np.cos(self.theta), self.tail.y + r * np.sin(self.theta))
            # while intersect != False:
            #     print('Intersection = '+ str(intersect.x) + ',' + str(intersect.y))
            #     dist_to_intersection = ((intersect.y - self.tail.y) ** 2 + (intersect.x - self.tail.x) ** 2) \
            #                             ** 0.5
            #     if i != len(room.edges)-1:
            #         self.theta = reflect(self.tail, tip,
            #                             room.edges[i], room.edges[i+1])
            #     else:
            #         self.theta = reflect(self.tail, tip,
            #                             room.edges[i], room.edges[0])
            #     r = dist - dist_to_intersection
            #     tip = Point(self.tail.x + r * np.cos(self.theta), self.tail.y + r * np.sin(self.theta))
            #     if self.theta > 0:
            #         if i != len(room.edges) - 1:
            #             intersect = intersection(self.tail, tip, room.edges[i], room.edges[i+1])
            #             if intersect != False: self.volume *= room.materials[i]
            #         else:
            #             intersect = intersection(self.tail, tip, room.edges[i], room.edges[0])
            #             if intersect != False: self.volume *= room.materials[0]
            #     else:
            #         if i == 0:
            #             intersect = intersection(self.tail, tip, room.edges[len(room.edges)-1],
            #                                         room.edges[0])
            #         if intersect != False: self.volume *= room.materials[len(room.edges)-1]
            #         else:
            #             intersect = intersection(self.tail, tip, room.edges[i-1], room.edges[i])
            #             if intersect != False: self.volume *= room.materials[i-1]

        self.tail = tip

