import matplotlib.pyplot as plt
import numpy as np

const w=720; //Canvas size
const draw_num = 4; // How many circles to place in one direction
const draw_size = w/draw_num; // Size of one circle
const mark_num = 8; // How many circles to draw per circle
const mark_size = draw_size/mark_num;
const set_color=["#4267D8", "#DDDeF1"]; // Specify two colors to draw

function setup() {
   createCanvas(w, w);
   noStroke();

   for(let j=0;j<4*(draw_num+1);j++){
      const y = draw_size/4 * j; // Move vertically by a quarter of the size of the circle
      const dx = (j%2==1) ? draw_size/2 : 0 ; // If the vertical direction is an odd number, move half a circle horizontally

      for(let i=0;i<draw_num+1;i++){
         const x = draw_size * i; // Move horizontally by one circle
         push();
         translate(x+dx, y);

         //One drawing
         for(let k=0;k<mark_num;k++){
          fill(set_color[k%2]); // Set two colors alternately
          circle(0, 0, mark_size * (mark_num-k)); // Draw the outer circle
         }

         pop();
      }
   }
}

w = 720  # Canvas size
draw_num = 4  # How many circles to place in one direction
draw_size = w / draw_num  # Size of one circle
mark_num = 8  # How many circles to draw per circle
mark_size = draw_size / mark_num
set_color = ["#4267D8", "#DDDeF1"]  # Specify two colors to draw

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(0, w)
ax.set_ylim(0, w)
ax.axis('off')

for j in range(4 * (draw_num + 1)):
    y = draw_size / 4 * j  # Move vertically by a quarter of the size of the circle
    dx = draw_size / 2 if j % 2 == 1 else 0  # If the vertical direction is odd, move 0.5 draw_size horizontally

    for i in range(draw_num + 1):
        x = draw_size * i  # Move horizontally by one circle

        for k in range(mark_num):
            circle = plt.Circle((x + dx, y), mark_size * (mark_num - k) / 2, color=set_color[k % 2], ec='none')
            ax.add_patch(circle)

plt.gca().invert_yaxis()
plt.show()