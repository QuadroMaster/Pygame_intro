# Старый телевизор (расширение задачи 2 первого урока)
import pygame
import random

size = width, height = 300, 300
screen = pygame.display.set_mode(size)

# отрисовка 10000 точек, расположенных в случайных местах
def draw():
    screen.fill((0, 0, 0))
    for i in range(10000):
        screen.fill(pygame.Color('white'), (random.random() * width,
                                            random.random() * height, 1, 1))

# главный игровой цикл
running = True
while running:
    # внутри игрового цикла ещё один цикл приёма и обработки различных событий
    events = pygame.event.get()
    for event in events:
        # обработка закрытия окна
        if event.type == pygame.QUIT:
            running = False

    # каждый раз с каждым циклом рисуются 10000 точек в поизвольных местах
    draw()

    # обновление экрана
    pygame.display.flip()
#print(random.random())
pygame.quit()