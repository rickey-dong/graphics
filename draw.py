from display import *

def draw_line_octant_one(x0, y0, x1, y1, screen, color):
    x = x0
    y = y0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)
    d = A + B/2
    while x <= x1:
        plot(screen, color, x, y)
        if d > 0:
            y += 1
            d += B
        x += 1
        d += A

def draw_line_octant_two(x0, y0, x1, y1, screen, color):
    x = x0
    y = y0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)
    d = A/2 + B
    while y <= y1:
        plot(screen, color, x, y)
        if d < 0:
            x += 1
            d += A
        y += 1
        d += B

def draw_line_octant_seven(x0, y0, x1, y1, screen, color):
    x = x0
    y = y0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)
    d = A/2 - B
    while y >= y1:
        plot(screen, color, x, y)
        if d > 0:
            x += 1
            d += A
        y -= 1
        d -= B

def draw_line_octant_eight(x0, y0, x1, y1, screen, color):
    x = x0
    y = y0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)
    d = A - B/2
    while x <= x1:
        plot(screen, color, x, y)
        if d < 0:
            y -= 1
            d -= B
        x += 1
        d += A

def draw_line( x0, y0, x1, y1, screen, color ):
    x0 = int(x0)
    y0 = int(y0)
    x1 = int(x1)
    y1 = int(y1)
    # if second pixel's x-cor is < first pixel's x-cor, swap coords
    # so that we draw from left to right
    if x1 < x0:
        swap_x = x1
        swap_y = y1
        x1 = x0
        y1 = y0
        x0 = swap_x
        y0 = swap_y
    if (x1 == x0): # handling undefined slopes
        draw_line_octant_two(x0, y0, x1, y1, screen, color)
    else:
        slope = (y1 - y0) / (x1 - x0)
        if slope >= 0 and slope < 1:
            draw_line_octant_one(x0, y0, x1, y1, screen, color)
        elif slope >= 1:
            draw_line_octant_two(x0, y0, x1, y1, screen, color)
        elif slope <= -1:
            draw_line_octant_seven(x0, y0, x1, y1, screen, color)
        else:
            draw_line_octant_eight(x0, y0, x1, y1, screen, color)