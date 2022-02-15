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
c[RED] = 205
c[GREEN] = 133
c[BLUE] = 63
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

c[RED] = 139
c[GREEN] = 69
c[BLUE] = 19
draw_line(400, 180, 450, 240, s, c)
draw_line(400, 220, 425, 240, s, c)
draw_line(425, 240, 425, 400, s, c)
draw_line(450, 240, 450, 340, s, c)
draw_line(450, 340, 425, 360, s, c)
draw_line(450, 340, 475, 380, s, c)
draw_line(475, 380, 475, 400, s, c)
draw_line(475, 400, 450, 420, s, c)
draw_line(450, 420, 425, 400, s, c)

c[RED] = 255
c[GREEN] = 0
c[BLUE] = 0
draw_line(350, 280, 350, 300, s, c)
draw_line(350, 300, 375, 280, s, c)
draw_line(375, 280, 375, 340, s, c)
draw_line(375, 340, 400, 320, s, c)
draw_line(400, 320, 375, 380, s, c)
draw_line(375, 380, 400, 360, s, c)
draw_line(400, 360, 400, 380, s, c)
draw_line(400, 380, 375, 420, s, c)
draw_line(375, 420, 400, 420, s, c)
draw_line(400, 420, 375, 440, s, c)
draw_line(375, 440, 325, 460, s, c)
draw_line(325, 460, 350, 480, s, c)
draw_line(350, 480, 250, 480, s, c)
draw_line(250, 480, 225, 460, s, c)
draw_line(225, 460, 200, 480, s, c)
draw_line(200, 480, 100, 480, s, c)
draw_line(100, 480, 125, 460, s, c)
draw_line(125, 460, 75, 440, s, c)
draw_line(75, 440, 50, 420, s, c)
draw_line(50, 420, 75, 420, s, c)
draw_line(75, 420, 50, 380, s, c)
draw_line(50, 360, 50, 380, s, c)
draw_line(50, 360, 75, 380, s, c)
draw_line(75, 380, 50, 320, s, c)
draw_line(50, 320, 75, 340, s, c)
draw_line(75, 280, 75, 340, s, c)
draw_line(75, 280, 100, 300, s, c)
draw_line(100, 280, 100, 300, s, c)
draw_line(100, 280, 125, 240, s, c)
draw_line(125, 240, 125, 280, s, c)
draw_line(125, 280, 175, 240, s, c)
draw_line(175, 240, 175, 260, s, c)
draw_line(175, 260, 225, 220, s, c)
draw_line(225, 220, 275, 260, s, c)
draw_line(275, 240, 275, 260, s, c)
draw_line(275, 240, 325, 280, s, c)
draw_line(325, 240, 325, 280, s, c)
draw_line(325, 240, 350, 280, s, c)

c[RED] = 255
c[GREEN] = 140
c[BLUE] = 0
draw_line(125, 320, 125, 400, s, c)
draw_line(125, 400, 175, 420, s, c)
draw_line(175, 420, 275, 420, s, c)
draw_line(275, 420, 325, 400, s, c)
draw_line(325, 320, 325, 400, s, c)
draw_line(325, 320, 275, 300, s, c)
draw_line(275, 300, 175, 300, s, c)
draw_line(175, 300, 125, 320, s, c)

draw_line(150, 440, 150, 460, s, c)
draw_line(150, 460, 175, 460, s, c)
draw_line(175, 460, 200, 440, s, c)

draw_line(300, 440, 300, 460, s, c)
draw_line(300, 460, 275, 460, s, c)
draw_line(275, 460, 250, 440, s, c)

draw_line(175, 380, 175, 400, s, c)
draw_line(175, 400, 200, 400, s, c)
draw_line(200, 380, 200, 400, s, c)
draw_line(200, 380, 175, 380, s, c)

draw_line(250, 380, 250, 400, s, c)
draw_line(250, 400, 275, 400, s, c)
draw_line(275, 380, 275, 400, s, c)
draw_line(275, 380, 250, 380, s, c)

draw_line(200, 360, 250, 360, s, c)
draw_line(200, 360, 225, 340, s, c)
draw_line(250, 360, 225, 340, s, c)
draw_line(225, 320, 225, 340, s, c)
draw_line(200, 320, 250, 320, s, c)
draw_line(200, 320, 175, 340, s, c)
draw_line(250, 320, 275, 340, s, c)

display(s)
save_ppm(s, 'binary.ppm')
save_ppm_ascii(s, 'ascii.ppm')
save_extension(s, 'img.png')
