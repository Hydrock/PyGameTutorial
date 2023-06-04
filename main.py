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

# Запускаем бесконечный цикл программы
# Это делается чтобы программа не завершалась и постоянно рисовала новые кадры игры
while True:
    # Рисуем изображение на заднем фоне
    screen.blit(SPACE_BG, (0, 0))

    # Постоянно проверяем события игры и если присутствует событие Выход - останавливаем игру.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # Обновляем кадры игры
    pygame.display.update()

