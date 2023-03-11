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

k = 6000

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

# class Cassa:
#     def __init__(self):
#         self.r = r

class Point:
    def __init__(self):
        self.ismoved = False
        self.shush = None
        self.newshush = None


    def move(self):
        if self.shush is not None:
            return self.shush.upd()
        else:
            return None



def upd_map(map):
    q = []

    p = [random.randint(0, H//block - 1), random.randint(0, W//block - 1)]

    while map[p[0]][p[1]].shush is not None:
        p = [random.randint(0, H // block - 1), random.randint(0, W // block - 1)]

    q.append(p)

    while len(q)> 0:

        p = q[0]
        nq = []
        nq.append([(p[0] - 1) % (H//block), p[1]])
        nq.append([(p[0] + 1) % (H//block), p[1]])
        nq.append([p[0], (p[1] - 1) % (W//block)])
        nq.append([p[0], (p[1] + 1) % (W//block)])

        b = map[p[0]][p[1]].shush is None

        nnq = []
        for i in nq:
            k = map[i[0]][i[1]]

            if k.ismoved == False:
                d = k.move()
                if d is not None:
                    if [(d[0] + i[0]) % (H//block), (d[1] + i[1])% (W//block)] == p:
                        if b:
                            b = False
                            map[p[0]][p[1]].shush = k.shush
                            k.shush = None

                nnq.append(i)


        map[p[0]][p[1]].ismoved = True
        for i in nnq:
            if i not in q:
                q.append(i)
        q.pop(0)




def draw_map(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
            p = map[i][j]
            p.ismoved = False
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