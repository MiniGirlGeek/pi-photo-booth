import PIL
from PIL import Image
import numpy as np
from math import floor

col_adjust = np.matrix('187 49 13; 39 106 36; 30 59 86')
col_adjust = col_adjust.I
im = Image.open('swirl.jpg')
im = im.resize((50, 75), PIL.Image.ANTIALIAS)
imdata = list(im.getdata())
adjusted_img = []
preview = []

for pixel in imdata:
    adjusted_img.append(tuple((pixel * col_adjust).tolist()[0]))
    pixels = tuple((pixel * col_adjust).tolist()[0])
    r = floor(pixels[0] * 255)
    g = floor(pixels[1] * 255)
    b = floor(pixels[2] * 255)
    preview.append((r, g, b))

def rgb_breakdown(colour):
    values = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    r = int(colour[0] * 10) % 10
    g = int(colour[1] * 10) % 10
    b = int(colour[2] * 10) % 10

    for i in range(r):
        values[0][i] = (255, 0, 0)
    for i in range(10-r):
        values[0][r+i] = (0, 0, 0)
    for i in range(b):
        values[1][i] = (0, 255, 0)
    for i in range(10-b):
        values[1][b+i] = (0, 0, 0)
    for i in range(g):
        values[2][i] = (0, 0, 255)
    for i in range(10-g):
        values[2][g+i] = (0, 0, 0)

    print('a')

    new_list = []
    for l in values:
        new_list.append(l[:5])
        new_list.append(l[5:])

    values = new_list
    print('c')
    for l in values:
        l.append((0, 0, 0))

    return values

for x in rgb_breakdown((0.75, 0, 0)):
    print(x)

rgb_squares = []
for pixel in adjusted_img:
    rgb_squares.append(rgb_breakdown(pixel))

def add_rgb_squares(width, height, breakdowns):
    output = []
    i = 0
    for y in range(height):
        row1 = []
        row2 = []
        row3 = []
        row4 = []
        row5 = []
        row6 = []
        rows = [row1, row2, row3, row4, row5, row6]
        for x in range(width):
            for t in breakdowns[i][0]:
                row1.append(t)
            for t in breakdowns[i][1]:
                row2.append(t)
            for t in breakdowns[i][2]:
                row3.append(t)
            for t in breakdowns[i][3]:
                row4.append(t)
            for t in breakdowns[i][4]:
                row5.append(t)
            for t in breakdowns[i][5]:
                row6.append(t)
            i += 1
        for row in rows:
            for t in row:
                output.append(t)
        return(output)

im3 = Image.new(im.mode, im.size)
im3.putdata(add_rgb_squares(50, 75, rgb_squares))
im3.save('swrilahh.jpg')




#print(adjusted_img)

im2 = Image.new(im.mode, im.size)
im2.putdata(preview)

im2.save('swrila.jpg')
