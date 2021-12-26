import pygame

size = width, height = 300, 300
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
# количество кадров в секунду
fps = 60
# отрисовка круга с заданной координатой по оси абсцисс
def draf(x):
    pygame.draw.circle(screen, (255, 0, 0), (x, 200), 20)

#