for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                o = (not(x) and not(y)) or (y == z) or w
                print(x, y, z, w, int(o))
