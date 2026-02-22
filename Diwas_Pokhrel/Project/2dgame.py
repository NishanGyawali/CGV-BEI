import pygame
import random
import sys
pygame.init()
WIDTH, HEIGHT = 700, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Dodge Game")
clock = pygame.time.Clock()
background = pygame.Surface((WIDTH, HEIGHT))
background.fill((0, 0, 0))  # Black background
player_img = pygame.image.load("newton.jpeg")
player_img = pygame.transform.scale(player_img, (40, 40))
enemy_img = pygame.image.load("apple.jpeg")
enemy_img = pygame.transform.scale(enemy_img, (40, 40))
font = pygame.font.SysFont(None, 30)
big_font = pygame.font.SysFont(None, 55)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
WHITE = (255, 255, 255)
def reset_game():
    player = player_img.get_rect()
    player.centerx = WIDTH // 2
    player.bottom = HEIGHT - 10
    enemies = []
    for _ in range(3):
        enemy = enemy_img.get_rect()
        enemy.x = random.randint(0, WIDTH - 40)
        enemy.y = random.randint(-300, 0)
        enemies.append(enemy)
    score = 0
    lives = 3
    enemy_speed = 7
    next_level = 50
    level_up = False
    level_time = 0
    return player, enemies, score, lives, enemy_speed, next_level, level_up, level_time
def start_screen():
    while True:
        screen.blit(background, (0, 0))
        title = big_font.render("2D DODGE GAME", True, RED)
        msg = font.render("Press SPACE to Start but please don't let gravity win!", True, WHITE)
        screen.blit(title, (140, 150))
        screen.blit(msg, (150, 220))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
def game_over_screen(score):
    while True:
        screen.blit(background, (0, 0))
        over_text = big_font.render("OH NO! Gravity Discovered", True, RED)
        score_text = font.render(f"Final Score: {score}", True, GREEN)
        restart_text = font.render("Press R to Restart", True, WHITE)
        quit_text = font.render("Press Q to Quit", True, WHITE)
        screen.blit(over_text, (170, 120))
        screen.blit(score_text, (220, 180))
        screen.blit(restart_text, (200, 220))
        screen.blit(quit_text, (220, 250))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
start_screen()
player, enemies, score, lives, enemy_speed, next_level, level_up, level_time = reset_game()
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(background, (0, 0))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= 6
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += 6
    for enemy in enemies:
        enemy.y += enemy_speed
        if enemy.top > HEIGHT:
            enemy.y = random.randint(-200, 0)
            enemy.x = random.randint(0, WIDTH - 40)
            score += 1
            if score >= next_level:
                enemy_speed += 3
                next_level += 50
                level_up = True
                level_time = pygame.time.get_ticks()
        if player.colliderect(enemy):
            lives -= 1
            enemy.y = random.randint(-200, 0)
            enemy.x = random.randint(0, WIDTH - 40)
            if lives <= 0:
                restart = game_over_screen(score)
                if restart:
                    player, enemies, score, lives, enemy_speed, next_level, level_up, level_time = reset_game()
    screen.blit(player_img, player)
    for enemy in enemies:
        screen.blit(enemy_img, enemy)
    score_text = font.render(f"Score: {score}", True, GREEN)
    lives_text = font.render(f"Lives: {lives}", True, RED)
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 40))
    if level_up:
        if pygame.time.get_ticks() - level_time < 2000:
            level_text = big_font.render("LEVEL UP!", True, WHITE)
            screen.blit(level_text, (190, 170))
        else:
            level_up = False
    pygame.display.update()
