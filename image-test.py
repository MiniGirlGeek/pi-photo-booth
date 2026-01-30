import PIL
from PIL import Image
import numpy as np
from math import floor

width, height = 67, 100

#col_adjust = np.matrix('187 49 13; 30 59 86; 39 106 36')
#rgb were the worng way round, this fixes it
col_adjust = np.matrix('255 0 0; 0 0 225; 0 225 0')
col_adjust = col_adjust.I
im = Image.open('input.jpg')
im = im.rotate(90, expand=True)
im = im.resize((width, height), PIL.Image.ANTIALIAS)
imdata = list(im.getdata())
adjusted_img = []
preview = []

for pixel in imdata:
    adjusted_img.append(tuple((pixel * col_adjust).tolist()[0]))
    pixels = tuple((pixel * col_adjust).tolist()[0])
    r = int(pixels[0] * 255)
    g = int(pixels[1] * 255)
    b = int(pixels[2] * 255)
    preview.append((r, g, b))

def rgb_breakdown(colour):
    values = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    r = int(colour[0] * 12)
    g = int(colour[1] * 12)
    b = int(colour[2] * 12)

    if r > 12:
        r = 12
    if g > 12:
        g = 12
    if b > 12:
        b = 12

    if r < 0:
        r = 0
    if g < 0:
        g = 0
    if b < 0:
        b = 0

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

    new_list = []
    for l in values:
        new_list.append(l[:6])
        new_list.append(l[6:])

    values = new_list
    return values

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

im3 = Image.new(im.mode, (im.size[0]*6, im.size[1]*6))
im3.putdata(add_rgb_squares(width, height, rgb_squares))
im3.save('output.png')


im2 = Image.new(im.mode, im.size)
im2.putdata(preview)

im2.save('output.jpg')
