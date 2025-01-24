#main_script
import fme
import fmeobjects
import random
import numpy as np
from fmeobjects import FMELine, FMEGeometryTools
from math import sqrt, cos, sin, pi


width = 360
N = 8
d=width/N
        
def translate(points,x_diff, y_diff):
    # input list of lists 
    # with coordinates [[x0,y0][x1,y1][x2,y2]]
    # add diff values for each x and y 
    translated_coords = [(i[0] + x_diff, i[1] + y_diff)
    for i in points
    ]
    return translated_coords
  
    
    
class FeatureProcessor(object):
    

    def __init__(self):
        
        pass
    def pattern(self, x, y, size):
        """
        prepair a pattern consisting of two sets of triangles 
        at the specified position:
        x (float): The x-coordinate of the pattern's position.
        y (float): The y-coordinate of the pattern's position.
        size (float): The size of the pattern.
        The function calculates the points for two sets of 
        # triangles based on the given size.
        It then translates the drawing context to 
        # the specified (x, y) position and draws the triangles.
        """
        l = size / sqrt(4)
        points = []
        for i in range(4):
            r = 3 * pi / 3 * i + pi / 6
            points.append([l * cos(r), l * sin(r)])
        for i in range(4):
            r = 3 * pi / 3 * i + pi / 6 + pi
            points.append([l * cos(r), l * sin(r)])
        
        #move the current position to the given x and y values.
        x_start, y_start  = x, y + l / 2
        start_point = (float(x_start),float(y_start), 0)
        start_point_pt = fmeobjects.FMEPoint().setXYZ(float(x_start),float(y_start), 0)
        translated_points = translate(points,x_start, y_start)
        points = translated_points
        
        fme_points = []
        
        for i in translated_points:
            point = fmeobjects.FMEPoint()
            point.setXYZ(float(i[0]), float(i[1]), 0)
            fme_points.append(point)
        
        for i in range(len(fme_points) - 1):
            point1 = fme_points[i]
            point2 = fme_points[i + 1]
            point3 = start_point_pt

        for i in range(len(translated_points) - 1):
            points = [translated_points[i],translated_points[i+1],start_point]
            linefeature = fmeobjects.FMEFeature()
            line = FMELine(points) # init(points) (list[tuple[float]]) – The list of points to set to the line. The points are represented as (x, y) or (x, y, z) tuples
            linefeature.setGeometry(line)
            self.pyoutput(linefeature)
        
        return points 
    def input(self, feature: fmeobjects.FMEFeature):
        

        # svg_body = create_svg_no_deps(datastructure,'foo')
        pass

    def close(self):
        for i in range(2 * N + 1):
            x = d * i / 2
            dy = d * sqrt(3) / 2 if i % 2 == 1 else 0
            for j in range(N):
                y = d * j * sqrt(3)
                points = self.pattern(x, y + dy, d)
                pts_crd = [(i[0],i[1]) for i in points[0:2]]
                linefeature = fmeobjects.FMEFeature()
                line = FMELine(pts_crd) # init(points) (list[tuple[float]]) – The list of points to set to the line. The points are represented as (x, y) or (x, y, z) tuples
                linefeature.setGeometry(line)
                self.pyoutput(linefeature)
