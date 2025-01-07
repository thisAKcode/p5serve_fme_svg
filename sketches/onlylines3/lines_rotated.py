import numpy as np
import random
import math
import matplotlib.pyplot as plt


def _polygon_maker(start_x, start_y, _length, num_pts):
    array_x, array_y = [],[]
    _lines = []
    for i in range(num_pts):
        TAU = 2 * math.pi
        angle = TAU / num_pts * i

        array_x.append(start_x + _length * math.cos(angle))
        array_y.append(start_y + _length * math.sin(angle))
   
    for i in range(num_pts):
        obj1 = [(array_x[i], array_y[i]), (array_x[(i+1) % num_pts], array_y[(i+1) % num_pts])]
        _lines.append(obj1)

    print(_lines)
_polygon_maker(0,0, 100, 3)