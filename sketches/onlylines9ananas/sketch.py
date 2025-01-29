import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_uptriangle(ax, tx, ty):
  corner = 3
  angle_offset = math.pi / 3
  points = []
  for i in range(corner):
    angle = 2 * math.pi * i / corner + angle_offset
    x = tx + math.sin(angle) * 30
    y = ty + math.cos(angle) * 30
    points.append((x, y))
  polygon = patches.Polygon(points, closed=True, fill=None, edgecolor='#da8d93', linewidth=3)
  ax.add_patch(polygon)

def draw_downtriangle(ax, tx, ty):
  corner = 3
  points = []
  for i in range(corner):
    angle = 2 * math.pi * i / corner
    x = tx + math.sin(angle) * 30
    y = ty + math.cos(angle) * 30
    points.append((x, y))
  polygon = patches.Polygon(points, closed=True, fill=None, edgecolor='#da8d93', linewidth=3)
  ax.add_patch(polygon)

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(0, 450)
ax.set_ylim(0, 400)
ax.set_facecolor('#e7acb9')

for j in range(10):
  for i in range(10):
    if j % 2 == 0:
      dx = 0
    else:
      dx = math.sqrt(3) * 15

    draw_uptriangle(ax, i * math.sqrt(3) * 30 - dx, j * 45)
    draw_downtriangle(ax, 15 * math.sqrt(3) + i * math.sqrt(3) * 30 - dx, -math.sqrt(3) * 10 + j * 45)

plt.gca().invert_yaxis()
plt.show()