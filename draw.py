from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
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