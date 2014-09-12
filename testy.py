def whatsThisDo(x):
    for side in [0,-1]:
        for y in range(0, x + side):
            y += side * (2 * (y + 1) - x)
            row = str(x - y) * (2 * (x - y) - 1)
            print(" " * y + row + " " * y)
