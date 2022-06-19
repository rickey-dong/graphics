from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 255 ]
m1 = new_matrix()
m2 = []
edges = []

print('\nTesting add_edge. Adding (1, 2, 3), (4, 5, 6) m2 =')
add_edge(m2, 1, 2, 3, 4, 5, 6)
print_matrix( m2 )

print('Testing ident. m1 = ')
ident(m1)
print_matrix( m1 )

print('\nTesting matrix_mult. m1 * m2 =')
matrix_mult(m1, m2)
print_matrix(m2)

m1 = [];
add_edge(m1, 1, 2, 3, 4, 5, 6)
add_edge(m1, 7, 8, 9, 10, 11, 12)
print("\nTesting Matrix mult. m1 =")
print_matrix(m1)
print("\nTesting Matrix mult. m1 * m2 =")
matrix_mult(m1, m2);
print_matrix(m2);

add_edge(edges, 50, 450, 0, 100, 450, 0)
add_edge(edges, 50, 450, 0, 50, 400, 0)
add_edge(edges, 100, 450, 0, 100, 400, 0)
add_edge(edges, 100, 400, 0, 50, 400, 0)

add_edge(edges, 200, 450, 0, 250, 450, 0)
add_edge(edges, 200, 450, 0, 200, 400, 0)
add_edge(edges, 250, 450, 0, 250, 400, 0)
add_edge(edges, 250, 400, 0, 200, 400, 0)

add_edge(edges, 150, 400, 0, 130, 360, 0)
add_edge(edges, 150, 400, 0, 170, 360, 0)
add_edge(edges, 130, 360, 0, 170, 360, 0)

add_edge(edges, 100, 340, 0, 200, 340, 0)
add_edge(edges, 100, 320, 0, 200, 320, 0)
add_edge(edges, 100, 340, 0, 100, 320, 0)
add_edge(edges, 200, 340, 0, 200, 320, 0)  

# screen2 = new_screen()
# color2 = [255, 255, 255]
# trix_bunny_edge_list = []
# add_edge(trix_bunny_edge_list, 40, 60, 0, 40, 80, 0)
# add_edge(trix_bunny_edge_list, 40, 80, 0, 60, 120, 0)
# add_edge(trix_bunny_edge_list, 60, 120, 0, 60, 130, 0)
# add_edge(trix_bunny_edge_list, 60, 130, 0, 80, 120, 0)

# add_edge(trix_bunny_edge_list, 80, 120, 0, 100, 120, 0)
# add_edge(trix_bunny_edge_list, 100, 120, 0, 120, 130, 0)
# add_edge(trix_bunny_edge_list, 120, 130, 0, 140, 140, 0)
# add_edge(trix_bunny_edge_list, 150, 160, 0, 140, 140, 0)

# add_edge(trix_bunny_edge_list, 60, 130, 0, 40, 140, 0)
# add_edge(trix_bunny_edge_list, 40, 140, 0, 20, 160, 0)
# add_edge(trix_bunny_edge_list, 20, 160, 0, 20, 190, 0)
# add_edge(trix_bunny_edge_list, 20, 190, 0, 40, 220, 0)
# add_edge(trix_bunny_edge_list, 40, 220, 0, 80, 250, 0)
# add_edge(trix_bunny_edge_list, 80, 250, 0, 90, 260, 0)
# add_edge(trix_bunny_edge_list, 90, 260, 0, 80, 300, 0)
# add_edge(trix_bunny_edge_list, 80, 300, 0, 80, 360, 0)
# add_edge(trix_bunny_edge_list, 80, 360, 0, 90, 400, 0)
# add_edge(trix_bunny_edge_list, 90, 400, 0, 100, 400, 0)
# add_edge(trix_bunny_edge_list, 100, 400, 0, 130, 340, 0)
# add_edge(trix_bunny_edge_list, 130, 340, 0, 130, 300, 0)
# add_edge(trix_bunny_edge_list, 130, 300, 0, 120, 260, 0)
# add_edge(trix_bunny_edge_list, 120, 260, 0, 140, 300, 0)
# add_edge(trix_bunny_edge_list, 140, 300, 0, 200, 340, 0)
# add_edge(trix_bunny_edge_list, 200, 340, 0, 220, 340, 0)
# add_edge(trix_bunny_edge_list, 220, 340, 0, 160, 300, 0)
# add_edge(trix_bunny_edge_list, 160, 300, 0, 120, 260, 0)

# add_edge(trix_bunny_edge_list, 220, 340, 0, 220, 320, 0)
# add_edge(trix_bunny_edge_list, 220, 320, 0, 200, 280, 0)
# add_edge(trix_bunny_edge_list, 140, 220, 0, 200, 280, 0)
# add_edge(trix_bunny_edge_list, 240, 280, 0, 200, 280, 0)
# add_edge(trix_bunny_edge_list, 240, 280, 0, 300, 260, 0)
# add_edge(trix_bunny_edge_list, 300, 260, 0, 320, 220, 0)
# add_edge(trix_bunny_edge_list, 320, 220, 0, 330, 230, 0)
# add_edge(trix_bunny_edge_list, 330, 230, 0, 340, 220, 0)
# add_edge(trix_bunny_edge_list, 340, 220, 0, 340, 180, 0)
# add_edge(trix_bunny_edge_list, 340, 180, 0, 320, 160, 0)
# add_edge(trix_bunny_edge_list, 320, 220, 0, 320, 140, 0)
# add_edge(trix_bunny_edge_list, 320, 140, 0, 300, 120, 0)
# add_edge(trix_bunny_edge_list, 300, 120, 0, 300, 80, 0)
# add_edge(trix_bunny_edge_list, 300, 80, 0, 240, 20, 0)
# add_edge(trix_bunny_edge_list, 240, 20, 0, 200, 20, 0)
# add_edge(trix_bunny_edge_list, 200, 20, 0, 180, 20, 0)
# add_edge(trix_bunny_edge_list, 200, 20, 0, 200, 40, 0)
# add_edge(trix_bunny_edge_list, 200, 40, 0, 240, 80, 0)
# add_edge(trix_bunny_edge_list, 240, 80, 0, 220, 80, 0)
# add_edge(trix_bunny_edge_list, 220, 80, 0, 180, 40, 0)
# add_edge(trix_bunny_edge_list, 180, 20, 0, 180, 40, 0)
# add_edge(trix_bunny_edge_list, 220, 80, 0, 200, 80, 0)
# add_edge(trix_bunny_edge_list, 200, 80, 0, 120, 20, 0)
# add_edge(trix_bunny_edge_list, 120, 20, 0, 100, 20, 0)
# add_edge(trix_bunny_edge_list, 100, 20, 0, 100, 40, 0)
# add_edge(trix_bunny_edge_list, 100, 40, 0, 120, 80, 0)
# add_edge(trix_bunny_edge_list, 120, 80, 0, 100, 80, 0)
# add_edge(trix_bunny_edge_list, 100, 80, 0, 60, 60, 0)
# add_edge(trix_bunny_edge_list, 60, 60, 0, 40, 60, 0)

# draw_lines(trix_bunny_edge_list, screen2, color2)
# save_extension(screen2, "trix.png")

draw_lines( edges, screen, color )
save_extension(screen, "bob.png")
#display(screen)
