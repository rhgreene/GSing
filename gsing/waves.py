import math
from .utility import linear_map
from .channel import Wave


class SinWave(Wave):

    def get_sample(self):
        return math.sin(self.displacement)


class TriangleWave(Wave):

    def get_sample(self):
        if self.displacement < math.pi * 0.5:
            return (self.displacement / (math.pi * 0.5))
        elif self.displacement > math.pi * 1.5:
            return (self.displacement / (math.pi * 0.5)) - 4.0
        else:
            reverse = ((self.displacement - math.pi) * 2.0 / math.pi)
            return linear_map(reverse, 0.0, 1.0, 1.0, 0.0) - 1.0


class SquareWave(SinWave):

    def get_sample(self):
        y = super(SquareWave, self).get_sample()
        if y >= 0.0:
            return 1.0
        else:
            return -1.0


class SawWave(Wave):

    def get_sample(self):
        if self.displacement < math.pi:
            return (self.displacement / math.pi)
        else:
            return (self.displacement / math.pi) - 2
