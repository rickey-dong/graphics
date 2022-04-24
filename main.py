from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
zbuffer = new_zbuffer()
color = [ 255, 255, 0 ]
edges = []
polygons = []
t = new_matrix()
ident(t)
csystems = [ t ]


parse_file( 'script', edges, polygons, csystems, screen, zbuffer, color )