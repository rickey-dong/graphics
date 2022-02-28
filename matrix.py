"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    # [ [x0, y0, z0, 1], [x1, y1, z1, 1], [x2, y2, z2, 1] ]
    string_representation = ""
    row = 0
    while row < 4:
        for point in range(len(matrix)):
            string_representation += str(matrix[point][row])
            if point != len(matrix) - 1:
                string_representation += " "
        string_representation += '\n'
        row += 1
    print(string_representation)

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if row == col:
                matrix[row][col] = 1
            else:
                matrix[row][col] = 0

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    product_matrix = []
    for matrix_col in range(len(m2)):
        product_matrix.append([])
        for matrix_row in range(len(m1[0])):
            value = 0
            m2_coefficients = m2[matrix_col][:]
            m1_coefficients = []
            for row in range(len(m1)):
                m1_coefficients.append(m1[row][matrix_row]) ###
            for element in range(len(m2_coefficients)):
                value += (m1_coefficients[element] * m2_coefficients[element])
            product_matrix[matrix_col].append(value)




def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
