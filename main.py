# Подключаем игровой движок Pygame
import pygame
# Подключаем модуль для работы с файловой системой
import os

# Подготавливаем необходимые модули Pygame
pygame.init()

# Константы размера окна
WIDTH = 600
HEIGHT = 300

# Задаем размеры игрового окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Загружаем изображение в память
SPACE_IMAGE = pygame.image.load(os.path.join('./assets', 'space.jpg'))

# Создаем объект фона с разрешением окна
SPACE_BG = pygame.transform.scale(SPACE_IMAGE, (WIDTH, HEIGHT))

# Формируем объект границы
BORDER = pygame.Rect(WIDTH//2 - 2, 0, 4, HEIGHT)

# Размеры корабля
SPACESHIP_WIDTH = 55
SPACESHIP_HEIGHT = 40

# Загружаем изображение красного корабля 
RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('./assets', 'spaceship_red.png'))
# Разворачиваем изображение в нужном направлении
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

# Загружаем изображение желтого корабля 
YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('./assets', 'spaceship_yellow.png'))
# Разворачиваем изображение в нужном направлении
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

# Создаем два объекта/прямоугольника
red = pygame.Rect(100, 150, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
yellow = pygame.Rect(500, 150, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

# Запускаем бесконечный цикл программы
# Это делается чтобы программа не завершалась и постоянно рисовала новые кадры игры
while True:
    # Рисуем изображение на заднем фоне
    screen.blit(SPACE_BG, (0, 0))

    # Рисуем прямоугольник 
    pygame.draw.rect(screen, "white", BORDER)

    # Рисуем корабли
    screen.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    screen.blit(RED_SPACESHIP, (red.x, red.y))

    # Постоянно проверяем события игры и если присутствует событие Выход - останавливаем игру.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # Обновляем кадры игры
    pygame.display.update()

