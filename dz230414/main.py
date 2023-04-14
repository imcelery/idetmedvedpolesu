import math

import pygame
import random
import numpy as np

WIDTH = 360
HEIGHT = 480
FPS = 30
# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

r = 2

x, y = (WIDTH-r//2)//2 , (HEIGHT-r//2)//2 - 200
g = 10
dt = 0.1
vy = 0
vx = 1


def draw_lines(surface: pygame.surface.Surface, color: pygame.color.Color, xs: list[int], ys: list[int]) -> None:
    """
    Рисуем параболу с помощью pyGame
    :param surface:
    :param color:
    :param xs:
    :param ys:
    :return: None
    """
    # print(xs[:3])
    # print(ys[:3])
    x1 = xs[0]
    y1 = ys[0]
    for i in range(1, len(xs)):
        x2 = xs[i]
        y2 = ys[i]
        pygame.draw.line(surface, color, (x1, y1), (x2, y2))
        # print(x1,y1, x2, y2)
        x1, y1 = x2, y2


x_parable = np.arange(0, WIDTH+1, 1)


def f_parabble(x, xs):
    m = max((xs - WIDTH//2)**2)
    return HEIGHT - (((x - WIDTH//2)**2)/m*HEIGHT)

def pf_parabble(x, xs):
    y1 = f_parabble(x - 1, xs)
    y2 = f_parabble(x+1, xs)
    return (y2 - y1)


y_parable = f_parabble(x_parable, x_parable)

# print(x_parable)
# print(y_parable)
# Создаем игру и окно
pygame.init()
# pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # Проверяем хотят ли выйти
        if event.type == pygame.QUIT:
            running = False


    #print("x,y, v, E:", x, y, np.sqrt(vx**2 + vy**2), (vx**2 + vy**2)/2 + g*y)
    # if y > HEIGHT:
    #     y = HEIGHT
    #     vy = -vy

    # a = dv / dt -> dv = a * dt
    vy = vy + g * dt
    vx = vx
    # v = dy  / dt -> dy = v * dt
    y = int(y + vy * dt)
    x = int(x + vx * dt)

    if f_parabble(np.array([x]), x_parable)[0] < y:
        y = f_parabble(np.array([x]), x_parable)[0]
        tg_parabol = pf_parabble(x, x_parable)
        print(tg_parabol)
        #print(tg_parabol)
        # d = np.arctan(tg_parabol)
        # print(d)
        # g = np.sqrt(vy**2 + vx ** 2)
        # vy = g * -np.cos(d)
        # vx = g * np.sin(d)



        modul_v = np.sqrt(vx**2 + vy**2)
        #print("modul_v", modul_v)
        tg_v = np.array([vx])/np.array([vy])
        print(tg_v)
        #print("tg_v", tg_v)
        #print("угол наклона параболы", np.arctan(tg_parabol))
        # print("угола наклона весктора скорости", np.arctan(tg_v))
        # print("разность углов", np.arctan(tg_parabol) - np.arctan(tg_v))
        alpha_minus_beta =np.pi - 2 * np.arctan(tg_parabol) - np.arctan(tg_v)
        new_tan = np.tan(alpha_minus_beta)[0]
        print(math.degrees(alpha_minus_beta))

        vy = modul_v * np.cos(alpha_minus_beta[0])
        vx = modul_v * np.sin(alpha_minus_beta[0])

        # # print("--------")
        # # print(vx, vy)
        # if np.abs(new_tan) < 1:
        #     vy = np.round(modul_v * new_tan)
        #     #print("vy", vy)
        #     vx = np.round((np.sign(alpha_minus_beta) * np.sqrt(modul_v**2 - vy**2))[0])
        #     #print(vx, vy)
        # else:
        #     vx = np.round(modul_v/new_tan)
        #     #print("vx", vx)
        #     vy = np.round((np.sign(alpha_minus_beta) * np.sqrt(modul_v**2 - vx**2))[0])
        #     #print(vx, vy)
        # break

    screen.fill(BLACK)
    pygame.draw.circle(screen, RED, [x, y], r)
    draw_lines(screen, GREEN, x_parable, y_parable)
    pygame.display.flip()

pygame.quit()


if __name__ == "__main__":
    pass