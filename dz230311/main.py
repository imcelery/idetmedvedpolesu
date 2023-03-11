import random
import matplotlib.pyplot as plt
import pygame



W = 800
H = 800

FPS = 20
block = 10  # ширина змеи

# цвета в rgb
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (120, 120, 120)

k = 1000


r = 2



class Shushun:
    def __init__(self,dir = None):
        self.rab = False
        if dir == None:
            self.newdirect()
        else:
            self.direct = dir


    def newdirect(self):
        d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        self.direct = d[random.randint(0, len(d)-1)]


    def upd(self):
        c = random.randint(0, 10)
        if c >= 9:
            self.newdirect()
        return self.direct

class Cassa:
    def __init__(self):
        self.r = r

class Point:
    def __init__(self):
        self.ismoved = False
        self.shush = None
        self.newshush = None

    def move(self):
        if self.shush is not None:
            d = self.shush.upd()
            self.shush = None
            return d
        else:
            return None

    def upd(self):
        self.shush = self.newshush
        self.newshush = None
        self.ismoved = False



def upd_map(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
            d = map[i][j].move()
            if d is not None:
                x = (j + d[0]) % (W // block)
                y = (i + d[1]) % (H // block)
                if map[y][x].newshush is None:
                    map[y][x].newshush = Shushun(d)
                else:
                    if map[i][j].newshush is None:
                        map[i][j].newshush = Shushun(d)
                    else:
                        print("bag")

    for i in range(len(map)):
        for j in range(len(map[0])):
            map[i][j].upd()

def draw_map(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
            p = map[i][j]
            if p.shush is not None:
                pygame.draw.rect(screen, RED, (j * block, i * block, block, block))

if __name__ == '__main__':
    pygame.init()  # инициализируем модуль pygame

    screen = pygame.display.set_mode((W, H))  # получаем объект cодержимого окна с ширной W и высотой H
    pygame.display.set_caption("Игра Змейка")  # устанавливаем у окна заголовок
    clock = pygame.time.Clock()  # получаем объект "часы"
    font_style = pygame.font.SysFont(None, 50)  # получаем объект стиль-текста
    running = True

    map = []
    for i in range(H//block):
        a = []
        for j in range(W // block):
            a.append(Point())
        map.append(a)


    for i in range(k):
        map[random.randint(0, H//block - 1)][random.randint(0, W//block - 1)].shush = Shushun()


    while running:  # основной цикл игры
        # получаем все события, зарегистрированные в игре
        for event in pygame.event.get():
            # если пользователь нажал крестик на окне
            if event.type == pygame.QUIT:
                # прерываем основной цикл (чтобы закрыть потом приложение)
                running = False



        # заполняем область окна белым цветом
        screen.fill(WHITE)

        upd_map(map)

        draw_map(map)


        # отображаем на экране то, что нарисовали
        pygame.display.update()

        clock.tick(FPS)

    # если вышли из основного цикла
    # закрываем pygame
    pygame.quit()

    # plt.plot(data)
    #
    # maxn = 3400
    #
    # data2 = []
    # n = 20
    #
    # k = 0.05
    # for i in range(len(data)):
    #     data2.append(n)
    #     n = n * (1 + k * (maxn - n)/maxn)
    #
    # plt.plot(data2)
    #
    # plt.savefig("2.png")

    quit()