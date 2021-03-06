from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""

def parse_file( fname, points, transform, screen, color ):
    instruction_script = open(fname, 'r')
    while True:
        instr = instruction_script.readline()
        instr = instr.strip()
        if not instr:
            break
        if instr == "line":
            two_points = instruction_script.readline().strip().split()
            x0 = float(two_points[0])
            y0 = float(two_points[1])
            z0 = float(two_points[2])
            x1 = float(two_points[3])
            y1 = float(two_points[4])
            z1 = float(two_points[5])
            add_edge(points, x0, y0, z0, x1, y1, z1)
        elif instr == "ident":
            ident(transform)
        elif instr == "scale":
            scale_factors = instruction_script.readline().strip().split()
            sx = float(scale_factors[0])
            sy = float(scale_factors[1])
            sz = float(scale_factors[2])
            scale_matrix = make_scale(sx, sy, sz)
            matrix_mult(scale_matrix, transform)
        elif instr == "move":
            translation_factors = instruction_script.readline().strip().split()
            tx = float(translation_factors[0])
            ty = float(translation_factors[1])
            tz = float(translation_factors[2])
            translate_matrix = make_translate(tx, ty, tz)
            matrix_mult(translate_matrix, transform)
        elif instr == "rotate":
            axis_and_theta = instruction_script.readline().strip().split()
            degrees = float(axis_and_theta[1])
            axis = axis_and_theta[0]
            if axis == "x":
                  rotation_matrix = make_rotX(degrees)
                  matrix_mult(rotation_matrix, transform)
            elif axis == "y":
                  rotation_matrix = make_rotY(degrees)
                  matrix_mult(rotation_matrix, transform)
            elif axis == "z":
                  rotation_matrix = make_rotZ(degrees)
                  matrix_mult(rotation_matrix, transform)
        elif instr == "apply":
            matrix_mult(transform, points)
        elif instr == "display":
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)
        elif instr == "save":
            name_of_file = instruction_script.readline().strip().split()
            clear_screen(screen)
            draw_lines(points, screen, color)
            save_extension(screen, name_of_file[0])
        elif instr == "quit":
            break