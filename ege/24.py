
m = 0
s = 0
with open("zadanie24_2.txt") as f:
    bo = False
    for i in f.readlines():
        for j in i:
            if j == "R":
                s += 1
            else:
                m = max(s, m)
                s = 0




print(m)