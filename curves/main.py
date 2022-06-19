from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 255, 0, 255 ]
edges = []
transform = new_matrix()

parse_file( 'script', edges, transform, screen, color )
# color = [0, 0, 0]
# parse_file('curve_stomp_script', edges, transform, screen, color)