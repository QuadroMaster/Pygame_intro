#Задача 4. Изменение яркости


import pygame

size = width, height = (400, 300)
screen = pygame.display.set_mode(size)
pygame.init()


def draw():
    screen.fill((0, 0, 0))
    color = pygame.Color(50, 150, 50)
    # рисуем "тень"
    pygame.draw.rect(screen, color,
                     (20, 20, 100, 100), 0)
    hsv = color.hsva

    # увеличиваем яркость
    color.hsva = (hsv[0], hsv[1], hsv[2] + 30, hsv[3])
    # рисуем сам объект
    pygame.draw.rect(screen, color, (10, 10, 100, 100), 0)


draw()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

