import random
import matplotlib.pyplot as plt
import pygame


timetorise= 50

timetodie = 50

shuneat = 3

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

class Food:
    def __init__(self):
        self.dead = False
        self.timer = 0

    def upd(self):
        if self.dead:
            self.timer += 1
            if self.timer == timetorise:
                self.dead = False
                self.timer = 0

    def eated(self):
        self.dead = True


class Shushun:
    def __init__(self, eaten = 0, dir = None, time = timetodie):
        if dir == None:
            self.newdirect()
        else:
            self.direct = dir
        self.timetodie = time
        self.eatenfood = eaten

    def newdirect(self):
        d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        self.direct = d[random.randint(0, len(d)-1)]

    def eat(self):
        self.eatenfood += 1
        self.timetodie = timetodie

        if self.eatenfood == shuneat:
            self.eatenfood = 0
            return True

        return False

    def upd(self):
        c = random.randint(0, 10)
        if c >= 9:
            self.newdirect()
        self.timetodie -= 1

        if self.timetodie == 0:

            return [0, 0]
        else:
            return self.direct


class Point:
    def __init__(self):
        self.food = Food()
        self.shush = []
        self.newshush = []

    def move(self):
        o = {"shushun" : []}
        for i in self.shush:
            d = i.upd()
            if not d == [0, 0]:
                o["shushun"].append([d, i.eatenfood, i.direct, i.timetodie])
        self.shush = []
        return o


    def upd(self):
        self.shush = self.newshush
        self.newshush = []
        self.food.upd()
        if not self.food.dead and len(self.shush) > 0:
            self.food.eated()
            if self.shush[0].eat():
                self.shush.append(Shushun(0))




def upd_map(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
            d = map[i][j].move()
            for k in d["shushun"]:
                x = (j + k[0][0]) % (W // block)
                y = (i + k[0][1]) % (H // block)
                map[y][x].newshush.append(Shushun(k[1], k[2], k[3]))

    for i in range(len(map)):
        for j in range(len(map[0])):
            map[i][j].upd()

def draw_map(map):
    l = 0
    for i in range(len(map)):
        for j in range(len(map[0])):

            p = map[i][j]
            l += len(p.shush)
            if not p.food.dead:
                pygame.draw.rect(screen, GREEN, (j * block, i * block, block, block))
            if len(p.shush) > 0:
                pygame.draw.rect(screen, RED, (j * block, i * block, block, block))
    return l
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

    map[4][4].shush.append(Shushun(0))

    data = []

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

        l = draw_map(map)
        data.append(l)

        # отображаем на экране то, что нарисовали
        pygame.display.update()

        clock.tick(FPS)

    # если вышли из основного цикла
    # закрываем pygame
    pygame.quit()

    plt.plot(data)

    maxn = 3300

    data2 = []
    n = 1

    k = 0.1
    for i in range(len(data)):
        data2.append(n)
        n = n * (1 + k * (maxn - n)/maxn)

    plt.plot(data2)

    plt.savefig("2.png")

    quit()