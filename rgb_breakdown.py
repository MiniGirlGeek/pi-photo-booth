def rgb_breakdown(colour):
    values = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    r = int(colour[0] * 10)
    g = int(colour[1] * 10)
    b = int(colour[2] * 10)

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
