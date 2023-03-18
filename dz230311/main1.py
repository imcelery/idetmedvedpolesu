import random
import matplotlib.pyplot as plt
import pygame



W = 800
H = 800

FPS = 200
block = 10  # ширина змеи

# цвета в rgb
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (120, 120, 120)

k = 1000

r = 2

u = 20



class Shushun:
    def __init__(self,dir = None):
        self.rab = False
        self.ismoved = False
        self.cassa = [0, 0]
        self.isupd = False
        if dir == None:
            self.newdirect()
        else:
            self.direct = dir


    def newdirect(self):
        d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        self.direct = d[random.randint(0, len(d)-1)]


    def upd(self, p):
        if self.rab:
            y = self.cassa[0] - p[0]
            x = self.cassa[1] - p[1]
            if y == 0:
                my = 0
            else: my = y//abs(y)
            if x == 0:
                mx = 0
            else: mx =x//abs(x)
            self.direct = [my,mx]
        elif not self.isupd:
            self.isupd = True
            c = random.randint(0, 10)
            if c >= 9:
                self.newdirect()
        return self.direct

class Point:
    def __init__(self):
        self.isupd = False
        self.shush = None
        self.cassa = None


    def upd(self, p):
        if self.shush is not None:
            return self.shush.upd(p)
        else:
            return None



def upd_map(map):
    q = []
    p = [0, 0]
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j].cassa is True:
                for k in range(2 * r + 1):
                    for e in range(2 * r + 1):
                        d = map[(i - r + k)%(H//block)][(j - r + e)%(W//block)]
                        if d.shush is not None:
                            d.shush.rab = True
                            d.shush.cassa = [i, j]
            if map[i][j].shush is not None:
                p = [i,j]

    q.append(p)

    while len(q)> 0:

        p = q[0]
        nq = []
        f = [[-1, -1], [-1, 0], [-1, 1],
             [0, -1],          [0, 1],
             [1, -1], [1, 0], [1, 1],]
        for i in f:
            nq.append([(p[0] + i[0]) % (H//block),(p[1] + i[1]) % (W//block)])

        b = map[p[0]][p[1]].shush is None

        nnq = []
        for i in nq:
            k = map[i[0]][i[1]]


            d = k.upd([i[0], i[1]])
            if d is not None:
                if not k.shush.ismoved:
                    if [(d[0] + i[0]) % (H//block), (d[1] + i[1])% (W//block)] == p:
                        if b:
                            b = False
                            map[p[0]][p[1]].shush = k.shush
                            k.shush = None
                            map[p[0]][p[1]].shush.ismoved = True

            if k.isupd == False:
                nnq.append(i)


        map[p[0]][p[1]].isupd = True
        for i in nnq:
            if i not in q:
                q.append(i)
        q.pop(0)




def draw_map(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
            p = map[i][j]
            p.isupd = False
            if p.shush is not None:
                pygame.draw.rect(screen, RED, (j * block, i * block, block, block))
                p.shush.ismoved = False
                p.shush.isupd = False
            if p.cassa:
                pygame.draw.rect(screen, GRAY, (j * block, i * block, block, block))

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

    i = u
    while i > 0:
        d = map[random.randint(0, H // block - 1)][random.randint(0, W // block - 1)]
        if d.cassa is None:
            d.cassa = True
            i -= 1

    i = k
    while i > 0:
        d = map[random.randint(0, H//block - 1)][random.randint(0, W//block - 1)]
        if d.shush is None and not d.cassa:
            d.shush = Shushun()
            i -= 1


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
        print(clock.get_fps())
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