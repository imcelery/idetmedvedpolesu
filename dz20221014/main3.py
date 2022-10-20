from random import randint
from random import shuffle

import numpy
import numpy as np



class InputCommon:
    def input(self):
        return input()


class OutputCommon:
    def output(self, val):
        print(val)


class Hero:
    def __init__(self, pos):
        self.pos = pos
        self.rot = 0
        # чтобы удобнее было брать соседние ячейки
        self._costil = np.array([(1, 0), (0, -1), (-1, 0), (0, 1)])

    def right(self):
        self.rot += 1
        self.rot %= 4

    def left(self):
        self.rot -= 1
        self.rot %= 4

    def forward(self):
        self.pos += self._costil[self.rot]

    @property
    def forward_pos(self):
        return self.pos + self._costil[self.rot]


class Lab:
    def __init__(self, width: int, height: int, fill_persent : int):
        self.width = width
        self.height = height
        self.shape = (height, width)
        self.fill_persent = fill_persent
        self.map = None
        self.start_pos = np.array([randint(1, height - 2), randint(1, width - 2)])


    def generate(self):
        generator = GenerateLab(self.width, self.height, self.fill_persent, self.start_pos)
        self.map = generator.generate()

    def on_finish(self, hero: Hero) -> bool:
        return self.map[hero.pos[0], hero.pos[1]] == 3

    def forward_info(self, hero: Hero):
        return self.map[hero.forward_pos[0], hero.forward_pos[1]]

    def printmap(self):
        graf = {0: "@", 1: "_", 2: "b", 3: "w"}
        for i in range(self.height):
            a = ""
            for j in range(self.width):
                a += graf.get(self.map[i, j])
                a += " "
            print(a)


class GenerateLab:
    def __init__(self, width: int, height: int, fill_persent: int, start_pos):
        self.width = width
        self.height = height
        self.fill_persent = fill_persent
        self.tons = []
        self._costil = np.array([(1, 0), (0, -1), (-1, 0), (0, 1)])
        self.map = np.zeros((height, width))

        self.start_pos = start_pos
        self.map[self.start_pos[0], self.start_pos[1]] = 1

    @property
    def count_cells(self):
        return self.width * self.height

    def into_map(self, x, y):
        return 0 < x < self.height - 1 and 0 < y < self.width - 1

    def generate(self):
        previoustons = [list(self.start_pos)]
        self.tons = previoustons.copy()

        s = self.count_cells
        while len(self.tons) / s < self.fill_persent / 100:  # пока не закрасим нужный процент точек
            while len(previoustons) != 0:
                previoustons = self.get_new_tons(previoustons)
                for i in range(len(previoustons)):
                    if not previoustons[i] in self.tons:

                        self.tons.append(previoustons[i])
        # если мы не нашли ячейку для окраски
        # то стартуем с рандомной точки в нашем пути
            previoustons = [self.tons[randint(0, len(self.tons) - 1)]]

        return self.map

    def get_new_tons(self, previoustons):
        newtons = []
        for i in range(len(previoustons)):
            # считаем сколько нулей вокруг текущей ячейки
            m = []
            for k in range(len(self._costil)):
                xy = np.array([previoustons[i][ 0] + self._costil[k, 0], previoustons[i][1] + self._costil[k, 1]])
                if self.map[xy[0], xy[1]] == 0:
                    # запоминаем в какую сторону был ноль
                    m.append(k)
            h = 0
            while m:
                # берем случайную сторону с нулем
                a = randint(0, len(m) - 1)
                # если мы еще в этом цикле не добавили единицы к массиву
                # и ноль был только в одну сторону
                # или с вероятностью 1/100 заходим в условие
                if (h == 0 and len(m) == 1) or randint(0, 100) == 1:
                    # запомнили координаты точки с нулем
                    bc = np.array([previoustons[i][0] + self._costil[m[a]][0], previoustons[i][1] + self._costil[m[a]][1]])

                    # если она попадает в массив (без крайних точек)
                    if self.into_map(*bc):
                        # то запоминаем кто из ее соседей закрашена единицей
                        f = []
                        for k in range(len(self._costil)):
                            xy = np.array([bc[0] + self._costil[k][0], bc[1] + self._costil[k][1]])
                            if self.map[xy[0], xy[1]] == 1:
                                f.append(k)
                        # если такой сосед всего один
                        if len(f) == 1:

                            # то наша нулевая точка продолжение пути
                            self.map[bc[0], bc[1]] = 1
                            # запоминаем ее
                            newtons.append(list(bc))
                            h += 1
                        # если таких соседа два
                        elif len(f) == 2:
                            # и соседи на противоположных сторонах
                            d = abs(f[0] - f[1])
                            if d == 2:
                                # соединяем их окрашивая в единицу
                                self.map[bc[0], bc[1]] = 1
                                newtons.append(list(bc))
                                h += 1
                            # если соседи 90 градусов друг другу
                            else:
                                # и еще не соединены
                                if self.map[bc[0] + self._costil[f[0], 0] + self._costil[f[1], 0], bc[1] + self._costil[f[0], 1] + self._costil[f[1], 1]] == 0:
                                    # соединяем их
                                    self.map[bc[0], bc[1]] = 1
                                    newtons.append(list(bc))
                                    h += 1
                # обработали сторону с нулем забываем про нее
                m.pop(a)
        return newtons






class Game:
    def __init__(self):
        self.__intro = """Ты - крот, который немножко заблудился. Твоя задача - 
на ощупь найти выход из подземных тунелей. 
Ты можешь: двигаться вперед командой - 'w' и поворачивать вправо и 
влево на 90 градусов командами 'r' и 'l' соответственно.
Удачи в поисках выхода."""
        self.out = OutputCommon()
        self.input = InputCommon()
        self.do_dict = {
            "w": self.do_forward,
            "r": self.do_right,
            "l": self.do_left,
        }
        self.hero = None
        self.lab = None
        self.wall_signal = 0

    def _intro(self):
        self.out.output(self.__intro)

    def is_wall(self):
        return self.lab.forward_info(self.hero) == self.wall_signal

    def do_forward(self):
        # если впереди 0 то считаем это стеной
        if self.is_wall():
            self.out.output("Впереди стена")
        else:
            self.out.output("Ты продвинулся")
            self.hero.forward()

    def do_right(self):
        self.hero.right()
        if self.is_wall():
            self.out.output("Ты повернулся вправо, впереди стена")
        else:
            self.out.output("Ты повернулся вправо, впереди нет стены")

    def do_left(self):
        self.hero.left()
        if self.is_wall():
            self.out.output("Ты повернулся влево, впереди стена")
        else:
            self.out.output("Ты повернулся влево, впереди нет стены")

    def win(self):
        self.out.output("Ты ПАБЕДИЛ!!!")

    def start(self):
        self._intro()
        # ширина 10 клеток, высота 10 клеток, процент заполнения тунелями - 20
        self.lab = Lab(10, 10, 20)
        self.lab.generate()
        #self.lab.printmap()
        self.hero = Hero(self.lab.start_pos)
        # пока не дойдем до выхода
        while not self.lab.on_finish(self.hero):
            a = ""
            while a not in self.do_dict:
                a = self.input.input()
            self.do_dict[a]()
        self.win()



if __name__ == '__main__':
    game = Game()
    game.start()