# Подключаем игровой движок Pygame
import pygame
# Подключаем модуль для работы с файловой системой
import os

# Подготавливаем необходимые модули Pygame
pygame.init()

### Константы ###
# Константы размера окна
WIDTH = 600
HEIGHT = 300
# Размеры корабля
SPACESHIP_WIDTH = 55
SPACESHIP_HEIGHT = 40
# Скорость корабля
VELOCITY = 5
# Количество кадров в секунду
FPS = 60

# Ограничитель кадров
clock = pygame.time.Clock()

# Задаем размеры игрового окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Загружаем изображение в память
SPACE_IMAGE = pygame.image.load(os.path.join('./assets', 'space.jpg'))

# Создаем объект фона с разрешением окна
SPACE_BG = pygame.transform.scale(SPACE_IMAGE, (WIDTH, HEIGHT))

# Формируем объект границы
BORDER = pygame.Rect(WIDTH//2 - 2, 0, 4, HEIGHT)

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

# Функция движения красного корабля
def red_handle_movement(keys_pressed, red):
    # Движение ВЛЕВО
    if keys_pressed[pygame.K_a] and red.x - VELOCITY > 0:
        red.x -= VELOCITY
    # Движение ВПРАВО (запрещаем пересекать границу игроков)
    if keys_pressed[pygame.K_d] and red.x + VELOCITY + red.width < BORDER.x:
        red.x += VELOCITY
    # Движение ВВЕРХ (запрещаем подниматься выше 0 по координате y)
    if keys_pressed[pygame.K_w] and red.y - VELOCITY > 0:
        red.y -= VELOCITY
    # Движение ВНИЗ (запрещаем опускаться ниже чем высота экрана за вычетом высоты корабля и дополнительных 15 для отступа)
    if keys_pressed[pygame.K_s] and red.y + VELOCITY + red.height < HEIGHT - 15:
        red.y += VELOCITY

# Функция движения желтого корабля
def yellow_handle_movement(keys_pressed, yellow):
    # Движение ВЛЕВО (запрещаем пересекать границу игроков)
    if keys_pressed[pygame.K_LEFT] and yellow.x - VELOCITY > BORDER.x + BORDER.width:
        yellow.x -= VELOCITY
    # Движение ВПРАВО
    if keys_pressed[pygame.K_RIGHT] and yellow.x + VELOCITY + yellow.width < WIDTH:
        yellow.x += VELOCITY
    # Движение ВВЕРХ
    if keys_pressed[pygame.K_UP] and yellow.y - VELOCITY > 0:
        yellow.y -= VELOCITY
    # Движение ВНИЗ
    if keys_pressed[pygame.K_DOWN] and yellow.y + VELOCITY + yellow.height < HEIGHT - 15:
        yellow.y += VELOCITY


# Запускаем бесконечный цикл программы
# Это делается чтобы программа не завершалась и постоянно рисовала новые кадры игры
while True:
    # Ограничиваем количество кадров игры
    clock.tick(FPS)

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

    # Узнаем нажатие клавишей
    keys_pressed = pygame.key.get_pressed()
    # Выполняем установку координат кораблей
    red_handle_movement(keys_pressed, red)
    yellow_handle_movement(keys_pressed, yellow)

    # Обновляем кадры игры
    pygame.display.update()

