from collections import defaultdict
import pygame
import random
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

import matplotlib
matplotlib.use("Agg")

import matplotlib.backends.backend_agg as agg
import pylab
import matplotlib.pyplot as plt

from copy import copy, deepcopy


plt.rcParams.update({
    #"lines.marker": "o",         # available ('o', 'v', '^', '<', '>', '8', 's', 'p', '*', 'h', 'H', 'D', 'd', 'P', 'X')
    "lines.linewidth": "1.8",
    "axes.prop_cycle": plt.cycler('color', ['white']),  # line color
    "text.color": "white",       # no text in this example
    "axes.facecolor": "black",   # background of the figure
    "axes.edgecolor": "lightgray",
    "axes.labelcolor": "white",  # no labels in this example
    "axes.grid": "True",
    "grid.linestyle": "--",      # {'-', '--', '-.', ':', '', (offset, on-off-seq), ...}
    "xtick.color": "white",
    "ytick.color": "white",
    "grid.color": "lightgray",
    "figure.facecolor": "black", # color surrounding the plot
    "figure.edgecolor": "black",
})


WIDTH = 500
HEIGHT = 500
WIDTH_OBJECT = 10
HEIGHT_OBJECT = 10
FPS = 300
# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class GraphicObject:
    def __init__(self, *args, name=""):
        self.fig = pylab.figure(figsize=[4, 4],  # Inches
                           dpi=100,# 100 dots per inch, so the resulting buffer is 400x400 pixels
                           )
        self.ax = self.fig.gca()
        self.ax.plot(*args)
        self.name = name
        self.ax.set_title(self.name)


        self.canvas = agg.FigureCanvasAgg(self.fig)
        self.canvas.draw()
        self.renderer = self.canvas.get_renderer()
        self.raw_data = self.renderer.tostring_rgb()

        plt.close()

    def draw(self,screen, x=1050, y=0):
        # screen = pygame.display.get_surface()
        size = self.canvas.get_width_height()
        surface = pygame.image.fromstring(self.raw_data, size, "RGB")
        screen.blit(surface, (x, y))


class GameObject:
    def __init__(self, xy, number):
        self.number = number
        self.x, self.y = xy
        self.color = None
        self.w = WIDTH_OBJECT
        self.h = HEIGHT_OBJECT

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x*self.w, self.y*self.h, self.w, self.h))

    def __eq__(self, other):
        return other.number == self.number

class Alg:
    def __init__(self, w=None):
        if w is None:
            len_w = [75, 20, 9]
            self.w = []
            for i in range(len(len_w) - 1):
                self.w.append(np.random.random((len_w[i], len_w[i + 1])) * 2 - 1)

            # 7600 + 10000 + 2000 + 180
        else:
            self.w = w
        self.last_move = None

        self.d_move = {
            0: np.array((1, -1)),  # вправо-вверх
            1: np.array((0, 1)),  # идти вниз
            2: np.array((1, 0)),  # идти вправо
            3: np.array((0, -1)),  # идти вверх
            4: np.array((-1, 0)),  # идти вниз
            5: np.array((1, 1)),  # вправо-вниз
            6: np.array((-1, -1)),  # влево-вверх
            7: np.array((-1, 1)),  # влево-вниз
            8: np.array((0, 0)),  # влево-вниз

        }

    def sigmoid(self, Z):
        return 1 / (1 + np.exp(-Z))

    def get_move(self, a):
        for i in range(len(self.w)):
            a = self.sigmoid(a.dot(self.w[i]))

        rr = np.where(a == np.max(a))[0][0]
        return self.d_move[rr]

    def mutation(self):

        for i in range(len(self.w)):
            p = (np.random.random(self.w[i].shape) > 0.9).astype(int)
            self.w[i][p == 1] += (np.random.rand() * 2 - 1) * 0.1

    def sex(self, u1, u2):
        w1 = u1.get_w()
        w2 = u2.get_w()
        for i in range(len(self.w)):
            for j in range(len(self.w[i])):
                for k in range(len(self.w[i][j])):
                    self.w[i][j][k] = w1[i][j][k]
                    if random.randint(0, 2) > 1:
                        w1, w2 = w2, w1

    def get_w(self):
        return self.w


class Person(GameObject):
    def __init__(self, xy, number, w=None):
        super().__init__(xy, number)
        self.energy = grass_men_energy + random.randint(-2, 2)
        self.alg = Alg(w=None)
        self.age = 0
        self.eaten = 0

    def add_energy(self, val=1):
        self.energy += val
        self.eaten += 1

    def spend_energy(self):
        self.energy -= 1
        self.age += 1

    def get_slide(self, a):
        b = np.zeros((5,5))
        for i in range(-2, 3):
            for j in range(-2, 3):
                m = a[(self.x + i) % a.shape[0], (self.y + j) % a.shape[1]]
                if m < 0:
                    m = 0
                b[i + 2, j+ 2] = m
        return b

    def get_move(self, m1, m2, m3):
        a = np.concatenate([self.get_slide(m1).reshape((-1,)), self.get_slide(m2).reshape((-1,)), self.get_slide(m3).reshape((-1,))], axis=0)
        self.spend_energy()
        return self.alg.get_move(a)

    def mutation(self):
        self.alg.mutation()

    def get_w(self):
        return self.alg.get_w()


class Grass(GameObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = GREEN
        self.count = 0
        self.imeat = False

    def eat(self):
        self.imeat = True
        self.count = grass_rise_time

    def draw(self, surface):
        if not self.imeat:
            super().draw(surface)

    def update(self):
        if self.imeat:
            self.count -= 1
            if self.count <= 0:
                self.imeat = False



class Herbivore(Person):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = BLUE


class Predator(Person):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = RED
        self.energy = meat_man_energy


class World:
    def __init__(self):
        self.count_object = 0
        self.shape = (WIDTH//WIDTH_OBJECT, HEIGHT//HEIGHT_OBJECT)
        # self.field = np.zeros(self.shape)
        self.grass = (np.random.random(self.shape) > 0.8).astype(int)
        self.grass_dict = self.create_obj(self.grass, Grass)
        self.herbivore = (np.random.random(self.shape) > 0.99  ).astype(int)
        self.herbivore_dict = self.create_obj(self.herbivore, Herbivore)
        self.predator = (np.random.random(self.shape) > 0.996).astype(int)
        self.predator_dict = self.create_obj(self.predator, Predator)
        self.herbivore_deaded_count = 0
        self.predator_deaded_count = 0

    def create_obj(self, m, Obj):
        res = defaultdict(list)
        for el in np.argwhere(m == 1):
            res[tuple(el)].append(Obj(el, self.count_object))
            self.count_object += 1
        return res

    def world_logic(self):

        for el in self.grass_dict.values():
            for eg in el:
                eg.update()

        for el in np.argwhere(self.grass == -1):
            el = tuple(el)
            for eg in self.grass_dict[el]:
                if not eg.imeat:
                    self.grass[el] = len(self.grass_dict[el])

        for el in np.argwhere((self.grass > 0) & (self.herbivore > 0)):
            el = tuple(el)
            # print("del grass", el)
            self.grass[el] = -1
            count_grass = len(self.grass_dict[el])
            for grass in self.grass_dict[el]:
                grass.eat()
            count_herb = len(self.herbivore_dict[el])
            for eh in self.herbivore_dict[el]:
                eh.add_energy(val=count_grass * energy_for_food / count_herb)

        for el in np.argwhere((self.herbivore > 0) & (self.predator > 0)):
            el = tuple(el)
            # print("del herbivore", el)
            self.herbivore[el] = 0
            count_herb = sum([kp.energy for kp in self.herbivore_dict[el]]) / 20
            del self.herbivore_dict[el]
            count_pred = len(self.predator_dict[el])
            for ep in self.predator_dict[el]:
                ep.add_energy(val=count_herb * energy_for_meat / count_pred)

        key_list = list(self.herbivore_dict)
        for xy in key_list:
            for i, eh in enumerate(self.herbivore_dict[xy]):
                if eh.energy <= 0:
                    # print("null energy herbivore", xy)
                    self.herbivore[xy] -= 1
                    self.herbivore_dict[xy].remove(eh)

        key_list = list(self.predator_dict)
        for xy in key_list:
            for i, ep in enumerate(self.predator_dict[xy]):
                if ep.energy <= 0:
                    # print("null energy herbivore", xy)
                    self.predator[xy] -= 1
                    self.predator_dict[xy].remove(ep)

    def move(self):
        dd = np.sum(np.sum(self.herbivore)) <= dd_porog
        # dd = sum([len(el) for el in self.herbivore_dict.values()]) <= 10

        if dd:

            self.herbivore_deaded_count += 1

            a = []
            b = []
            s = 0
            list_herbivore = deepcopy(self.herbivore_dict).items()
            for xy, el in list_herbivore:
                for i, eh in enumerate(el):
                    a.append(eh)
                    b.append(eh.eaten)
                    s += eh.eaten
            print(s)
            b = np.array(b)


            self.herbivore = (np.random.random(self.shape) > 0.99).astype(int)
            self.herbivore_dict = self.create_obj(self.herbivore, Herbivore)
            self.count_object = 0


            for xy, el in self.herbivore_dict.items():
                for i, eh in enumerate(el):

                    u1, u2 = None, None
                    while u1 == u2:
                        u1 = random.choices(a, weights=b)[0]
                        u2 = random.choices(a, weights=b)[0]

                    eh.alg.sex(u1.alg, u2.alg)

                    eh.mutation()



        else:
            a = []
            b = []
            s = 0
            list_herbivore = deepcopy(self.herbivore_dict).items()
            for xy, el in list_herbivore:
                for i, eh in enumerate(el):
                    delta = eh.get_move(self.grass, self.herbivore, self.predator)
                    self.herbivore[xy] -= 1
                    eh.x += delta[0]
                    eh.x = eh.x % (WIDTH // WIDTH_OBJECT)
                    eh.y += delta[1]
                    eh.y = eh.y % (HEIGHT // HEIGHT_OBJECT)
                    self.herbivore[(eh.x, eh.y)] += 1
                    self.herbivore_dict[xy].remove(eh)
                    self.herbivore_dict[(eh.x, eh.y)].append(eh)

                    a.append(eh)
                    b.append(eh.eaten)
                    s += eh.eaten

            b = np.array(b)

            for xy, el in list_herbivore:
                for i, eh in enumerate(el):

                    if eh.energy >= energy_for_sex_with_yourself:
                        eh.energy -= grass_men_energy
                        new_h = Herbivore(xy, self.count_object, w=eh.get_w())

                        u2 = eh
                        while u2 == eh:
                            u2 = random.choices(a, weights=b)[0]

                        new_h.alg.sex(eh.alg, u2.alg)

                        new_h.mutation()
                        self.herbivore_dict[xy].append(new_h)
                        self.count_object += 1
                        self.herbivore[xy] += 1

        dd = np.sum(np.sum(self.predator)) <= dd_porog
        if dd:
            self.predator_deaded_count += 1
            a = []
            b = []
            s = 0
            list_herbivore = deepcopy(self.predator_dict).items()
            for xy, el in list_herbivore:
                for i, eh in enumerate(el):
                    a.append(eh)
                    b.append(eh.eaten)
                    s += eh.eaten
            print(s)
            b = np.array(b)

            self.predator = (np.random.random(self.shape) > 0.99).astype(int)
            self.predator_dict = self.create_obj(self.predator, Predator)
            self.count_object = 0

            for xy, el in self.predator_dict.items():
                for i, eh in enumerate(el):

                    u1, u2 = None, None
                    while u1 == u2:
                        u1 = random.choices(a, weights=b)[0]
                        u2 = random.choices(a, weights=b)[0]

                    eh.alg.sex(u1.alg, u2.alg)

                    eh.mutation()

        else:
            list_predator = deepcopy(self.predator_dict).items()
            for xy, el in list_predator:
                for i, ep in enumerate(el):
                    delta = ep.get_move(self.grass, self.herbivore, self.predator)
                    self.predator[xy] -= 1
                    ep.x += delta[0]
                    ep.x = ep.x % (WIDTH // WIDTH_OBJECT)
                    ep.y += delta[1]
                    ep.y = ep.y % (HEIGHT // HEIGHT_OBJECT)
                    self.predator[(ep.x, ep.y)] += 1
                    self.predator_dict[xy].remove(ep)
                    self.predator_dict[(ep.x, ep.y)].append(ep)
                    if ep.energy >= energy_for_sex_with_yourself:
                        ep.energy -= meat_man_energy
                        new_p = Predator(xy, self.count_object, w=ep.get_w())
                        new_p.mutation()
                        self.predator_dict[xy].append(new_p)
                        self.count_object += 1
                        self.predator[xy] += 1

    def get_stat(self):
        return (
                np.sum(np.sum(self.grass[self.grass > 0])),
                np.sum(np.sum(self.herbivore)),
                np.sum(np.sum(self.predator)),
                sum([eh.energy for el in self.herbivore_dict.values() for eh in el]),
                sum([ep.energy for el in self.predator_dict.values() for ep in el]),
                self.herbivore_deaded_count,
                self.predator_deaded_count
                )

            # (sum([len(el) for el in self.grass_dict.values() if len(el) and not el[0].imeat]),
            #     sum([len(el) for el in self.herbivore_dict.values()]),
            #     sum([len(el) for el in self.predator_dict.values()]),


class WorldEvolution:
    def __init__(self):

        self._init_pygame()
        self.screen = pygame.display.set_mode((900, 500))
        self.background = BLACK
        self.clock = pygame.time.Clock()
        self.world = World()
        self.k = 0

        self.paused = False

        self.max_meat_man_age = 0
        self.max_grass_man_age = 0

        self.age = 0


        self.font = pygame.font.Font(None, 24)

        self.current_block = ()


    def main_loop(self):
        while True:
            if not self.paused:
                self._process_game_logic()
                self.age += 1
            #print(self.clock.get_fps())
            self.clock.tick(FPS)
            self._handle_input()
            self._draw()
            self._draw_stats()
            #self._draw_grafs()


            pygame.display.flip()

    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("Эволюция!")

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.paused = not self.paused
            p = pygame.mouse.get_pos()

            self.current_block = (p[0] // WIDTH_OBJECT, p[1] // HEIGHT_OBJECT)


    def _process_game_logic(self):
        self.world.world_logic()
        self.world.move()
        x1,x2,x3,x4,x5,x6,x7 = self.world.get_stat()
        self.x1 = x1
        self.x2=x2
        self.x3=x3
        self.x4=x4
        self.x5=x5
        self.x6=x6
        self.x7=x7
        self.x=self.k
        self.k += 1

    def _draw(self):
        self.screen.fill(self.background)
        for el in self.world.grass_dict.values():
            for eg in el:
                eg.draw(self.screen)
        for el in self.world.herbivore_dict.values():
            for eh in el:
                eh.draw(self.screen)
        for el in self.world.predator_dict.values():
            for ep in el:
                ep.draw(self.screen)

    def _draw_grafs(self):
        GraphicObject(self.x_list, self.x1_list, "green",
                      self.x_list, self.x2_list, "blue",
                      self.x_list, self.x3_list, "red", name="Cущности").draw(self.screen, 1030, 0)

        GraphicObject(self.x_list[-100:], self.x1_list[-100:], "green",
                      self.x_list[-100:], self.x2_list[-100:], "blue",
                      self.x_list[-100:], self.x3_list[-100:], "red", name="Cущности за 100 циклов").draw(self.screen, 1030, 400)

        GraphicObject(self.x_list, self.x6_list, "blue",
                      self.x_list, self.x7_list, "red", name="Число вымераний").draw(self.screen, 1450, 0)

        GraphicObject(self.x_list, self.x4_list, "blue",
                      self.x_list, self.x5_list, "red", name="Энергиия").draw(self.screen, 1450, 400)

    def _draw_stats(self):
        crx = 550
        cry = 20
        # pygame.draw.rect(self.screen,(255, 0, 0), (crx, cry, 10, 10))
        pygame.draw.rect(self.screen, (0, 0, 255), (crx, cry + 30, 10, 10))
        pygame.draw.rect(self.screen, (0, 255, 0), (crx, cry + 60, 10, 10))

        # text = self.font.render("Хищники", False,
        #                   (255, 255, 255))
        # self.screen.blit(text, (crx + 15, cry - 5))

        text = self.font.render("Травоядные", False,
                                 (255, 255, 255))
        self.screen.blit(text, (crx + 15, cry + 25))

        text = self.font.render("Трава", False,
                                 (255, 255, 255))
        self.screen.blit(text, (crx + 15, cry + 55))


        # prages = [self.max_meat_man_age]
        # for el in self.world.predator_dict.values():
        #     for eg in el:
        #         prages.append(eg.age)
        # self.max_meat_man_age = max(prages)
        # text = self.font.render("Максимальный возвраст мясоеда  " + str(self.max_meat_man_age), False,
        #                         (255, 255, 255))
        # self.screen.blit(text, (crx, cry + 120))

        prages = [self.max_grass_man_age]
        for el in self.world.herbivore_dict.values():
            for eg in el:
                prages.append(eg.age)
        self.max_grass_man_age = max(prages)

        text = self.font.render("Максимальный возвраст травоеда " + str(self.max_grass_man_age), False,
                                (255, 255, 255))
        self.screen.blit(text, (crx, cry + 150))

        text = self.font.render("Вымерания травоядных " + str(self.x6), False,
                                (255, 255, 255))
        self.screen.blit(text, (crx, cry + 200))

        # text = self.font.render("Вымерания мясоядных " + str(self.x7), False,
        #                         (255, 255, 255))
        # self.screen.blit(text, (crx, cry + 230))

        cp = self.world.predator_dict.get(self.current_block)
        if cp is None:
            cp = []

        ch = self.world.herbivore_dict.get(self.current_block)
        if ch is None:
            ch = []

        i = 0
        while i < len(cp):
            text = self.font.render("Хищник: энергия = " + str(cp[i].energy) + " возвраст = " + str(cp[i].age), False,
                                    (255, 255, 255))
            self.screen.blit(text, (crx, cry + 250 + i * 30))
            i += 1

        j = 0
        while j < len(ch):
            text = self.font.render("Травоядное: энергия = " + str(ch[j].energy) + " возвраст = " + str(ch[j].age), False,
                                    (255, 255, 255))
            self.screen.blit(text, (crx, cry + 250 + (i + j) * 30 ))
            j += 1

        text = self.font.render("Год " + str(self.age), False,
                                (255, 255, 255))
        self.screen.blit(text, (crx, cry + 230 ))



if __name__ == "__main__":
    grass_rise_time = 170

    grass_men_energy = 50
    meat_man_energy = 30

    energy_for_sex_with_yourself = 100

    energy_for_food = 8
    energy_for_meat = 1

    dd_porog = 10

    world_evolution = WorldEvolution()
    world_evolution.main_loop()


# 1. Подписать графики и оси на них
# 2. Изменить название x_list, x итд. , сделать d_move статическим свойством класса
# 3. Выделить те константы которые являются параметрами в отдельные переменные.
#                      Подобрать параметры чтобы не вымирали (не факт что получится)
# 4. Сделать вывод информации о квадратике в правый нижний угол при наведении на него мышкой:
#                         номер, тип, сколько циклов живет, какая энергия
# 5. Выводить внизу еще правее - максимальную длинну жизни травоядного и хищника, максимальную энергию
# 6. Написать алгоритм для хищников, который бы выигрывал хищников по-умолчанию и не вымирал
#        изначально 1, но может размножаться. (не изменяется при наследовании)
# 7. Написать алгоритм для травоядных который бы выигрывал травоядных по-умолчанию и не вымирал
#        изначально 1, но может размножаться. (не изменяется при наследовании)
# 8. Расширить поле видимости с 5на5 до 7 на 7.
# 9. Добавить возможность играть за травоядного или хищника и сохранять при этом что получает на вход нейросеть и ваш ход

# 1,2,[3] - 1 бал
# 4,5 - 1 бал
# 6 - 1 бал
# 7,8 - 1 бал
# 9 - 1 бал