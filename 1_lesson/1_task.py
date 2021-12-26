# Занятие 1. Элементарное рисование
# Задача 1. Красный прямоугольник на белом фоне

import pygame

size = width, height = (400, 300)
screen = pygame.display.set_mode(size)
pygame.init()

def draw():
    screen.fill((205, 205, 205))
    screen.fill(pygame.Color('red'), pygame.Rect(50, 50, 60, 120))
    #краткая запись: screen.fill(pygame.Color('red'), (10, 10, 60, 60))

draw()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()

