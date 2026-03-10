import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches

let img; // Declare variable 'img'.
let pathCheck;
let palette = ["#D3BB99", "#6C6754", "#DD4622", "#5A1A0E", "#181310", "#F2EFE9"];
let palette2 = ["#90e0ef","#001219","#240046", "#edede9","#3a7ca5", "#33415c"];

let darkPalette = ["#001219", "#005f73", "#0a9396", "#240046", "#3d314a","#5A1A0E"];
let lightPalette = ["#f9ed69", "#f08a5d", "#b83b5e", "#6a2c70", "#94d2bd",  "#e9d8a6"];

let description = "I wanted to mix triangles with arcs."

// create class Tile that can be of following parameters 
// x, y, size, color, stroke, transparency, rotation, flipX, flipY

// as class instances
// of n types
// each jumping to x, y position
// each with a size of tile_size
// each with a color from the palette
// each with a stroke of 0
// each with variying transparency in range (0,35%, 70%)
// each (except square) with a random rotation of 0, 90, 180, 270 degrees
// each with a random flip in x or y
// each with a random flip in y and x (diagonal flip)
// class
from dataclasses import dataclass

@dataclass
class Tile:
  x: int
  y: int
  size: int
  color: str
  stroke: int
  transparency: float
  rotation: int
  flipX: bool
  flipY: bool

  def draw_arc_half_pi(self, ax):
    t = patches.Arc((self.x, self.y), self.size * 2, self.size * 2, angle=self.rotation, theta1=0, theta2=90, color=self.color, alpha=self.transparency)
    ax.add_patch(t)

  def draw_triangle(self, ax):
    triangle = patches.Polygon([(self.x, self.y), (self.x + self.size, self.y), (self.x, self.y + self.size)], closed=True, color=self.color, alpha=self.transparency)
    ax.add_patch(triangle)

  def draw(self, ax):
    if self.type == 'polygon':
      self.draw_arc_half_pi(ax)
    elif self.type == 'triangle':
      self.draw_triangle(ax)

def setup():
  fig, ax = plt.subplots()
  ax.set_aspect('equal')
  ax.set_xlim(0, 720)
  ax.set_ylim(0, 720)
  ax.set_facecolor('#006d77')
  return fig, ax

def draw(ax):
  gridSize = 4
  tileSize = 720 // gridSize
  palette = ["#D3BB99", "#6C6754", "#DD4622", "#5A1A0E", "#181310", "#F2EFE9"]
  palette2 = ["#90e0ef","#001219","#240046", "#edede9","#3a7ca5", "#33415c"]
  one_of_palettes = random.choice([palette, palette2])

  for i in range(gridSize):
    for j in range(gridSize):
      color = random.choice(one_of_palettes)
      transparency = random.choice([0.10, 0.25])
      rotation = random.choice([0, 90, 180, 270])
      flipX = random.choice([True, False])
      flipY = random.choice([True, False])

      tile = Tile(j * tileSize, i * tileSize, tileSize, color, 0, transparency, rotation, flipX, flipY)
      tile.type = random.choice(['polygon', 'triangle'])
      tile.draw(ax)

fig, ax = setup()
draw(ax)
plt.gca().invert_yaxis()
plt.show()

  for i in range(gridSize):
    for j in range(gridSize):
      # Randomly select color, transparency, rotation, flipX, and flipY
      color = random.choice(one_of_palettes)
      transparency = random.choice([0.10, 0.25])
      rotation = random.choice([0, 90, 180, 270])
      flipX = random.choice([True, False])
      flipY = random.choice([True, False])

      # Create an instance of Tile class
      tile = Tile(j * tileSize, i * tileSize, tileSize, color, 0, transparency, rotation, flipX, flipY)

      # Randomly assign type to tile
      tile.type = random.choice(['polygon', 'triangle'])

      # Render the tile
      tile.draw()