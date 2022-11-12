import numpy as np
from room import Room


class SoundParticle():

    def __init__(self, loc=[0, 0], angle=90):
        self.loc = [loc[0], loc[1]]     # 2D List of x,y location
        self.angle = angle*np.pi/2      # Angle with respect to positive x-axis, CCW positive, in rad
        self.volumePercent = 1          # Volume Percentage, reduces after every wall hit
        self.speed = 343                # meters per sec

    def move(self, room, dt):
        tot_dist = self.speed * dt
        dx = np.cos(self.angle) * tot_dist
        dy = np.sin(self.angle) * tot_dist
        suggested_next_loc = [self.loc[0] + dx, self.loc[1] + dy]

    #Static
    def check_hit_wall(next_loc, room):
        if room.left_angle < np.pi/2:
            if next_loc[1] > room.bottom_y_limits[0] + np.cos(room.left_angle) * (next_loc[0] - room.bottom_y_limits[0]):



if __name__ == "__main__":
    room = Room()