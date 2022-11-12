from utils import Point


class People():

    def __init__(self, center_coord):
        self.center = Point(center_coord[0], center_coord[1])
        self.volumes = []
        self.lateral_vols = 0
        self.all_vols = 0

    def get_lateral_ratio(self):
        return self.lateral_vols / self.all_vols
