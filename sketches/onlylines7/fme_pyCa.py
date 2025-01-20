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

class CustomPolygon(fmeobjects.FMEPolygon):
    """
    A custom polygon class that extends the FMEPolygon class.
    """
        """
        Initializes a new instance of the CustomPolygon class.
        """
        """
        Adds a triangular part to the polygon using the provided coordinates.
        Args:
            x1 (float): The x-coordinate of the first vertex.
            y1 (float): The y-coordinate of the first vertex.
            x2 (float): The x-coordinate of the second vertex.
            y2 (float): The y-coordinate of the second vertex.
            x3 (float): The x-coordinate of the third vertex.
            y3 (float): The y-coordinate of the third vertex.
        """
    def __init__(self):
        super().__init__()

    def triangle(self, x1, y1, x2, y2, x3, y3):
        coords = [(x1, y1), (x2, y2), (x3, y3)]
        self.addPart(FMELine(coords))
def pattern(x, y, size):
    """
    prepair a pattern consisting of two sets of triangles 
    at the specified position:
    x (float): The x-coordinate of the pattern's position.
    y (float): The y-coordinate of the pattern's position.
    size (float): The size of the pattern.
    The function calculates the points for two sets of triangles based on the given size.
    It then translates the drawing context to the specified (x, y) position and draws the triangles.
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
    # by * [(1,2),(3,4),(5,6)...] you unpack the subelements of first element,
    # and subelements of second element
    # i would like to create a class that inherits the properties of  fmeobjects.FMEPolygon
    # and then use the triangle method of it  to create the triangles


    polygon = CustomPolygon()
    polygon.triangle(*points[0], *points[1], x_start, y_start)
    polygon.triangle(*points[1], *points[2], x_start, y_start)
    polygon.triangle(*points[2], *points[0], x_start, y_start)

    polygon.triangle(*points[3], *points[4], x_start, y_start)
    polygon.triangle(*points[4], *points[5], x_start, y_start)
    polygon.triangle(*points[5], *points[3], x_start, y_start)
    triangle(*points[1], *points[2], x_start, y_start)
    triangle(*points[2], *points[0], x_start, y_start)
    
    triangle(*points[3], *points[4], x_start, y_start)
    triangle(*points[4], *points[5], x_start, y_start)
    triangle(*points[5], *points[3], x_start, y_start)
   
class FeatureProcessor(object):
    

    def __init__(self):
        
        pass
  
    def input(self, feature: fmeobjects.FMEFeature):
        

        # svg_body = create_svg_no_deps(datastructure,'foo')
        """
        _lines = _main()
        for i in _lines:
            # i being [[4, 1], [4.0, 1.125]] 
            # i can make a fme line
            coords = [tuple(sublist) for sublist in i]
            feature.setAttribute('i', 'yo')
            line = FMELine(coords)
            feature.setGeometry(line)
            self.pyoutput(feature)
        """
    def close(self):
        for i in range(2 * N + 1):
            x = d * i / 2
            dy = d * sqrt(3) / 2 if i % 2 == 1 else 0
            for j in range(N):
                y = d * j * sqrt(3)
                #push()
                #translate(x, y + dy)
                pattern(0, 0, d)
                #pop()

    
    