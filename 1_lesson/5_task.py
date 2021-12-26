# Задача 5. Вывод надписи


import pygame

size = width, height = (400, 300)
screen = pygame.display.set_mode(size)
pygame.init()


def draw():
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("Hello, Pygame!", True, (100, 255, 100))
    # параметр True- antialias- сглаживание
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (0, 255, 0),
                     (text_x - 10, text_y - 10, text_w + 20, text_h + 20), 3)


draw()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()