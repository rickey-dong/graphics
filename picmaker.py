f = open("picnic.ppm", "w")
f.write(
"""P3
500 500
255
"""
)
f.close()

red_rgb = "255 0 0"
pink_rgb = "255 192 203"
white_rgb = "255 255 255"
even_xcor = True
even_ycor = True
rows = 500
cols = 500

with open('picnic.ppm', 'a') as f:
    for ycor in range(rows): # each square is 20 pixels
        for xcor in range(int(cols / 20)):
            if even_xcor and even_ycor:
                for i in range(20):
                    f.write(red_rgb)
                    f.write('\n')
            elif ((not even_xcor) and even_ycor) or (even_xcor and (not even_ycor)):
                for i in range(20):
                    f.write(pink_rgb)
                    f.write('\n')
            else:
                for i in range(20):
                    f.write(white_rgb)
                    f.write('\n')
            even_xcor = not even_xcor
        even_xcor = True
        if ycor != 0 and ycor % 20 == 0:
            even_ycor = not even_ycor
