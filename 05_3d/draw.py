from display import *
from matrix import *

  # ====================
  # add the points for a rectagular prism whose 
  # upper-left corner is (x, y, z) with width, 
  # height and depth dimensions.
  # ====================
def add_box( points, x, y, z, width, height, depth ):
    points.append([x, y, z, 1])
    points.append([x + width, y, z, 1])

    points.append([x, y, z, 1])
    points.append([x, y - height, z, 1])

    points.append([x, y - height, z, 1])
    points.append([x + width, y - height, z, 1])

    points.append([x + width, y - height, z, 1])
    points.append([x + width, y, z, 1])

    points.append([x, y - height, z, 1])
    points.append([x, y - height, z - depth, 1])
    
    points.append([x + width, y - height, z, 1])
    points.append([x + width, y - height, z - depth, 1])

    points.append([x + width, y, z, 1])
    points.append([x + width, y, z - depth, 1])
    
    points.append([x, y, z, 1])
    points.append([x, y, z - depth, 1])

    points.append([x, y, z - depth, 1])
    points.append([x, y - height, z - depth, 1])

    points.append([x, y, z - depth, 1])
    points.append([x + width, y, z - depth, 1])
    
    points.append([x, y - height, z - depth, 1])
    points.append([x + width, y - height, z - depth, 1])

    points.append([x + width, y - height, z - depth, 1])
    points.append([x + width, y, z - depth, 1])

  # ====================
  # Generates all the points along the surface
  # of a sphere with center (cx, cy, cz) and
  # radius r.
  # Returns a matrix of those points
  # ====================
def generate_sphere( points, cx, cy, cz, r, step ):
    generated_points = []
    rotation = 0
    while rotation < 1:
        circle = 0
        while circle < 1:
            x = r * math.cos(math.pi * circle) + cx
            y = r * math.sin(math.pi * circle) * math.cos((math.pi * 2) * rotation) + cy
            z = r * math.sin(math.pi * circle) * math.sin((math.pi * 2) * rotation) + cz
            generated_points.append([x, y, z, 1])
            generated_points.append([x+1, y, z, 1]) # just a pixel away from it to make it like dots
            circle += step
        rotation += step
    return generated_points

  # ====================
  # adds all the points for a sphere with center 
  # (cx, cy, cz) and radius r to points
  # should call generate_sphere to create the
  # necessary points
  # ====================
def add_sphere( points, cx, cy, cz, r, step ):
    g_p = generate_sphere(points, cx, cy, cz, r, step)
    for sphere_point in g_p:
        points.append(sphere_point)


  # ====================
  # Generates all the points along the surface
  # of a torus with center (cx, cy, cz) and
  # radii r0 and r1.
  # Returns a matrix of those points
  # ====================
def generate_torus( points, cx, cy, cz, r0, r1, step ):
    r = r0
    R = r1
    generated_points = []
    phi = 0
    while phi < 1:
        theta = 0
        while theta < 1:
            x = (math.cos((math.pi * 2) * phi)) * ((r * math.cos((math.pi * 2) * theta) + R)) + cx
            y = (r * math.sin((math.pi * 2) * theta)) + cy
            z = ((-1) * math.sin((math.pi * 2) * phi)) * (r * math.cos((math.pi * 2) * theta) + R) + cz
            generated_points.append([x, y, z, 1])
            generated_points.append([x+1, y, z, 1]) # just a pixel away from it to make it like dots
            theta += step
        phi += step
    return generated_points

  # ====================
  # adds all the points for a torus with center
  # (cx, cy, cz) and radii r0, r1 to points
  # should call generate_torus to create the
  # necessary points
  # ====================
def add_torus( points, cx, cy, cz, r0, r1, step ):
    g_p = generate_torus(points, cx, cy, cz, r0, r1, step)
    for torus_point in g_p:
        points.append(torus_point)

def add_circle( points, cx, cy, cz, r, step ):
    pass

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
    pass


def draw_lines( matrix, screen, color ):
    if len(matrix) < 2:
        print('Need at least 2 points to draw')
        return

    point = 0
    while point < len(matrix) - 1:
        draw_line( int(matrix[point][0]),
                   int(matrix[point][1]),
                   int(matrix[point+1][0]),
                   int(matrix[point+1][1]),
                   screen, color)    
        point+= 2
        
def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)
    
def add_point( matrix, x, y, z=0 ):
    matrix.append( [x, y, z, 1] )
    



def draw_line( x0, y0, x1, y1, screen, color ):
    x0 = int(x0)
    y0 = int(y0)
    x1 = int(x1)
    y1 = int(y1)
    #swap points if going right -> left
    if x0 > x1:
        xt = x0
        yt = y0
        x0 = x1
        y0 = y1
        x1 = xt
        y1 = yt

    x = x0
    y = y0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)

    #octants 1 and 8
    if ( abs(x1-x0) >= abs(y1 - y0) ):

        #octant 1
        if A > 0:            
            d = A + B/2

            while x < x1:
                plot(screen, color, x, y)
                if d > 0:
                    y+= 1
                    d+= B
                x+= 1
                d+= A
            #end octant 1 while
            plot(screen, color, x1, y1)
        #end octant 1

        #octant 8
        else:
            d = A - B/2

            while x < x1:
                plot(screen, color, x, y)
                if d < 0:
                    y-= 1
                    d-= B
                x+= 1
                d+= A
            #end octant 8 while
            plot(screen, color, x1, y1)
        #end octant 8
    #end octants 1 and 8

    #octants 2 and 7
    else:
        #octant 2
        if A > 0:
            d = A/2 + B

            while y < y1:
                plot(screen, color, x, y)
                if d < 0:
                    x+= 1
                    d+= A
                y+= 1
                d+= B
            #end octant 2 while
            plot(screen, color, x1, y1)
        #end octant 2

        #octant 7
        else:
            d = A/2 - B;

            while y > y1:
                plot(screen, color, x, y)
                if d > 0:
                    x+= 1
                    d+= A
                y-= 1
                d-= B
            #end octant 7 while
            plot(screen, color, x1, y1)
        #end octant 7
    #end octants 2 and 7
#end draw_line
