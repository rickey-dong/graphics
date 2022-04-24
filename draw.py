from display import *
from matrix import *
from gmath import *

def scanline_convert(polygons, i, screen, zbuffer, color_choice):
    """
    colors in the i'th polygon in the polygons list
    """
    x0 = polygons[i][0]
    y0 = polygons[i][1]
    z0 = polygons[i][2]

    x1 = polygons[i+1][0]
    y1 = polygons[i+1][1]
    z1 = polygons[i+1][2]

    x2 = polygons[i+2][0]
    y2 = polygons[i+2][1]
    z2 = polygons[i+2][2]

    if color_choice % 6 == 0: # color triangle with pink
        handle_triangle(x0, y0, z0, x1, y1, z1, x2, y2, z2, screen, zbuffer, [255, 192, 203])
    elif color_choice % 6 == 1: # color triangle with green
        handle_triangle(x0, y0, z0, x1, y1, z1, x2, y2, z2, screen, zbuffer, [127, 255, 0])
    elif color_choice % 6 == 2: # color triangle with blue
        handle_triangle(x0, y0, z0, x1, y1, z1, x2, y2, z2, screen, zbuffer, [70, 130, 180])
    elif color_choice % 6 == 3: # color triangle with gray
        handle_triangle(x0, y0, z0, x1, y1, z1, x2, y2, z2, screen, zbuffer, [220, 220, 220])
    elif color_choice % 6 == 4: # color triangle with brown
        handle_triangle(x0, y0, z0, x1, y1, z1, x2, y2, z2, screen, zbuffer, [165, 42, 42])
    else: # color triangle with purple
        handle_triangle(x0, y0, z0, x1, y1, z1, x2, y2, z2, screen, zbuffer, [128, 0, 128])

def handle_triangle(x0, y0, z0, x1, y1, z1, x2, y2, z2, screen, zbuffer, color):
    """
    handle all triangle cases
    """
    # find the top, middle, and bottom vertices and draw lines of that triangle
    point_A = (x0, y0, z0)
    point_B = (x1, y1, z1)
    point_C = (x2, y2, z2)
    ordered_y_vals = [y0, y1, y2]
    ordered_y_vals.sort()
    if y0 != y1 and y1 != y2 and y0 != y2: # normal triangle
        point_mappings = {
            y0: point_A,
            y1: point_B,
            y2: point_C
        }
        top = point_mappings[ordered_y_vals[2]]
        mid = point_mappings[ordered_y_vals[1]]
        bottom = point_mappings[ordered_y_vals[0]]
        draw_normal_triangle(top, mid, bottom, screen, zbuffer, color)
    else: # special triangle
        if ordered_y_vals[0] == ordered_y_vals[1]: # triangle with 2 bottom equals
            if ordered_y_vals[2] == point_A[1]:
                top = point_A
                if point_B[0] < point_C[0]:
                    mid = point_B
                    bottom = point_C
                else:
                    mid = point_C
                    bottom = point_B
            elif ordered_y_vals[2] == point_B[1]:
                top = point_B
                if point_A[0] < point_C[0]:
                    mid = point_A
                    bottom = point_C
                else:
                    mid = point_C
                    bottom = point_A
            else:
                top = point_C
                if point_A[0] < point_B[0]:
                    mid = point_A
                    bottom = point_B
                else:
                    mid = point_B
                    bottom = point_A
            draw_bottom_triangle(top, mid, bottom, screen, zbuffer, color)
        elif ordered_y_vals[1] == ordered_y_vals[2]: # triangle with 2 top equals
            if ordered_y_vals[0] == point_A[1]:
                bottom = point_A
                if point_B[0] < point_C[0]:
                    top = point_B
                    mid = point_C
                else:
                    top = point_C
                    mid = point_B
            elif ordered_y_vals[0] == point_B[1]:
                bottom = point_B
                if point_A[0] < point_C[0]:
                    top = point_A
                    mid = point_C
                else:
                    top = point_C
                    mid = point_A
            else:
                bottom = point_C
                if point_A[0] < point_B[0]:
                    top = point_A
                    mid = point_B
                else:
                    top = point_B
                    mid = point_A
            draw_top_triangle(top, mid, bottom, screen, zbuffer, color)

def draw_normal_triangle(t, m, b, screen, zbuffer, color):
    x0 = b[0]
    x1 = b[0]
    y = b[1]
    dx0 = (t[0] - b[0]) / (t[1] - b[1] + 1)
    dx1_default = (m[0] - b[0]) / (m[1] - b[1] + 1)
    dx1_other = (t[0] - m[0]) / (t[1] - m[1] + 1)
    changed_trajectory = False
    while y <= t[1]:
        draw_line(x0, y, 0, x1, y, 0, screen, zbuffer, color) # CHANGE Z VALUES LATER
        # update the endpoints
        x0 += dx0
        x1 += dx1_default
        y += 1
        # swap dx1 if changing direction
        if y >= m[1] and not changed_trajectory:
            dx1_default = dx1_other
            x1 = m[0]
            changed_trajectory = True

def draw_bottom_triangle(t, m, b, screen, zbuffer, color):
    x0 = m[0]
    x1 = b[0]
    y = m[1]
    dx0 = (t[0] - m[0]) / (t[1] - m[1] + 1)
    dx1 = (t[0] - b[0]) / (t[1] - b[1] + 1)
    while y <= t[1]:
        draw_line(x0, y, 0, x1, y, 0, screen, zbuffer, color) # CHANGE Z VALUES LATER
        x0 += dx0
        x1 += dx1
        y += 1

def draw_top_triangle(t, m, b, screen, zbuffer, color):
    x0 = b[0]
    x1 = b[0]
    y = b[1]
    dx0 = (t[0] - b[0]) / (t[1] - b[1] + 1)
    dx1 = (m[0] - b[0]) / (m[1] - b[1] + 1)
    while y <= t[1]:
        draw_line(x0, y, 0, x1, y, 0, screen, zbuffer, color) # CHANGE Z VALUES LATER
        x0 += dx0
        x1 += dx1
        y += 1

def add_polygon( polygons, x0, y0, z0, x1, y1, z1, x2, y2, z2 ):
    add_point(polygons, x0, y0, z0)
    add_point(polygons, x1, y1, z1)
    add_point(polygons, x2, y2, z2)

def draw_polygons( polygons, screen, zbuffer, color ):
    if len(polygons) < 2:
        print('Need at least 3 points to draw')
        return

    point = 0
    color_index = 0
    while point < len(polygons) - 2:

        normal = calculate_normal(polygons, point)[:]
        #print normal
        if normal[2] > 0:
            scanline_convert(polygons, point, screen, zbuffer, color_index)
            color_index += 1
        point+= 3


def add_box( polygons, x, y, z, width, height, depth ):
    x1 = x + width
    y1 = y - height
    z1 = z - depth

    #front
    add_polygon(polygons, x, y, z, x1, y1, z, x1, y, z)
    add_polygon(polygons, x, y, z, x, y1, z, x1, y1, z)

    #back
    add_polygon(polygons, x1, y, z1, x, y1, z1, x, y, z1)
    add_polygon(polygons, x1, y, z1, x1, y1, z1, x, y1, z1)

    #right side
    add_polygon(polygons, x1, y, z, x1, y1, z1, x1, y, z1)
    add_polygon(polygons, x1, y, z, x1, y1, z, x1, y1, z1)
    #left side
    add_polygon(polygons, x, y, z1, x, y1, z, x, y, z)
    add_polygon(polygons, x, y, z1, x, y1, z1, x, y1, z)

    #top
    add_polygon(polygons, x, y, z1, x1, y, z, x1, y, z1)
    add_polygon(polygons, x, y, z1, x, y, z, x1, y, z)
    #bottom
    add_polygon(polygons, x, y1, z, x1, y1, z1, x1, y1, z)
    add_polygon(polygons, x, y1, z, x, y1, z1, x1, y1, z1)

def add_sphere(polygons, cx, cy, cz, r, step ):
    points = generate_sphere(cx, cy, cz, r, step)

    lat_start = 0
    lat_stop = step
    longt_start = 0
    longt_stop = step

    step+= 1
    for lat in range(lat_start, lat_stop):
        for longt in range(longt_start, longt_stop):

            p0 = lat * step + longt
            p1 = p0+1
            p2 = (p1+step) % (step * (step-1))
            p3 = (p0+step) % (step * (step-1))

            if longt != step - 2:
                add_polygon( polygons, points[p0][0],
                             points[p0][1],
                             points[p0][2],
                             points[p1][0],
                             points[p1][1],
                             points[p1][2],
                             points[p2][0],
                             points[p2][1],
                             points[p2][2])
            if longt != 0:
                add_polygon( polygons, points[p0][0],
                             points[p0][1],
                             points[p0][2],
                             points[p2][0],
                             points[p2][1],
                             points[p2][2],
                             points[p3][0],
                             points[p3][1],
                             points[p3][2])


def generate_sphere( cx, cy, cz, r, step ):
    points = []

    rot_start = 0
    rot_stop = step
    circ_start = 0
    circ_stop = step

    for rotation in range(rot_start, rot_stop):
        rot = rotation/float(step)
        for circle in range(circ_start, circ_stop+1):
            circ = circle/float(step)

            x = r * math.cos(math.pi * circ) + cx
            y = r * math.sin(math.pi * circ) * math.cos(2*math.pi * rot) + cy
            z = r * math.sin(math.pi * circ) * math.sin(2*math.pi * rot) + cz

            points.append([x, y, z])
            #print 'rotation: %d\tcircle%d'%(rotation, circle)
    return points

def add_torus(polygons, cx, cy, cz, r0, r1, step ):
    points = generate_torus(cx, cy, cz, r0, r1, step)

    lat_start = 0
    lat_stop = step
    longt_start = 0
    longt_stop = step

    for lat in range(lat_start, lat_stop):
        for longt in range(longt_start, longt_stop):

            p0 = lat * step + longt;
            if (longt == (step - 1)):
                p1 = p0 - longt;
            else:
                p1 = p0 + 1;
            p2 = (p1 + step) % (step * step);
            p3 = (p0 + step) % (step * step);

            add_polygon(polygons,
                        points[p0][0],
                        points[p0][1],
                        points[p0][2],
                        points[p3][0],
                        points[p3][1],
                        points[p3][2],
                        points[p2][0],
                        points[p2][1],
                        points[p2][2] )
            add_polygon(polygons,
                        points[p0][0],
                        points[p0][1],
                        points[p0][2],
                        points[p2][0],
                        points[p2][1],
                        points[p2][2],
                        points[p1][0],
                        points[p1][1],
                        points[p1][2] )


def generate_torus( cx, cy, cz, r0, r1, step ):
    points = []
    rot_start = 0
    rot_stop = step
    circ_start = 0
    circ_stop = step

    for rotation in range(rot_start, rot_stop):
        rot = rotation/float(step)
        for circle in range(circ_start, circ_stop):
            circ = circle/float(step)

            x = math.cos(2*math.pi * rot) * (r0 * math.cos(2*math.pi * circ) + r1) + cx;
            y = r0 * math.sin(2*math.pi * circ) + cy;
            z = -1*math.sin(2*math.pi * rot) * (r0 * math.cos(2*math.pi * circ) + r1) + cz;

            points.append([x, y, z])
    return points


def add_circle( points, cx, cy, cz, r, step ):
    x0 = r + cx
    y0 = cy
    i = 1

    while i <= step:
        t = float(i)/step
        x1 = r * math.cos(2*math.pi * t) + cx;
        y1 = r * math.sin(2*math.pi * t) + cy;

        add_edge(points, x0, y0, cz, x1, y1, cz)
        x0 = x1
        y0 = y1
        i+= 1

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):

    xcoefs = generate_curve_coefs(x0, x1, x2, x3, curve_type)[0]
    ycoefs = generate_curve_coefs(y0, y1, y2, y3, curve_type)[0]

    i = 1
    while i <= step:
        t = float(i)/step
        x = t * (t * (xcoefs[0] * t + xcoefs[1]) + xcoefs[2]) + xcoefs[3]
        y = t * (t * (ycoefs[0] * t + ycoefs[1]) + ycoefs[2]) + ycoefs[3]
        #x = xcoefs[0] * t*t*t + xcoefs[1] * t*t + xcoefs[2] * t + xcoefs[3]
        #y = ycoefs[0] * t*t*t + ycoefs[1] * t*t + ycoefs[2] * t + ycoefs[3]

        add_edge(points, x0, y0, 0, x, y, 0)
        x0 = x
        y0 = y
        i+= 1


def draw_lines( matrix, screen, zbuffer, color ):
    if len(matrix) < 2:
        print('Need at least 2 points to draw')
        return

    point = 0
    while point < len(matrix) - 1:
        draw_line( int(matrix[point][0]),
                   int(matrix[point][1]),
                   matrix[point][2],
                   int(matrix[point+1][0]),
                   int(matrix[point+1][1]),
                   matrix[point+1][2],
                   screen, zbuffer, color)
        point+= 2

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)

def add_point( matrix, x, y, z=0 ):
    matrix.append( [x, y, z, 1] )



def draw_line( x0, y0, z0, x1, y1, z1, screen, zbuffer, color ):
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
    wide = False
    tall = False

    if ( abs(x1-x0) >= abs(y1 - y0) ): #octants 1/8
        wide = True
        loop_start = x
        loop_end = x1
        dx_east = dx_northeast = 1
        dy_east = 0
        d_east = A
        if ( A > 0 ): #octant 1
            d = A + B/2
            dy_northeast = 1
            d_northeast = A + B
        else: #octant 8
            d = A - B/2
            dy_northeast = -1
            d_northeast = A - B

    else: #octants 2/7
        tall = True
        dx_east = 0
        dx_northeast = 1
        if ( A > 0 ): #octant 2
            d = A/2 + B
            dy_east = dy_northeast = 1
            d_northeast = A + B
            d_east = B
            loop_start = y
            loop_end = y1
        else: #octant 7
            d = A/2 - B
            dy_east = dy_northeast = -1
            d_northeast = A - B
            d_east = -1 * B
            loop_start = y1
            loop_end = y

    while ( loop_start < loop_end ):
        plot( screen, zbuffer, color, x, y, 0 )
        if ( (wide and ((A > 0 and d > 0) or (A < 0 and d < 0))) or
             (tall and ((A > 0 and d < 0) or (A < 0 and d > 0 )))):

            x+= dx_northeast
            y+= dy_northeast
            d+= d_northeast
        else:
            x+= dx_east
            y+= dy_east
            d+= d_east
        loop_start+= 1
    plot( screen, zbuffer, color, x, y, 0 )
