# Задача 2. Рисование точек как пикселей

import pygame
import random


size = width, height = (400, 300)
screen = pygame.display.set_mode(size)
pygame.init()


def draw():
    for i in range(10000):
        screen.fill(pygame.Color('white'),
                    (random.random() * width,
                     random.random() * height, 1, 1))


draw()
while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()
