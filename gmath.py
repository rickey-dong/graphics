import math
from display import *


  # IMPORANT NOTE

  # Ambient light is represeneted by a color value

  # Point light sources are 2D arrays of doubles.
  #      - The fist index (LOCATION) represents the vector to the light.
  #      - The second index (COLOR) represents the color.

  # Reflection constants (ka, kd, ks) are represened as arrays of
  # doubles (red, green, blue)

AMBIENT = 0
DIFFUSE = 1
SPECULAR = 2
LOCATION = 0
COLOR = 1
SPECULAR_EXP = 4
RED = 0
GREEN = 1
BLUE = 2

#lighting functions
def get_lighting(normal, view, ambient, light, areflect, dreflect, sreflect ):
    return [0, 0, 0]

def calculate_ambient(alight, areflect):
    I_r = alight[RED] * areflect[RED]
    I_g = alight[GREEN] * areflect[GREEN]
    I_b = alight[BLUE] * areflect[BLUE]
    
    limit_color(I_r)
    limit_color(I_g)
    limit_color(I_b)

    return [I_r, I_g, I_b]

def calculate_diffuse(point_light, dreflect, normal):

    normalized_normal = normal[:]
    normalize(normalized_normal)

    normalized_L = point_light[LOCATION][:]
    normalize(normalized_L)

    I_r = point_light[COLOR][RED] * dreflect[RED] * \
    ( dot_product( normalized_normal, normalized_L) )
    I_g = point_light[COLOR][GREEN] * dreflect[GREEN] * \
    ( dot_product( normalized_normal, normalized_L) )
    I_b = point_light[COLOR][BLUE] * dreflect[BLUE] * \
    ( dot_product( normalized_normal, normalized_L) )

    limit_color(I_r)
    limit_color(I_g)
    limit_color(I_b)

    return [I_r, I_g, I_b]

def calculate_specular(point_light, sreflect, view, normal):
    pass

def limit_color(color):
    if color > 255 or color < 0:
        if color > 255:
            color = 255
        else:
            color = 0

#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    magnitude = math.sqrt( vector[0] * vector[0] +
                           vector[1] * vector[1] +
                           vector[2] * vector[2] )
    for i in range(3):
        vector[i] = vector[i] / magnitude

#Return the dot porduct of a . b
def dot_product(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):

    A = [0, 0, 0]
    B = [0, 0, 0]
    N = [0, 0, 0]

    A[0] = polygons[i+1][0] - polygons[i][0]
    A[1] = polygons[i+1][1] - polygons[i][1]
    A[2] = polygons[i+1][2] - polygons[i][2]

    B[0] = polygons[i+2][0] - polygons[i][0]
    B[1] = polygons[i+2][1] - polygons[i][1]
    B[2] = polygons[i+2][2] - polygons[i][2]

    N[0] = A[1] * B[2] - A[2] * B[1]
    N[1] = A[2] * B[0] - A[0] * B[2]
    N[2] = A[0] * B[1] - A[1] * B[0]

    return N
