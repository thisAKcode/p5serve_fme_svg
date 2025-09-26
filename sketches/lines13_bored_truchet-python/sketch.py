#main_script
import fmeobjects
import random
import numpy as np
from fmeobjects import FMELine, FMEPoint, FMEPolygon
from math import sqrt, sin, cos, pi, degrees


width =  720 
draw_num = 4  # num circles per direction
draw_size = width / draw_num  # circle size
mark_num = 8  # number of circle duplicates 
mark_size = draw_size / mark_num

gridSize = 4
tileSize = width / gridSize


from dataclasses import dataclass

@dataclass
class Tile:
    x: int
    y: int
    size: int
    rotation: float
    flipX: bool
    flipY: bool
    type: str = 'polygon'  # Add default type
    
    
    def draw_arc_half_pi(self):
        _center_point = FMEPoint()
        newFeature= fmeobjects.FMEFeature()
        _center_point.setXYZ(self.x,self.y, 0)
        rotation = pi*2 / 5 * 2 + pi- pi / 10    
        newFeature= fmeobjects.FMEFeature()
        _arc = fmeobjects.FMEArc(_center_point, 0.0, self.size, self.size, 30.0, 120.0)
        _arc.rotate2D(_center_point, float(degrees(self.rotation)))
        newFeature.setGeometry(_arc)
        return newFeature
        # self.pyoutput(newFeature)

    def draw_triangle(self):
        _center_point = FMEPoint()
        newFeature= fmeobjects.FMEFeature()
        _center_point.setXYZ(self.x, self.y, 0)  # Use self.x and self.y
        rotation = pi*2 / 5 * 2 + pi- pi / 10    
        newFeature= fmeobjects.FMEFeature()
        _arc = fmeobjects.FMEArc(_center_point, 0.0, self.size, self.size, 30.0, 120.0)
        _arc.rotate2D(_center_point, float(degrees(self.rotation)))
        newFeature.setGeometry(_arc)
        return newFeature
        # self.pyoutput(newFeature)

    def draw(self):
        if self.type == 'polygon':
            self.draw_arc_half_pi()
        elif self.type == 'triangle':
            self.draw_triangle()



class FeatureProcessor(object):
    def __init__(self):
        pass

    def geometry_group(self, tx, ty, radius): 

        _center_point = FMEPoint()
        
        newFeature= fmeobjects.FMEFeature()
        x = tx
        y = ty
        _center_point.setXYZ(x,y, 0)


        rotation = pi*2 / 5 * 2 + pi- pi / 10    
        newFeature= fmeobjects.FMEFeature()
        _arc = fmeobjects.FMEArc(_center_point, 0.0, radius, radius, 30.0, 120.0)
        _arc.rotate2D(_center_point, float(degrees(rotation)))
        newFeature.setGeometry(_arc)
        
        self.pyoutput(newFeature)
    
    
    def pattern(self, size):
        for j in range(4 * (draw_num + 1)):
            y = draw_size / 4 * j  # Move 0.25 of the size of the circle vertically 
            dx = draw_size / 2 if j % 2 == 1 else 0  # move 0.5 horisontally if vertical direction is odd
            for i in range(draw_num + 1):
                x = draw_size * i  # Move horizontally by one circle
                _start_x, _start_y = x + dx, y
                # time to break it and move to geometry group
                for k in range(mark_num):
                    radius=mark_size * (mark_num - k) / 2
                    self.geometry_group(_start_x, _start_y, radius)
        
        for i in range(gridSize):
            for j in range(gridSize):
              # Randomly select rotation
              '''
              rotation = random.choice([0, 90, 180, 270])
              flipX = random.choice([True, False])
              flipY = random.choice([True, False])
              tile = Tile(j * tileSize, i * tileSize, tileSize, rotation, flipX, flipY)
              tile.type = random.choice(['polygon', 'triangle'])
              tile.draw()        
              '''
    def input(self, feature: fmeobjects.FMEFeature):
        # svg_body = create_svg_no_deps(datastructure,'foo')
        pass

    def close(self):
        self.pattern(draw_size)

