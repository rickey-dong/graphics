# Graphics Final Project
### Names: Ryan Poon and Rickey Dong
### Class Period: 4
---
## New Graphics Engine Features
- Basic anti-aliasing
- Phong shading

---
## The Details
- Anti-aliasing
    - Implement Xiaolin Wu's line drawing algorithm. Create additional MDL "aaline" command to draw an anti-aliased line. Bresenham's algorithm will still be used for scanline conversion and zbuffer. Xiaolin Wu's algorithm will be used just to draw lines, not filling polygons.
- Phong shading
    - Implement shading MDL command to toggle between "phong" and "flat" shading models
---
## Instructions
Examples:
- ```make```
    - generates image (test.png) comparing the line algorithms, flat shading, and phong shading
- ```make cube```
    - generates gif (cube_spin.gif) of spinning cube using phong shading

Relevant MDL commands: aa_line and shading
- aa_line
    - Takes in arguments: x0, y0, z0, x1, y1, z1 but NOTE: does not take into z-values into account; the default z value used is always 0
    - otherwise, can be used the same as "line" command
    - Example use: `aa_line 0 0 0 250 -500 0`
- shading
    - Takes in an argument: either flat or phong
    - Example use: `shading phong`
