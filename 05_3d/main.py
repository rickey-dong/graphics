from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 255 ]
edges = []
transform = new_matrix()


parse_file( 'face_script', edges, transform, screen, color )
# parse_file( 'gallery_1', edges, transform, screen, color )
