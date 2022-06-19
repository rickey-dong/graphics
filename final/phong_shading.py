from matrix import *
from gmath import *
from display import *
from draw import *

def is_close(arr1, arr2):
    close = abs(arr1[0] - arr2[0]) <= 0.0001 and abs(arr1[1] - arr2[1]) <= 0.0001 and abs(arr1[2] - arr2[2]) <= 0.0001
    return close

def add_norm(normals, pt):
    close = False
    for n in normals:
        if is_close(n, pt):
            close = True
            break
    
    if not close:
        normals.append(pt)


def calculate_vertex_normals(polygons):

    vertices = { tuple(v): [] for v in set([ tuple(p[:3]) for p in polygons])}

    i = 0
    while i < len(polygons):

        A = [polygons[i+1][j] - polygons[i][j] for j in range(3)]
        B = [polygons[i+2][j] - polygons[i][j] for j in range(3)]
        v1_n = cross_product(A, B)
        add_norm(vertices[tuple(polygons[i][:3])], v1_n)


        A = [polygons[i+2][j] - polygons[i+1][j] for j in range(3)]
        B = [polygons[i][j] - polygons[i+1][j] for j in range(3)]
        v2_n = cross_product(A, B)
        add_norm(vertices[tuple(polygons[i+1][:3])], v2_n)


        A = [polygons[i][j] - polygons[i+2][j] for j in range(3)]
        B = [polygons[i+1][j] - polygons[i+2][j] for j in range(3)]
        v3_n = cross_product(A, B)
        add_norm(vertices[tuple(polygons[i+2][:3])], v3_n)

        i += 3

    for k, v in vertices.items():
        v = list(v)
        x_total = 0
        y_total = 0
        z_total = 0
        for i in v:
            x_total += i[0]
            y_total += i[1]
            z_total += i[2]
        a = [x_total, y_total, z_total]
        normalize(a)
        vertices[k] = a

    return vertices


def interpolate_normals(polygons, i, vertices, screen, zbuffer, view, ambient, light, symbols, reflect):
    flip = False
    BOT = 0
    TOP = 2
    MID = 1

    points = [ (polygons[i][0], polygons[i][1], polygons[i][2]),
               (polygons[i+1][0], polygons[i+1][1], polygons[i+1][2]),
               (polygons[i+2][0], polygons[i+2][1], polygons[i+2][2]) ]


    # alas random color, we hardly knew ye
    #color = [0,0,0]
    #color[RED] = (23*(i/3)) %256
    #color[GREEN] = (109*(i/3)) %256
    #color[BLUE] = (227*(i/3)) %256

    points.sort(key = lambda x: x[1])
    x0 = points[BOT][0]
    z0 = points[BOT][2]
    x1 = points[BOT][0]
    z1 = points[BOT][2]
    y = int(points[BOT][1])

    distance0 = int(points[TOP][1]) - y * 1.0 + 1
    distance1 = int(points[MID][1]) - y * 1.0 + 1
    distance2 = int(points[TOP][1]) - int(points[MID][1]) * 1.0 + 1

    dx0 = (points[TOP][0] - points[BOT][0]) / distance0 if distance0 != 0 else 0
    dz0 = (points[TOP][2] - points[BOT][2]) / distance0 if distance0 != 0 else 0
    dx1 = (points[MID][0] - points[BOT][0]) / distance1 if distance1 != 0 else 0
    dz1 = (points[MID][2] - points[BOT][2]) / distance1 if distance1 != 0 else 0

    v_bot = vertices[points[BOT]]
    v_mid = vertices[points[MID]]
    v_top = vertices[points[TOP]]

    # top vertex -> bottom 
    dvx0 = (v_top[0] - v_bot[0]) / distance0 if distance0 != 0 else 0
    dvy0 = (v_top[1] - v_bot[1]) / distance0 if distance0 != 0 else 0
    dvz0 = (v_top[2] - v_bot[2]) / distance0 if distance0 != 0 else 0

    # middle -> bottom
    dvx1 = (v_mid[0] - v_bot[0]) / distance1 if distance1 != 0 else 0
    dvy1 = (v_mid[1] - v_bot[1]) / distance1 if distance1 != 0 else 0
    dvz1 = (v_mid[2] - v_bot[2]) / distance1 if distance1 != 0 else 0

    v0 = v_bot[:]
    v1 = v_bot[:]

    while y <= int(points[TOP][1]):
        if ( not flip and y >= int(points[MID][1])):
            flip = True

            dx1 = (points[TOP][0] - points[MID][0]) / distance2 if distance2 != 0 else 0
            dz1 = (points[TOP][2] - points[MID][2]) / distance2 if distance2 != 0 else 0
            x1 = points[MID][0]
            z1 = points[MID][2]
            v1 = v_mid[:]

            # top -> middle
            dvx1 = (v_top[0] - v_mid[0]) / distance2 if distance2 != 0 else 0
            dvy1 = (v_top[1] - v_mid[1]) / distance2 if distance2 != 0 else 0
            dvz1 = (v_top[2] - v_mid[2]) / distance2 if distance2 != 0 else 0 

        horizontal_interpolation(v0, v1, int(x0), int(x1), z0, z1, y, screen, zbuffer, view, ambient, light, symbols, reflect)
        x0+= dx0
        z0+= dz0
        x1+= dx1
        z1+= dz1

        v0[0]+= dvx0
        v0[1]+= dvy0
        v0[2]+= dvz0

        v1[0] += dvx1
        v1[1] += dvy1
        v1[2] += dvz1

        y += 1


def horizontal_interpolation(v0, v1, x0, x1, z0, z1, y, screen, zbuffer, view, ambient, light, symbols, reflect):

    if x1 < x0:
        x0, x1, = x1, x0
        z0, z1 = z1, z0
        v0, v1 = v1, v0
    

    dvx = (v1[0] - v0[0]) / (x1 - x0 + 1) if x1 - x0 + 1 != 0 else 0
    dvy = (v1[1] - v0[1]) / (x1 - x0 + 1) if x1 - x0 + 1 != 0 else 0
    dvz = (v1[2] - v0[2]) / (x1 - x0 + 1) if x1 - x0 + 1 != 0 else 0

    delta_z = (z1 - z0) / (x1 - x0 + 1) if (x1 - x0 + 1) != 0 else 0

    new_v = v0[:]
    x = x0
    z = z0
    while x <= x1:

        color = get_lighting(new_v, view, ambient, light, symbols, reflect )
        plot(screen, zbuffer, color, x, y, z)

        new_v[0] += dvx
        new_v[1] += dvy
        new_v[2] += dvz
        z += delta_z
        x += 1






if __name__ == '__main__':
    polygons = []
    screen = []
    zbuffer = []
    # add_box(polygons, 250, 250, 0, 100, 100, 100)
    # t = generate_torus(0, 0, 0, 30, 100, 20)
    # add_torus(polygons, 0, 0, 0, 30, 100, 20)
    vertices = calculate_vertex_normals(polygons)
    interpolate_normals(polygons, 0, vertices, screen, zbuffer, [0, 0, 0])
    # print(polygons)

