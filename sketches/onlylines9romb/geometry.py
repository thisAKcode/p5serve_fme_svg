import fmeobjects
import numpy as np
from fmeobjects import FMELine, FMEPoint
from math import sqrt, sin, cos, pi

width = 360
N = 1
d = width / N

class FeatureProcessor(object):
    def __init__(self):
        pass

    def draw_uptriangle(self, tx, ty):
        corner = 3
        _center_point = FMEPoint()
        _center_point.setXYZ(float(tx), float(ty), 0)
        _points = []
        _lines = []
        angle_offset = pi / 3
        for i in range(corner):
            angle = 2 * pi * i / corner + angle_offset
            x2 = float(tx) + sin(angle) * 30
            y2 = float(ty) + cos(angle) * 30
            next_point = FMEPoint()
            next_point.setXYZ(x2, y2, 0)
            _points.append(next_point)
            line = FMELine()
            line.appendPoint(_center_point)
            line.appendPoint(next_point)
            _lines.append(line)
            _points.append(_center_point)

        return _points, _lines

    def pattern(self, size):
        l = size / sqrt(4)
        points = []
        lines = []
        for j in range(10):
            for i in range(10):
                if j % 2 == 0:
                    dx = 0
                else:
                    dx = sqrt(3) * 15
                up_triangle_points, uplines = self.draw_uptriangle(i * sqrt(3) * 30 - dx, j * 45)
                points.extend(up_triangle_points)
                lines.extend(uplines)

        for i in points:
            newFeature = fmeobjects.FMEFeature()
            newFeature.setGeometry(i)
            self.pyoutput(newFeature)
        for i in lines:
            newFeature = fmeobjects.FMEFeature()
            newFeature.setGeometry(i)
            self.pyoutput(newFeature)

        return points
    def input(self, feature: fmeobjects.FMEFeature):
        # svg_body = create_svg_no_deps(datastructure,'foo')
        pass
    def close(self):
        points = self.pattern(d)

    def pyoutput(self, feature):
        # Placeholder for the actual output method
        pass
