import numpy as np

from sound_wave import SoundParticle
from utils import Point


class Source():

    def __init__(self, loc, volume):
        """
        Initialize sound sources as points.
        :param locs: 2D List, gives the location [x,y]
        :param volume: Volume of person / source
        """
        self.loc = Point(loc[0], loc[1])
        self.sound_particles_emitted = []
        self.volume = volume

    def emit_sound(self, num_rays=10):
        if num_rays == 1:
            return SoundParticle(point = self.loc, theta=np.pi/2, volume=self.volume)
        if num_rays > 1:
            for k in range(num_rays):
                return SoundParticle(point = self.loc, theta=(np.pi/6 + 120*k/(num_rays-1)),
                                     volume=self.volumes)
