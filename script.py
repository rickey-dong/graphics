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
            1];
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
    print("HELLO")
    print(symbols)
    print("HEY")
    for command in commands:
        print(command)
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
                theta = command['args'][1]
                if direction == "x":
                    t = make_rotX(theta)
                elif direction == "y":
                    t = make_rotY(theta)
                else:
                    t = make_rotZ(theta)
                matrix_mult(stack[-1], t)
                stack[-1] = [row[:] for row in t]
             else:

         elif actual_command == "box" or actual_command == "sphere" or actual_command == "torus":
        
             if actual_command == "box":
            
             elif actual_command == "sphere":
            
             else:

         elif actual_command == "constants":
        
         elif actual_command == "line":
        
         elif actual_command == "save":
            
         elif actual_command == "display":

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
