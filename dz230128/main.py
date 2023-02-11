from typing import Dict, List, Union


class Vertex:
    def __init__(self, name):
        self.name = name
        self.marked = False

        #вспомогательная переменная для алгоритма дийкстры
        #минимальный путь до вершины
        self.weight = None

    # условие схожести
    def __eq__(self, v):
        #для вершин
        if isinstance(v, Vertex):
            return self.name == v.name

        # для названия str
        if isinstance(v, str):
            return self.name == v

class Edge:
    def __init__(self, v1, v2, w):
        self.v1 = v1
        self.v2 = v2
        self.weight = w


class Graph:
    def __init__(self, sa: dict[str: list]):
        self._sa = sa  # список смежности
        self._vertices = list([Vertex(el) for el in sa.keys()])  # список вершин
        self._d = {el.name: el for el in self._vertices} # словарь этих вершин
        self._edges = self._get_edges() # список ребер

    #создаем свписок ребер
    def _get_edges(self):
        edges = []
        for v, vs in self._sa.items():
            for vi, wi in vs:
                edges.append(Edge(self._d[v], self._d[vi], wi))
        return edges


    #получить вершину по имени
    def get_vertix(self, name):
        return self._d[name]

    def get_vertex_with_min_weight_not_marked(self):
        # возвращает не пройденную вершину с минимальным весом
        a = [(el.weight, el) for el in self._d.values() if not el.marked]
        if len(a) != 0:
            return min(a)[1]
        return None



    def get_weights_edges(self):
        # возвращает список весов всех ребер
        return list([el.weight for el in self._edges])

    def vertices(self):
        # возвращает список вершин
        return self._vertices

    def adjacency_nodes_ribbles(self, v):
        #возращает список смежных с вершиной вершин и ребер
        a = []
        for name, w in self._sa[v.name]:
            a.append((self.get_vertix(name), w))
        return a


def dijkstra(g, v0: str):
    #создаем граф из списка смежностей
    g = Graph(g)

    s = sum(g.get_weights_edges()) + 1

    # устанавливает для v0 вес в 0 а для остальных вес в сумма всех весов + 1
    for v in g._vertices:
        if v== v0:
            v.weight = 0
        else:
            v.weight = s

    #выходной словарь
    out = {}

    while True:
        # Выбираем вершину с минимальным весом не пройденную
        v = g.get_vertex_with_min_weight_not_marked()
        if v is None:
            break

        # Идем по смежным к ней вершинам не пройденным
        for vi, wi in g.adjacency_nodes_ribbles(v):
            if not vi.marked:
                #      Обновляем веса min(было, стало)
                if vi.weight is not None:
                    vi.weight = min(vi.weight, v.weight + wi)
                else:
                    vi.weight = v.weight + v.adjacency[vi.name]
        # Помечаем вершину как пройденную
        v.marked = True

        #добавляем в словарь пройденных так как вес уже не обновится
        out.update({v.name: v.weight})

    return out


if __name__ == '__main__':
    g = {'1': [['2', 3], ['3', 4]], '2':[['1',3],['3',7]], '3':[['2',7], ['1',4]]}
    print(dijkstra(g , '2'))