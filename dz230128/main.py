from typing import Dict, List, Union


class Vertex:
    def __init__(self, name, adjacency):
        self.name = name
        self.marked = False

        #вспомогательная переменная для алгоритма дийкстры
        #минимальный путь до вершины
        self.weight = None

        #словарь всех вершин рядом по имени
        self.adjacency = adjacency


class Graph:
    def __init__(self, sa: dict[str: list]):
        self._sa = sa  # список смежности
        self._vertices = self.get_vertices_from_sa() #список вершин

    #создаем свписок вершин
    def get_vertices_from_sa(self):
        d = {}
        for i in self._sa.keys():
            #словарь смежных вершин
            ad = {}
            for j in self._sa[i]:
                ad.update({j[0]: j[1]})
            d.update({i: Vertex(i, ad)})
        return d

    #получить вершину по имени
    def get_vertix(self, name):
        return self._vertices[name]

    def get_vertex_with_min_weight_not_marked(self):
        # возвращает не пройденную вершину с минимальным весом
        a = [(el.weight, el) for el in self._vertices.values() if not el.marked and el.weight is not None]
        if len(a) != 0:
            return min(a)[1]
        return None


    def vertices(self):
        # возвращает список вершин
        return self._vertices


    def adjacency_nodes(self, v:Vertex):
        #возращает смежные к вершине вершины
        a = self.get_vertix(v.name)
        return [self.get_vertix(el) for el in a.adjacency.keys()]

    def dijkstra(self, v0: str):


        # устанавливает для v0 вес в 0 а для остальных вес будет None
        self.get_vertix(v0).weight = 0

        #выходной словарь
        g = {}

        while True:
            # Выбираем вершину с минимальным весом не пройденную
            v = self.get_vertex_with_min_weight_not_marked()
            if v is None:
                break

            # Идем по смежным к ней вершинам не пройденным
            for vi in self.adjacency_nodes(v):
                if not vi.marked:
                    #      Обновляем веса min(было, стало)
                    if vi.weight is not None:
                        vi.weight = min(vi.weight, v.weight + v.adjacency[vi.name])
                    else:
                        vi.weight = v.weight + v.adjacency[vi.name]
            # Помечаем вершину как пройденную
            v.marked = True

            #добавляем в словарь пройденных так как вес уже не обновится
            g.update({v.name: v.weight})

        #отчищаем веса для следующих прогонов
        for i in self._vertices.values():
            i.weight = None
            i.marked = False
        return g


# если честно не понял вашу реализацию. изза большого количества классов данные были бы плохо связанны между собой и дулировались
# поэтому я отказался от класса ребер
if __name__ == '__main__':
    g = Graph({1: [[2, 3], [3, 4]], 2:[[1,3],[3,7]], 3:[[2,7], [1,4]]})
    print(g.dijkstra(1))