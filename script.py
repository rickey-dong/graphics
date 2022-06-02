import mdl
from display import *
from matrix import *
from draw import *

"""======== first_pass( commands ) ==========

  Checks the commands array for any animation commands
  (frames, basename, vary)

  Should set num_frames and basename if the frames
  or basename commands are present

  If vary is found, but frames is not, the entire
  program should exit.

  If frames is found, but basename is not, set name
  to some default value, and print out a message
  with the name being used.
  ==================== """
def first_pass( commands ):
    frames_found = False
    basename_found = False
    vary_found = False

    for command in commands:
        if command['op'] == 'frames':
            frames_found = True
            num_frames = command['args'][0]
        elif command['op'] == 'basename':
            basename_found = True
            name = command['args'][0]
        elif command['op'] == 'vary':
            vary_found = True
    
    if vary_found and not frames_found:
        exit()
    
    if frames_found and not basename_found:
        name = 'default_animation_name'
        print("No name found. Using default name 'default_animation_name'")
    
    num_frames = int(num_frames)

    return (name, num_frames)

"""======== second_pass( commands ) ==========

  In order to set the knobs for animation, we need to keep
  a seaprate value for each knob for each frame. We can do
  this by using an array of dictionaries. Each array index
  will correspond to a frame (eg. knobs[0] would be the first
  frame, knobs[2] would be the 3rd frame and so on).

  Each index should contain a dictionary of knob values, each
  key will be a knob name, and each value will be the knob's
  value for that frame.

  Go through the command array, and when you find vary, go
  from knobs[0] to knobs[frames-1] and add (or modify) the
  dictionary corresponding to the given knob with the
  appropirate value.
  ===================="""
# {'op': 'frames', 'args': [50.0]}
# {'op': 'basename', 'args': ['simple_50']}
# {'op': 'push', 'args': None}
# {'op': 'move', 'args': [250.0, 250.0, 0.0], 'knob': None}
# {'op': 'scale', 'args': [2.0, 2.0, 2.0], 'knob': 'bigenator'}
# {'op': 'rotate', 'args': ['y', 360.0], 'knob': 'spinny'}
# {'op': 'rotate', 'args': ['z', 360.0], 'knob': 'spinny'}
# {'op': 'torus', 'constants': None, 'cs': None, 'args': [0.0, 0.0, 0.0, 75.0, 125.0]}
# {'op': 'vary', 'args': [0.0, 49.0, 0.0, 1.0], 'knob': 'spinny'}
# {'op': 'vary', 'args': [0.0, 24.0, 0.0, 1.0], 'knob': 'bigenator'}
# {'op': 'vary', 'args': [25.0, 49.0, 1.0, 0.0], 'knob': 'bigenator'}

def second_pass( commands, num_frames ):
    frames = [ {} for i in range(num_frames) ]
    for command in commands:
        if command['op'] == 'vary':
            start_index = int(command['args'][0])
            end_index = int(command['args'][1])
            step_size = (command['args'][3] - command['args'][2]) / (command['args'][1] - command['args'][0])
            frames[start_index][command['knob']] = command['args'][2]
            while start_index <= end_index:
                start_index += 1
                if start_index <= end_index:
                    frames[start_index][command['knob']] = frames[start_index-1][command['knob']] + step_size
    return frames


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
    symbols['.white'] = ['constants',
                         {'red': [0.2, 0.5, 0.5],
                          'green': [0.2, 0.5, 0.5],
                          'blue': [0.2, 0.5, 0.5]}]
    reflect = '.white'

    (name, num_frames) = first_pass(commands)
    frames = second_pass(commands, num_frames)
    current_frame = 0
    while current_frame < num_frames:
        # print("Creating frame " + str(current_frame))
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
        if num_frames > 1:
            for knob_key in frames[current_frame]:
                symbols[knob_key].append(frames[current_frame][knob_key])
        for command in commands:
            c = command['op']
            args = command['args']
            knob_value = 1
            if c == 'box':
                if command['constants']:
                    reflect = command['constants']
                add_box(tmp,
                        args[0], args[1], args[2],
                        args[3], args[4], args[5])
                matrix_mult( stack[-1], tmp )
                draw_polygons(tmp, screen, zbuffer, view, ambient, light, symbols, reflect)
                tmp = []
                reflect = '.white'
            elif c == 'sphere':
                if command['constants']:
                    reflect = command['constants']
                add_sphere(tmp,
                        args[0], args[1], args[2], args[3], step_3d)
                matrix_mult( stack[-1], tmp )
                draw_polygons(tmp, screen, zbuffer, view, ambient, light, symbols, reflect)
                tmp = []
                reflect = '.white'
            elif c == 'torus':
                if command['constants']:
                    reflect = command['constants']
                add_torus(tmp,
                        args[0], args[1], args[2], args[3], args[4], step_3d)
                matrix_mult( stack[-1], tmp )
                draw_polygons(tmp, screen, zbuffer, view, ambient, light, symbols, reflect)
                tmp = []
                reflect = '.white'
            elif c == 'line':
                add_edge(tmp,
                        args[0], args[1], args[2], args[3], args[4], args[5])
                matrix_mult( stack[-1], tmp )
                draw_lines(tmp, screen, zbuffer, color)
                tmp = []
            elif c == 'move':
                if command['knob'] is not None:
                    knob_value = symbols[command['knob']][-1]
                tmp = make_translate(args[0]*knob_value, args[1]*knob_value, args[2]*knob_value)
                matrix_mult(stack[-1], tmp)
                stack[-1] = [x[:] for x in tmp]
                tmp = []
            elif c == 'scale':
                if command['knob'] is not None:
                    knob_value = symbols[command['knob']][-1]
                tmp = make_scale(args[0]*knob_value, args[1]*knob_value, args[2]*knob_value)
                matrix_mult(stack[-1], tmp)
                stack[-1] = [x[:] for x in tmp]
                tmp = []
            elif c == 'rotate':
                if command['knob'] is not None:
                    knob_value = symbols[command['knob']][-1]
                theta = args[1] * (math.pi/180) * knob_value
                if args[0] == 'x':
                    tmp = make_rotX(theta)
                elif args[0] == 'y':
                    tmp = make_rotY(theta)
                else:
                    tmp = make_rotZ(theta)
                matrix_mult( stack[-1], tmp )
                stack[-1] = [ x[:] for x in tmp]
                tmp = []
            elif c == 'push':
                stack.append([x[:] for x in stack[-1]] )
            elif c == 'pop':
                stack.pop()
            elif c == 'display':
                display(screen)
            elif c == 'save':
                save_extension(screen, args[0])
            # end operation loop
        save_extension(screen, "anim/"+name+f"%03d"%current_frame)
        current_frame += 1
    make_animation(name)