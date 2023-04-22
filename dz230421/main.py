import random
import networkx as nx
import matplotlib.pyplot as plt

class reb:
    def __init__(self, l, ver1, ver2):
        self.vers = [ver1, ver2]
        self.l = l
        self.fer = 1

    def upd(self, d):
        self.fer = max(self.fer - d, 0)

    def __hash__(self):
        return hash((self.vers[0], self.vers[1]))

    def __eq__(self, other):
        if not isinstance(other, type(self)): return NotImplemented
        return self.vers[0] == other.vers[0] and self.vers[1] == other.vers[1]

class mur:
    def __init__(self, speed, graf_rebs, ver, alpha=1, beta=-2):
        self.speed = speed
        self.reb = None
        self.l = 0
        self.next_ver =ver
        self.graf_rebs = graf_rebs
        self.taboo = []
        self.alpha = alpha
        self.beta = beta


    def upd(self):

        t = self.speed / self.reb.l
        self.l += t
        self.reb.fer += t
        if self.l >= 1:
            self.l = 0
            self.taboo.append(self.reb.vers)
            return self.set_new_reb(self.graf_rebs[self.next_ver])

        return True

    def set_new_reb(self, rebs):

        mh = []

        for i in rebs.values():

            if i.vers not in self.taboo:

                mh.append((i.fer ** self.alpha) * (i.l ** self.beta))



        if len(mh):
            return False


        for i in self.reb.vers:

            if i != self.next_ver:
                self.next_ver = i
                break



        return True


class GrafMurav:
    def __init__(self, speed, size_pop=10, max_iter=20, alpha=1, beta=2, rho=0.1):
        self.speed = speed
        self.size_pop = size_pop  # количество муравьёв
        self.max_iter = max_iter  # количество итераций
        self.rebs = []
        self.murs = []
        self.alpha = alpha  # коэффициент важности феромонов в выборе пути
        self.beta = beta  # коэффициент значимости расстояния
        self.rho = rho  # скорость испарения феромонов

    def get_rebs_from_matrix(self, m):
        self.rebs = []
        for i in range(len(m)):
            s = {}
            for j in range(len(m[i])):
                if d[i][j] != 0:
                    if i > j:
                        s.update({j: self.rebs[j][i]})
                    else:
                        s.update({j: reb(d[i][j], i, j)})
            self.rebs.append(s)

    def create_murs(self, n):
        self.murs = []
        for i in range(self.size_pop):
            self.murs.append(mur(self.speed, self.rebs, 0))
            self.murs[i].set_new_reb(self.rebs[0])


    def run(self):
        for _ in range(self.max_iter):

            self.create_murs(self.size_pop)


            while True:
                dm = []
                for j in range(len(self.murs)):
                    if not self.murs[j].upd():
                        dm.append(j)




                for j in range(len(dm)):
                    self.murs.pop(dm[j] - j)

                if len(self.murs) == 0:
                    break


                for j in self.rebs:
                    for k in j.values():
                        k.upd(self.rho)





if __name__ == "__main__":
    speed = 1
    n = 10

    d = [[0, 1, 2, 4, 3],
         [1, 0, 4, 2, 1],
         [2, 4, 0, 1, 1],
         [4, 2, 1, 0, 2],
         [3, 1, 1, 2, 0]]

    rebs = []

    gg = GrafMurav(1)

    gg.get_rebs_from_matrix(d)

    gg.run()

    G= nx.Graph()



    for i in range(len(d)):
        for j in gg.rebs[i].keys():
            if i < j:
                G.add_edge(*gg.rebs[i][j].vers, weight= gg.rebs[i][j].fer/ 100)
                print(gg.rebs[i][j].fer)


    edges = G.edges()

    weights = [G[u][v]['weight'] for u, v in edges]
    pos = nx.circular_layout(G)
    subax1 = plt.subplot(121)

    nx.draw(G, pos, with_labels=True,  width=weights)

    plt.show()
