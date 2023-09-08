import pygame


class Grafic:
    def __init__(self):
        self._width = 1200
        self._height = 800
        self._surface = pygame.Surface((self._width, self._height))


    def getSurface(self):
        return self._surface

    def clear(self):
        self._surface.fill((0,0,0))

    def drawPixel(self, x, y, color):
        x += self._width // 2
        y = -(y - self._height // 2)
        self._surface.set_at((x, y), color)

    def drawLine(self, x1, y1, x2, y2, color):
        pygame.draw.line(self._surface, color, (x1 + self._width // 2, -(y1 - self._height // 2)), (x2 + self._width // 2, -(y2 - self._height // 2)))

    def drawPoly(self, vec, color):
        b = []
        for i in range(3):
            x = int(vec[i][0]) + self._width // 2
            y = -(int(vec[i][1]) - self._height // 2)
            b.append((x,y))
        pygame.draw.polygon(self._surface, color, b)

