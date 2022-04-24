from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
zbuffer = new_zbuffer()
color = [ 0, 255, 0 ]
edges = []
polygons = []
t = new_matrix()
ident(t)
csystems = [ t ]


# parse_file( 'script', edges, polygons, csystems, screen, zbuffer, color )

draw_bottom_triangle((25, 400, 0), (50, 200, 0), (200, 200, 0), screen, zbuffer, color)
save_extension(screen, "test.png")