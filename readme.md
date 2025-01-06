# Purpose
Make FME workspaces with Python code easier to understand. Learn how to use the Python API for FME to automate the creation of data geometries such as points, lines, polygons, networks, solids, and surfaces.

### Language
the code is written in Python within pythoncaller transformer.

### Libraries Used

Three.js: For rendering 3D objects and exporting 2D SVG projection
D3.js: For rendering 2D SVG objects
P5.js: For rendering 2D SVG objects
FME: For creating geometries
pillow: For reading raster files
numpy: For creating arrays

### Instructions 
0. copy the 'blueprint' folder (last edited in the app folder) to the new folder
1. add .fmw file and add pythonCaller/pythonCreator transformer
2. write the code
3. run the workspace to write the svg file using fme writers
4. write down python code (run xmlparsing.py)
5. render svg along with code to illustrate use of python api for fme (pythoncaller).
6. make the code available to the public through githubpages using three.js,p5js, d3 etc.
