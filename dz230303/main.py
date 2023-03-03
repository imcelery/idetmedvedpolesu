import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 60
# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

player_height = 10
player_width = 50
player_pos = WIDTH // 2

move_r = False
move_l = False
speed = 5

ball_pos = [200, 100]

bal_r = 5

ball_speed = [2, 2]

line_k = 4
blocks_k = 10

block_heigt = 15
block_width = 30

block_dist_x = 5

block_dist_y = 2


class Block:
    def __init__(self, rect, color):
        self.color = color
        self.rect = rect

def gen_blocks():
    a = []
    for i in range(line_k):
        for j in range(blocks_k):
            a.append(Block( pygame.Rect(((block_dist_y + block_width) * j, (block_heigt + block_dist_y) * i, block_width, block_heigt)), WHITE))
    return a
if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("My Game")
    clock = pygame.time.Clock()

    blocks = gen_blocks()
    # Цикл игры
    running = True
    while running:
        # Держим цикл на правильной скорости
        clock.tick(FPS)
        # Ввод процесса (события)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    move_r = True
                    move_l = False

                elif event.key == pygame.K_a:
                    move_l = True
                    move_r = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    move_r = False


                elif event.key == pygame.K_a:
                    move_l = False



        if move_r:
            player_pos += speed

        if move_l:
            player_pos -= speed

        nx = ball_pos[0] + ball_speed[0]


        if nx <= 0:

            ball_pos[0] = -(ball_speed[0] + ball_pos[0])
            ball_speed[0] = -ball_speed[0]

        elif nx >= WIDTH:
            ball_pos[0] =  2 * WIDTH - (ball_speed[0] + ball_pos[0])
            ball_speed[0] = -ball_speed[0]
        else:
            ball_pos[0] = nx

        ny = ball_pos[1] + ball_speed[1]

        if ny <= 0:
            ball_pos[1] = -(ball_speed[1] + ball_pos[1])
            ball_speed[1] = -ball_speed[1]

        elif ny >= HEIGHT - player_height:
            if ball_pos[0] >= player_pos - player_width//2 and ball_pos[0] <= player_pos + player_width//2:
                ball_pos[1] = 2 * (HEIGHT - player_height) - (ball_speed[1] + ball_pos[1])
                ball_speed[1] = -ball_speed[1]
                # d = ball_pos[0] - player_pos
                # ball_speed[0] *= d

        elif ny >= HEIGHT:
            pygame.quit()

        else:
            ball_pos[1] = ny



        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, (player_pos - player_width//2, HEIGHT - player_height, player_width, player_height))
        ballrect = pygame.draw.circle(screen, WHITE, ball_pos, bal_r)

        newblocks = []
        for i in blocks:
            if not i.rect.colliderect(ballrect):
                newblocks.append(i)
        blocks = newblocks

        for i in blocks:
            pygame.draw.rect(screen, WHITE, i.rect)
        pygame.display.update()