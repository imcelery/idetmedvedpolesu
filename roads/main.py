import networkx as nx
import matplotlib.pyplot as plt

import requests
import numpy as np

# def parse(site):
#     text = requests.get(site).text
#     towns = {}
#     a = text.find("coordinates-items-left") + 25
#     while a != -1:
#         print(a)
#         f = text[a:].find(">") - 1 + a
#
#         nk = text[f:].find("coordinates-items-right") + 25 + f
#
#
#         towns.update({text[a:f]: text[nk:nk + 13].split(", ")})
#         print({text[a:f]: text[nk:nk + 12].split(", ")})
#         a = text[nk:].find("coordinates-items-left") + 37 + nk

def parse2(file):
    towns = {}
    with open(file, "r", encoding="utf8") as f:
        for i in f:
            i = i.split(", ")

            for j, el in enumerate(i[0]):
                if el.isdigit():
                    n = j
                    break

            towns.update({i[0][:n]: ( float(i[1]), float(i[0][n:]))})
    return towns




def graf(file, file2, file3):
    g = nx.Graph()
    chords = parse2(file)

    with open(file3, "r") as f:
        ribbles = eval(f.readline())
    vert = []
    for i in ribbles:

        if i[0] in chords.keys() and i[1] in chords.keys():
            if i[0] not in vert:
                g.add_node(i[0], pos =chords[i[0]])

            if i[1] not in vert:
                g.add_node(i[1], pos =chords[i[1]])
            g.add_edge(i[0], i[1])

        else:
            ribbles.remove(i)
    nx.draw_networkx(g, nx.get_node_attributes(g, 'pos'), with_labels=True, node_size=0)
    plt.show()
    plt.savefig("россия.png")


graf("towns.txt", "list.txt", "ribbles.txt")