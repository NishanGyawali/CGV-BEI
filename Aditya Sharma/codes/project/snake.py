import pygame
import random
import os
import sys

pygame.init()
pygame.mixer.init()

# Display settings
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game 🐍")

clock = pygame.time.Clock()
FPS = 10

current_dir = os.path.dirname(__file__)

# Load images
bg = pygame.image.load(os.path.join(current_dir, "bg.png"))
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

apple_img = pygame.image.load(os.path.join(current_dir, "apple.png"))
apple_img = pygame.transform.scale(apple_img, (GRID_SIZE, GRID_SIZE))

snake_img = pygame.image.load(os.path.join(current_dir, "snake.png"))
snake_img = pygame.transform.scale(snake_img, (GRID_SIZE, GRID_SIZE))

# Load sounds
crash_sound = pygame.mixer.Sound(os.path.join(current_dir, "crash.mp3"))
eat_sound = pygame.mixer.Sound(os.path.join(current_dir, "eat.mp3"))

font = pygame.font.SysFont("Arial", 30)

snake_pos = [[100, 100]]
snake_dir = "RIGHT"

dir_map = {
    "UP": (0, -GRID_SIZE),
    "DOWN": (0, GRID_SIZE),
    "LEFT": (-GRID_SIZE, 0),
    "RIGHT": (GRID_SIZE, 0)
}

def generate_apple():
    while True:
        pos = [random.randrange(0, WIDTH // GRID_SIZE) * GRID_SIZE,
               random.randrange(0, HEIGHT // GRID_SIZE) * GRID_SIZE]
        if pos not in snake_pos:
            return pos

apple_pos = generate_apple()
score = 0
running = True
game_over = False

while running:

    if not game_over:

        screen.blit(bg, (0, 0))
        screen.blit(apple_img, tuple(apple_pos))

        for pos in snake_pos:
            screen.blit(snake_img, tuple(pos))

        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        pygame.display.update()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_dir != "DOWN":
                    snake_dir = "UP"
                elif event.key == pygame.K_DOWN and snake_dir != "UP":
                    snake_dir = "DOWN"
                elif event.key == pygame.K_LEFT and snake_dir != "RIGHT":
                    snake_dir = "LEFT"
                elif event.key == pygame.K_RIGHT and snake_dir != "LEFT":
                    snake_dir = "RIGHT"

        new_head = [
            snake_pos[0][0] + dir_map[snake_dir][0],
            snake_pos[0][1] + dir_map[snake_dir][1]
        ]

        # Wall collision
        if (new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT):
            crash_sound.play()
            game_over = True

        # Self collision
        if new_head in snake_pos:
            crash_sound.play()
            game_over = True

        snake_pos.insert(0, new_head)

        # Apple collision
        if new_head == apple_pos:
            score += 1
            eat_sound.play()  # 🔔 Play eating sound
            apple_pos = generate_apple()
        else:
            snake_pos.pop()

    else:
        screen.fill((0, 0, 0))

        over_text = font.render(f"Game Over! Score: {score}", True, (255, 255, 255))
        restart_text = font.render("Press R to Restart or Q to Quit", True, (255, 255, 255))

        screen.blit(over_text, (WIDTH // 4, HEIGHT // 2 - 30))
        screen.blit(restart_text, (WIDTH // 6, HEIGHT // 2 + 10))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    snake_pos = [[100, 100]]
                    snake_dir = "RIGHT"
                    apple_pos = generate_apple()
                    score = 0
                    game_over = False

                elif event.key == pygame.K_q:
                    running = False

pygame.quit()
sys.exit()
