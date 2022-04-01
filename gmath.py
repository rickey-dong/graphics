import math
from display import *



#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    pass

#Return the dot porduct of a . b
def dot_product(a, b):
    return (
        (a[0] * b[0]) +
        (a[1] * b[1]) +
        (a[2] * b[2])
    )

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):
    point_zero = polygons[i]
    point_one = polygons[i+1]
    point_two = polygons[i+2]

    vector_a = [
        point_one[0] - point_zero[0],
        point_one[1] - point_zero[1],
        point_one[2] - point_zero[2]
    ]
    vector_b = [
        point_two[0] - point_zero[0],
        point_two[1] - point_zero[1],
        point_two[2] - point_zero[2]
    ]

    normal_vector = [
        (vector_a[1] * vector_b[2]) - (vector_a[2] * vector_b[1]),
        (vector_a[2] * vector_b[0]) - (vector_a[0] * vector_b[2]),
        (vector_a[0] * vector_b[1]) - (vector_a[1] * vector_b[0])
    ]
    return normal_vector