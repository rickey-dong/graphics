from display import *
from draw import *

s = new_screen()
c = [ 0, 255, 0 ]

    # #octants 1 and 5
    # draw_line(0, 0, XRES-1, YRES-1, s, c)
    # draw_line(0, 0, XRES-1, YRES / 2, s, c) 
    # draw_line(XRES-1, YRES-1, 0, YRES / 2, s, c)

    # #octants 8 and 4
    # c[BLUE] = 255;
    # draw_line(0, YRES-1, XRES-1, 0, s, c);  
    # draw_line(0, YRES-1, XRES-1, YRES/2, s, c);
    # draw_line(XRES-1, 0, 0, YRES/2, s, c);

    # #octants 2 and 6
    # c[RED] = 255;
    # c[GREEN] = 0;
    # c[BLUE] = 0;
    # draw_line(0, 0, XRES/2, YRES-1, s, c);
    # draw_line(XRES-1, YRES-1, XRES/2, 0, s, c);

    # #octants 7 and 3
    # c[BLUE] = 255;
    # draw_line(0, YRES-1, XRES/2, 0, s, c);
    # draw_line(XRES-1, 0, XRES/2, YRES-1, s, c);

    # #horizontal and vertical
    # c[BLUE] = 0;
    # c[GREEN] = 255;
    # draw_line(0, YRES/2, XRES-1, YRES/2, s, c);
    # draw_line(XRES/2, 0, XRES/2, YRES-1, s, c);

draw_line(0, 20, 500, 20, s, c)
draw_line(50, 20, 50, 40, s, c)
draw_line(75, 20, 75, 40, s, c)
draw_line(100, 20, 100, 40, s, c)
draw_line(125, 20, 150, 40, s, c)
draw_line(50, 40, 75, 60, s, c)
draw_line(75, 60, 50, 140, s, c)
draw_line(50, 140, 50, 220, s, c)
draw_line(50, 220, 75, 260, s, c)
draw_line(75, 260, 100, 280, s, c)
draw_line(150, 40, 125, 140, s, c)
draw_line(125, 140, 150, 180, s, c)
draw_line(125, 140, 175, 120, s, c)
draw_line(175, 100, 175, 120, s, c)
draw_line(175, 100, 200, 60, s, c)
draw_line(200, 40, 200, 60, s, c)
draw_line(200, 40, 175, 20, s, c)
draw_line(175, 120, 275, 120, s, c)
draw_line(275, 100, 275, 120, s, c)
draw_line(275, 100, 250, 60, s, c)
draw_line(250, 40, 250, 60, s, c)
draw_line(250, 40, 275, 20, s, c)
draw_line(325, 20, 300, 40, s, c)
draw_line(300, 40, 325, 140, s, c)
draw_line(325, 140, 300, 180, s, c)
draw_line(325, 140, 275, 120, s, c)
draw_line(350, 20, 350, 40, s, c)
draw_line(375, 20, 375, 40, s, c)
draw_line(400, 20, 400, 40, s, c)
draw_line(400, 40, 375, 60, s, c)
draw_line(375, 60, 400, 140, s, c)
draw_line(400, 140, 400, 220, s, c)
draw_line(400, 220, 375, 260, s, c)
draw_line(375, 260, 350, 280, s, c)

draw_line(400, 180, 450, 240, s, c)
draw_line(400, 220, 425, 240, s, c)
draw_line(425, 240, 425, 400, s, c)
draw_line(450, 240, 450, 340, s, c)
draw_line(450, 340, 425, 360, s, c)
draw_line(450, 340, 475, 380, s, c)
draw_line(475, 380, 475, 400, s, c)
draw_line(475, 400, 450, 420, s, c)
draw_line(450, 420, 425, 400, s, c)

display(s)
save_ppm(s, 'binary.ppm')
save_ppm_ascii(s, 'ascii.ppm')
save_extension(s, 'img.png')
