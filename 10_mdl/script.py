import mdl
from display import *
from matrix import *
from draw import *

def run(filename):
    """
    This function runs an mdl script
    """
    p = mdl.parseFile(filename)

    if p:
        (commands, symbols) = p
    else:
        print("Parsing failed.")
        return

    view = [0,
            0,
            1]
    ambient = [50,
               50,
               50]
    light = [[0.5,
              0.75,
              1],
             [255,
              255,
              255]]

    color = [0, 0, 0]
    tmp = new_matrix()
    ident( tmp )

    stack = [ [x[:] for x in tmp] ]
    screen = new_screen()
    zbuffer = new_zbuffer()
    tmp = []
    step_3d = 100
    consts = ''
    coords = []
    coords1 = []
    symbols['.white'] = ['constants',
                         {'red': [0.2, 0.5, 0.5],
                          'green': [0.2, 0.5, 0.5],
                          'blue': [0.2, 0.5, 0.5]}]
    reflect = '.white'
    for command in commands:
        actual_command = command['op']
        if actual_command == "push":
            copy_of_current_top = [row[:] for row in stack[-1]]
            stack.append(copy_of_current_top)
        elif actual_command == "pop":
            stack.pop()
        elif actual_command == "move" or actual_command == "rotate" or actual_command == "scale":
            if actual_command == "move":
                x_factor = command['args'][0]
                y_factor = command['args'][1]
                z_factor = command['args'][2]
                t = make_translate(x_factor, y_factor, z_factor)
                matrix_mult(stack[-1], t)
                stack[-1] = [row[:] for row in t]
            elif actual_command == "rotate":
                direction = command['args'][0]
                theta = command['args'][1] * (math.pi / 180)
                if direction == "x":
                    t = make_rotX(theta)
                elif direction == "y":
                    t = make_rotY(theta)
                else:
                    t = make_rotZ(theta)
                matrix_mult(stack[-1], t)
                stack[-1] = [row[:] for row in t]
            else:
                x_factor = command['args'][0]
                y_factor = command['args'][1]
                z_factor = command['args'][2]
                t = make_scale(x_factor, y_factor, z_factor)
                matrix_mult(stack[-1], t)
                stack[-1] = [row[:] for row in t]
        elif actual_command == "box" or actual_command == "sphere" or actual_command == "torus":
            if actual_command == "box":
                tmp = []
                x = command['args'][0]
                y = command['args'][1]
                z = command['args'][2]
                width = command['args'][3]
                height = command['args'][4]
                depth = command['args'][5]
                add_box(tmp, x, y, z, width, height, depth)
                matrix_mult(stack[-1], tmp)
                if command['constants'] == None:
                    draw_polygons(tmp, screen, zbuffer, view, ambient, light, symbols, reflect)
                else:
                    color_choice = command['constants']
                    draw_polygons(tmp, screen, zbuffer, view, ambient, light, symbols, color_choice)
                tmp = []
            elif actual_command == "sphere":
                tmp = []
                x = command['args'][0]
                y = command['args'][1]
                z = command['args'][2]
                r = command['args'][3]
                add_sphere(tmp, x, y, z, r, step_3d)
                matrix_mult(stack[-1], tmp)
                if command['constants'] == None:
                    draw_polygons(tmp, screen, zbuffer, view, ambient, light, symbols, reflect)
                else:
                    color_choice = command['constants']
                    draw_polygons(tmp, screen, zbuffer, view, ambient, light, symbols, color_choice)
                tmp = []
            else:
                tmp = []
                x = command['args'][0]
                y = command['args'][1]
                z = command['args'][2]
                r0 = command['args'][3]
                r1 = command['args'][4]
                add_torus(tmp, x, y, z, r0, r1, step_3d)
                matrix_mult(stack[-1], tmp)
                if command['constants'] == None:
                    draw_polygons(tmp, screen, zbuffer, view, ambient, light, symbols, reflect)
                else:
                    color_choice = command['constants']
                    draw_polygons(tmp, screen, zbuffer, view, ambient, light, symbols, color_choice)
                tmp = []
        elif actual_command == "constants":
            # don't need to do anything
            pass
        elif actual_command == "line":
            tmp = []
            x0 = command['args'][0]
            y0 = command['args'][1]
            z0 = command['args'][2]
            x1 = command['args'][3]
            y1 = command['args'][4]
            z1 = command['args'][5]
            add_edge(tmp, x0, y0, z0, x1, y1, z1)
            matrix_mult(tmp, stack[-1])
            draw_lines(stack[-1], screen, color)
            tmp = []
        elif actual_command == "save":
            file_name = command['args'][0]
            save_extension(screen, file_name)
        elif actual_command == "display":
            display(screen)
# HELLO
# {'shiny_purple': ['constants', {'red': [0.3, 0.2, 0.8], 'green': [0.3, 0.0, 0.0], 'blue': [0.3, 0.2, 0.8]}], 'shiny_teal': ['constants', {'red': [0.3, 0.0, 0.0], 'green': [0.3, 0.2, 0.8], 'blue': [0.3, 0.2, 0.8]}], 'dull_yellow': ['constants', {'red': [0.3, 0.8, 0.2], 'green': [0.3, 0.8, 0.2], 'blue': [0.0, 0.0, 0.0]}], '.white': ['constants', {'red': [0.2, 0.5, 0.5], 'green': [0.2, 0.5, 0.5], 'blue': [0.2, 0.5, 0.5]}]}
# HEY
# {'op': 'constants', 'args': None, 'constants': 'shiny_purple'}
# {'op': 'constants', 'args': None, 'constants': 'shiny_teal'}
# {'op': 'constants', 'args': None, 'constants': 'dull_yellow'}
# {'op': 'push', 'args': None}
# {'op': 'move', 'args': [250.0, 250.0, 0.0], 'knob': None}
# {'op': 'sphere', 'constants': 'shiny_purple', 'cs': None, 'args': [-100.0, 150.0, 0.0, 80.0]}
# {'op': 'sphere', 'constants': 'shiny_teal', 'cs': None, 'args': [100.0, 150.0, 0.0, 80.0]}
# {'op': 'push', 'args': None}
# {'op': 'rotate', 'args': ['x', 45.0], 'knob': None}
# {'op': 'rotate', 'args': ['y', 45.0], 'knob': None}
# {'op': 'box', 'constants': None, 'cs': None, 'args': [-40.0, 40.0, 40.0, 80.0, 80.0, 80.0]}
# {'op': 'pop', 'args': None}
# {'op': 'push', 'args': None}
# {'op': 'move', 'args': [0.0, -150.0, 0.0], 'knob': None}
# {'op': 'rotate', 'args': ['x', 30.0], 'knob': None}
# {'op': 'scale', 'args': [1.0, 1.0, 0.5], 'knob': None}
# {'op': 'torus', 'constants': 'dull_yellow', 'cs': None, 'args': [0.0, 0.0, 0.0, 30.0, 175.0]}
# {'op': 'display', 'args': None}
# {'op': 'save', 'args': ['face']}
