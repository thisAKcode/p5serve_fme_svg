import numpy as np
import random
import matplotlib.pyplot as plt


def gen2(repeat= 3):
    # recursive function
    initiator2 = "A" 
    generator2 = [ "F-[[A]+A]+F[+FA]-A" , "F[+A]F[-A]A" , "F[+[FA[-A]F]][-A]FA" ]
    generator_way2 = []
    
    for i in range(repeat):
        _com = []
        for k in initiator2:
            if k == "F":
                _com.append("FF")
            elif k == "A":
                _com.append(random.choice(generator2))
            else:
                _com.append(k)
            initiator2 = "".join(_com)
    return initiator2
foo = gen2(3)
generator_rand = {"A":foo}


import pdb; pdb.set_trace()

print(gen2)
generators = [{"F": "FB", "A": "F-[[A]+A]+F[+FA]-A", "B": "+F[+FA]-A"},
              {"F": "FF", "A": "F-[[A]+A]+F[+FA]-A"},
              {"F": "F+[[B]-B]-F[-FB]+B)", "A": "BA"}]
 
# global variables goes here
state = [[4, 1], np.pi / 2]  # Initial starting point and initial direction(in radians) of turtle
initiator = "A"
com = initiator
generator = random.choice(generators)
generator 
angle = 22.5 / 180 * np.pi  # Rotation angle degrees -> radians
drawcolor = 'green'
repeat = 4
distance = 2 * (1 / 2) ** repeat  # Length of one step. Change according to the object
# call stack is used to store the state of the turtle when encountering the `[` command 
# and to restore it when encountering the `]` command in order to 
# to remember its position and direction at certain points, enabling it to return to those points later.


stack = []
datastructure = []


# Move pointer froward  without drawing
# and memorize the state 
def move_pointer(state):
    th = state[1]
    x = state[0][0] + distance * np.cos(th)
    y = state[0][1] + distance * np.sin(th)
    return [[x, y], th]


# Move forward by distance and draw
def forward(state):
    
    th = state[1]
    x1 = state[0][0]
    y1 = state[0][1]
    x2 = x1 + distance * np.cos(th)
    y2 = y1 + distance * np.sin(th)
    datastructure.append([[x1, y1], [x2, y2]])
    return [[x2, y2], th]


# Change direction coef 1/0 left/right
def rotate(coef, state):
    th = state[1]
    th = th + coef * angle
    return [state[0], th]


def turtle(command, state):
# Move the turtle according to the command L, R do nothing, return the state of the turtle
# When the turtle encounters `[`, it saves the current state (position and direction) onto the stack.
#  When the turtle encounters `]`, it pops the last saved state from the stack and restores it.
# This mechanism is essential for generating branching structures in L-systems, where the turtle needs to backtrack to previous positions to create branches.
    if command == "A" or command == "B" or command == "F":
        state = forward(state)
    if command == "f":
        state = move_pointer(state)
    if command == "+":
        state = rotate(1, state)
    if command == "-":
        state = rotate(-1, state)
    if command == "[":
        stack.append(state)
    if command == "]":
        state = stack.pop()
    return state


def _main():
    """ main calls 
    str.maketrans(generator)
    com.translate(...)
    for command in com: 
    turtle(command, state)   where for each command you call:
    forward(state)|     move_pointer(state)|     rotate(coef, state)|     stack.append(state)|     stack.pop()     

This sequence ensures that the turtle graphics are generated according to the L
system rules defined by the    generator  
    """ 
    global state, com, datastructure
    for i in range(repeat):
        com = com.translate(str.maketrans(generator))
    
    for command in com:
        state = turtle(command, state)
    
    return datastructure

datastructure = _main()


def create_svg_no_deps(data, filename):
    # Find the maximum and minimum x and y values to scale the canvas
    min_x = np.min([line[0][0] for line in data] + [line[1][0] for line in data])
    max_x = np.max([line[0][0] for line in data] + [line[1][0] for line in data])
    min_y = np.min([line[0][1] for line in data] + [line[1][1] for line in data])
    max_y = np.max([line[0][1] for line in data] + [line[1][1] for line in data])

    # Define the size of the canvas
    canvas_width = (max_x - min_x)*50
    canvas_height = (max_y - min_y)*50

    # Calculate the scale factors
    scale_x = canvas_width / (max_x - min_x)
    scale_y = canvas_height / (max_y - min_y)

    svg_content = f'<svg viewBox=" {min_x} {min_y} {canvas_width} {canvas_height} 1" xmlns="http://www.w3.org/2000/svg" version="1.1" width="{canvas_width}" height="{canvas_height}">\n'
    for line in data:
        start, end = line
        # Scale and invert the y-axis by subtracting y values from max_y
        x1 = (start[0] - min_x) * scale_x
        y1 = canvas_height - (start[1] - min_y) * scale_y
        x2 = (end[0] - min_x) * scale_x
        y2 = canvas_height - (end[1] - min_y) * scale_y
        svg_content += f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="rgb(10%,10%,16%)" stroke-width="0.1" />\n'
    svg_content += '</svg>'

    with open(filename, 'w') as f:
        f.write(svg_content)

create_svg_no_deps(datastructure, 'output_no_deps.svg')
