def findfive(file, clas, value):
    a = []
    with open(file, "r") as f:
        for i in f.readlines():
            b = i.split(",")          
            c = b[3].strip()
            if c.isdigit():
                if int(c) == value and b[1] == clas:
                    a.append(b[2])
    return a