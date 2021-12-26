# Задача 3. Линия, прямоугольник и многоугольник

import pygame

size = width, height = (400, 500)
screen = pygame.display.set_mode(size)
pygame.init()


def draw():
    screen.fill((255, 255, 255))

    # Создание линии
    pygame.draw.line(screen, pygame.Color(255, 0, 0), (20, 20), (200, 30), 4)
    # pygame.draw.line(screen, pygame.Color(цвет), (координата начала линии), (координата конца линии (по диагонали)), толщина линии)
    #Можно задать цвет и короче:
    #pygame.draw.line(screen, (255, 0, 0), (20, 20), (60, 20), 2)

    # Создание прямоугольника
    pygame.draw.rect(screen, pygame.Color('black'), (100, 100, 60, 60), 4)
    #если width не задан, то нарисуется полностью залитый указанным цветом прямоугольник,
    # иначе нарисуется только рамка заданной толщины (у меня это 4)

    # Создание многоугольника
    pygame.draw.polygon(screen, pygame.Color('orange'), ((100, 200), (180, 300), (120, 330)), 4)

draw()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()
