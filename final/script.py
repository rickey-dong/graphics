from calendar import c
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

    name = ''
    num_frames = 1
    vary_present = False;

    for command in commands:
        if command['op'] == 'frames':
            num_frames = int(command['args'][0])
        if command['op'] == 'basename':
            name = command['args'][0]
        if command['op'] == 'vary':
            vary_present = True

    if vary_present and num_frames == 1:
        print('Error: Vary present, but no frames')
    
    if num_frames > 1 and name == '':
        name = 'default_name'


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
def second_pass( commands, num_frames ):
    # print("KSDJFLDSKJF", num_frames)
    frames = [ {} for i in range(num_frames) ]

    for i, frame in enumerate(frames):
        for command in commands:
            if command['op'] == 'vary':
                knob = command['knob']
                args = command['args']
                if i >= args[0] and i <= args[1]:
                    d_knob = (args[3] - args[2]) / (args[1] - args[0] + 1)
                    frame[knob] = args[2] + (i - args[0]) * d_knob

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
    light = [[0,
              0,
              1],
             [255,
              255,
              255]]

    color = [255, 255, 255]
    symbols['.white'] = ['constants',
                         {'red': [0.2, 0.5, 0.5],
                          'green': [0.2, 0.5, 0.5],
                          'blue': [0.2, 0.5, 0.5]}]
    reflect = '.white'

    (name, num_frames) = first_pass(commands)
    frames = second_pass(commands, num_frames)


    for current_frame, frame in enumerate(frames):

        for item in frame.items():
            symbols[item[0]] = item[1]

        tmp = new_matrix()
        ident( tmp )

        stack = [ [x[:] for x in tmp] ]
        screen = new_screen()
        zbuffer = new_zbuffer()
        tmp = []
        step_3d = 100
        shading = 'flat'
        consts = ''
        coords = []
        coords1 = []

        for command in commands:
            c = command['op']
            args = command['args']
            knob_value = 1
            if 'knob' in command.keys() and command['knob']:
                knob_value = symbols[command['knob']]
            

            if c == 'box':
                
                if command['constants']:
                    reflect = command['constants']
                add_box(tmp,
                        args[0], args[1], args[2],
                        args[3], args[4], args[5])
                matrix_mult( stack[-1], tmp )
                draw_polygons(tmp, screen, zbuffer, view, ambient, light, symbols, reflect, shading)
                tmp = []
                # read_obj('teapot.obj', tmp)
                # matrix_mult( stack[-1], tmp )
                # draw_polygons(tmp, screen, zbuffer, view, ambient, light, symbols, reflect)
                # tmp = []
                reflect = '.white'
            elif c == 'sphere':
                if command['constants']:
                    reflect = command['constants']
                add_sphere(tmp,
                        args[0], args[1], args[2], args[3], step_3d)
                matrix_mult( stack[-1], tmp )
                draw_polygons(tmp, screen, zbuffer, view, ambient, light, symbols, reflect, shading)
                tmp = []
                reflect = '.white'
            elif c == 'torus':
                if command['constants']:
                    reflect = command['constants']
                add_torus(tmp,
                        args[0], args[1], args[2], args[3], args[4], step_3d)
                matrix_mult( stack[-1], tmp )
                draw_polygons(tmp, screen, zbuffer, view, ambient, light, symbols, reflect, shading)
                tmp = []
                reflect = '.white'
            elif c == 'line':
                add_edge(tmp,
                        args[0], args[1], args[2], args[3], args[4], args[5])
                matrix_mult( stack[-1], tmp )
                draw_lines(tmp, screen, zbuffer, color)
                tmp = []
            
            elif c == 'aa_line':
                add_edge(tmp,
                        args[0], args[1], args[2], args[3], args[4], args[5])
                matrix_mult( stack[-1], tmp )
                draw_aa_lines(tmp, screen, zbuffer, color)
                tmp = []

            elif c == 'move':
                tmp = make_translate(args[0] * knob_value, args[1] * knob_value, args[2] * knob_value)
                matrix_mult(stack[-1], tmp)
                stack[-1] = [x[:] for x in tmp]
                tmp = []
            elif c == 'scale':

                tmp = make_scale(args[0] * knob_value, args[1] * knob_value, args[2] * knob_value)
                matrix_mult(stack[-1], tmp)
                stack[-1] = [x[:] for x in tmp]
                tmp = []
            elif c == 'rotate':
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
            elif c == 'shading':
                shading = command['shade_type']
            elif c == 'display' and num_frames < 2:
                display(screen)
            elif c == 'save':
                save_extension(screen, args[0] + '.png')
            # end operation loop
        if num_frames > 1:
            print('saving ' + name + f"_%03d.png"%current_frame)
            save_extension(screen, './anim/' + name + f"_%03d.png"%current_frame)
    
    if num_frames > 1:
        make_animation(name)