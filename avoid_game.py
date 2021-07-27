import pygame
import random

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Avoid Game")

clock = pygame.time.Clock()

background = pygame.image.load("D:\\devwood\\pythonproject\\python_project\\background.png")

character = pygame.image.load("D:\\devwood\\pythonproject\\python_project\\character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

to_x = 0
to_y = 0

character_speed = 0.5
enemy1_speed = 0.6
enemy2_speed = 0.7

enemy1 = pygame.image.load("D:\\devwood\\pythonproject\\python_project\\enemy.png")
enemy1_size = enemy1.get_rect().size
enemy1_width = enemy1_size[0]
enemy1_height = enemy1_size[1]
enemy1_x_pos = 0
enemy1_y_pos = 0

enemy2 = pygame.image.load("D:\\devwood\\pythonproject\\python_project\\enemy.png")
enemy2_size = enemy2.get_rect().size
enemy2_width = enemy2_size[0]
enemy2_height = enemy2_size[1]
enemy2_x_pos = screen_width - enemy2_width
enemy2_y_pos = 0

game_font = pygame.font.Font(None, 40)

start_ticks = pygame.time.get_ticks()


running = True
while running:
    dt = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    character_x_pos += to_x * dt
    enemy1_y_pos += enemy1_speed * dt
    enemy2_y_pos += enemy2_speed * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if enemy1_y_pos > screen_height:
        enemy1_y_pos = 0
        enemy1_x_pos = random.randint(0, screen_width - enemy1_width)
    if enemy2_y_pos > screen_height:
        enemy2_y_pos = 0
        enemy2_x_pos = random.randint(0, screen_width - enemy2_width)

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy1_rect = enemy1.get_rect()
    enemy1_rect.left = enemy1_x_pos
    enemy1_rect.top = enemy1_y_pos

    enemy2_rect = enemy2.get_rect()
    enemy2_rect.left = enemy2_x_pos
    enemy2_rect.top = enemy2_y_pos

    if character_rect.colliderect(enemy1_rect):
        running = False
    if character_rect.colliderect(enemy2_rect):
        running = False

    screen.blit(background, (0, 0)) # =screen.fill((0, 0, 255))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy1, (enemy1_x_pos, enemy1_y_pos))
    screen.blit(enemy2, (enemy2_x_pos, enemy2_y_pos))

    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render(str(int(elapsed_time)), True, (255, 255, 255))
    screen.blit(timer, (10, 10))

    pygame.display.update()

pygame.time.delay(2000)

pygame.quit()
