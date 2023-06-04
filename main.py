# Подключаем игровой движок Pygame
import pygame
# Подключаем модуль для работы с файловой системой
import os

# Подготавливаем необходимые модули Pygame
pygame.init()
pygame.mixer.init()

# Подключаем звуки к игре
# Звук попадания
BULLET_HIT_SOUND = pygame.mixer.Sound('./assets/grenade.mp3')
# Звук выстрела
BULLET_FIRE_SOUND = pygame.mixer.Sound('./assets/silencer.mp3')

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
# Шрифт здоровья
HEALTH_FONT = pygame.font.SysFont('comicsans', 20)
# Пользовательские события попаданий
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

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

# Здоровье игроков
red_health = 10
yellow_health = 10

# Хранение выпущенных пуль
red_bullets = []
yellow_bullets = []
# Макс. выпущенных пуль
MAX_BULLETS = 3
# Скорость пули
BULLET_VEL = 7

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

# Обработка выпущенных пуль
def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    # Перебираем все пули красного
    for bullet in red_bullets:
        # Двигаем пулю вправо
        bullet.x += BULLET_VEL
        # Если пуля задевает желтого игрока
        if yellow.colliderect(bullet):
            # Вызываем пользовательское событие попадание в Желтого
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            # Удаляем текущую пулю
            red_bullets.remove(bullet)
        # Удаляем пулю если она вышла за экран
        elif bullet.x > WIDTH:
            red_bullets.remove(bullet)

    # Перебираем все пули желтого
    for bullet in yellow_bullets:
        # Двигаем пулю влево
        bullet.x -= BULLET_VEL
        # Если пуля задевает красного игрока
        if red.colliderect(bullet):
            # Вызываем пользовательское событие попадание в Красного
            pygame.event.post(pygame.event.Event(RED_HIT))
            # Удаляем текущую пулю
            yellow_bullets.remove(bullet)
        # Удаляем пулю если она вышла за экран
        elif bullet.x < 0:
            yellow_bullets.remove(bullet)

# Функция рисует экран победителя
def draw_winner(text):
    # Создаем шрифт для победителя
    WINNER_FONT = pygame.font.SysFont('comicsans', 60)
    # Создаем надпись
    draw_text = WINNER_FONT.render(text, 1, 'white')
    # Устанавливаем надпись в центре игрового поля
    screen.blit(draw_text, (WIDTH/2 - draw_text.get_width() /
                         2, HEIGHT/2 - draw_text.get_height()/2))
    
    # Обновляем кадр игры
    pygame.display.update()
    # Задержка после победы
    pygame.time.delay(2000)

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

    # Отображаем здоровье на экране
    red_health_text = HEALTH_FONT.render(
        "Health: " + str(red_health), 1, "white")
    yellow_health_text = HEALTH_FONT.render(
        "Health: " + str(yellow_health), 1, "white")
    screen.blit(red_health_text, (10, 10))
    screen.blit(yellow_health_text, (WIDTH - red_health_text.get_width() - 10, 10))

    # Постоянно проверяем события игры и если присутствует событие Выход - останавливаем игру.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        # Если случилось пользовательское событие RED_HIT отнимаем жизни у Красного
        if event.type == RED_HIT:
            red_health -= 1
            # Звук попадания
            BULLET_HIT_SOUND.play()

        # Если случилось пользовательское событие YELLOW_HIT отнимаем жизни у Желтого
        if event.type == YELLOW_HIT:
            yellow_health -= 1
            # Звук попадания
            BULLET_HIT_SOUND.play()

        # Если произошло событие нажатия клавиши
        if event.type == pygame.KEYDOWN:
            # И нажали клавишу Пробел, а так же если длина листа выпущенных пуль красного меньше минимального
            if event.key == pygame.K_SPACE and len(red_bullets) < MAX_BULLETS:
                # Создаем объект прямоугольника для Пули
                bullet = pygame.Rect(
                    red.x + red.width, red.y + red.height//2 - 2, 10, 5)
                # Добавляем выпущенную пулю красному
                red_bullets.append(bullet)
                # Звук выстрела
                BULLET_FIRE_SOUND.play()

            # Если нажали клавишу Enter, создаем выпущенную пулю желтому игроку
            if event.key == pygame.K_RETURN and len(yellow_bullets) < MAX_BULLETS:
                # Создаем объект прямоугольника для Пули
                bullet = pygame.Rect(
                    yellow.x, yellow.y + yellow.height//2 - 2, 10, 5)
                # Добавляем выпущенную пулю желтому
                yellow_bullets.append(bullet)
                # Звук выстрела
                BULLET_FIRE_SOUND.play()

    # Узнаем нажатие клавишей
    keys_pressed = pygame.key.get_pressed()
    # Выполняем установку координат кораблей
    red_handle_movement(keys_pressed, red)
    yellow_handle_movement(keys_pressed, yellow)

    # Проверяем столкновения пуль
    handle_bullets(yellow_bullets, red_bullets, yellow, red)

    # Перебираем пули красного и рисуем каждый кадр
    for bullet in red_bullets:
        pygame.draw.rect(screen, "red", bullet)
    # Перебираем пули желтого и рисуем каждый кадр
    for bullet in yellow_bullets:
        pygame.draw.rect(screen, "yellow", bullet)

    # Если здоровье упало до нуля, рисуем имя победителя.
    winner_text = ""
    if red_health <= 0:
        winner_text = "Yellow Wins!"

    if yellow_health <= 0:
        winner_text = "Red Wins!"

    if winner_text != "":
        draw_winner(winner_text)
        # Обнуляем пули
        red_bullets.clear()
        yellow_bullets.clear()
        # Восстанавливаем здоровье
        red_health = 10
        yellow_health = 10

    # Обновляем кадры игры
    pygame.display.update()

