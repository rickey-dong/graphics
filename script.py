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
            
             else:

         elif actual_command == "box" or actual_command == "sphere" or actual_command == "torus":
        
             if actual_command == "box":
            
             elif actual_command == "sphere":
            
             else:

         elif actual_command == "constants":
        
         elif actual_command == "line":
        
         elif actual_command == "save":
            
         elif actual_command == "display":