import networkx as nx
import matplotlib.pyplot as plt
import requests
import math
import numpy as np

def parse(site):
    text = requests.get(site).text
    towns = {}
    n = text.find("</h2>")
    f = text[n:].find("<h2>") + n
    text = text[n:f]

    a = text.find("coordinates-items-left")
    while a != -1:
        a = a + 24
        f = text[a:].find("<") + a
        nk = text[f:].find("coordinates-items-right") + 25 + f
        nf = text[nk:].find("<") + nk


        towns.update({text[a:f]: list(map((lambda x : float(x)),reversed(text[nk:nf].split(", "))))})

        a = text[nf:].find("coordinates-items-left")
        if a == -1:
            break
        a += nf
    return towns



def graf(file):
    g = nx.Graph()
    chords = parse("https://time-in.ru/coordinates/russia")

    with open(file, "r") as f:
        ribbles = eval(f.readline())
    vert = []
    ser_med = 70
    r = 6378.1
    zy = {-9: 1, -8: 0.92, -7: 0.863, -6: 0.82, -5: 0.78, -4: 0.76, -3: 0.75, -2: 0.73, -1: 0.72, 0: 1, 1: .72, 2:0.73, 3: 0.75, 4: 0.76, 5: 0.78, 6: 0.82, 7: 0.863, 8: 0.92, 9: 1}


    for i in ribbles:
        if i[0] in chords.keys() and i[1] in chords.keys():
            if i[0] not in vert:
                x, y = chords[i[0]]
                ny = math.sin(math.radians(90 - y)) * math.sin(math.radians(x - ser_med)) * r * zy[round((x - ser_med)/10)]
                nz = math.cos(math.radians(90 - y)) * r  - math.cos(math.radians(x - ser_med))* r / 6
                g.add_node(i[0], pos=(ny, nz))

            if i[1] not in vert:
                x, y = chords[i[1]]
                ny = math.sin(math.radians(90 - y)) * math.sin(math.radians(x - ser_med)) * r * zy[round((x - ser_med)/10)]
                nz = math.cos(math.radians(90 - y)) * r - math.cos(math.radians(x - ser_med))* r / 6
                g.add_node(i[1], pos=(ny, nz))
            g.add_edge(i[0], i[1])

        else:
            ribbles.remove(i)

    x, y = (70, 40)
    ny = math.sin(math.radians(90 - y)) * math.sin(math.radians(x - ser_med)) * r
    nz = math.cos(math.radians(90 - y)) * r - math.cos(math.radians(x - ser_med))* r / 6
    g.add_node("a", pos=(ny, nz))
    #
    # x, y = (80, 50)
    # ny = math.sin(math.radians(90 - y)) * math.sin(math.radians(x - ser_med)) * r
    # nz = math.cos(math.radians(90 - y)) * r
    # g.add_node("d", pos=(ny, nz))
    #
    # x, y = (140, 40)
    # ny = math.sin(math.radians(90 - y)) * math.sin(math.radians(x - ser_med)) * r
    # nz = math.cos(math.radians(90 - y)) * r
    # g.add_node("b", pos=(ny, nz))
    #
    # x, y = (30, 60)
    # ny = math.sin(math.radians(90 - y)) * math.sin(math.radians(x - ser_med)) * r
    # nz = math.cos(math.radians(90 - y)) * r
    # g.add_node("c", pos=(ny, nz))



    img = plt.imread("map.jpg")
    fig, ax = plt.subplots()

    m = 0
    ax.imshow(img, extent=[-r + m, r - m, 0,r])
    nx.draw_networkx(g, nx.get_node_attributes(g, 'pos'), with_labels=False, node_size=100)
    plt.show()


if __name__ == "__main__":
    graf("ribbles.txt")
