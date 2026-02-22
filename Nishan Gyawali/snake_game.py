import pygame
import random
import sys

WIDTH, HEIGHT = 800, 600
CELL = 20
FPS = 12

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
DARK_GREEN = (0, 140, 0)
RED = (220, 0, 0)

def random_food_position(snake):
    while True:
        x = random.randrange(0, WIDTH, CELL)
        y = random.randrange(0, HEIGHT, CELL)
        if (x, y) not in snake:
            return (x, y)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("arial", 30)

    snake = [(400, 300), (380, 300), (360, 300)]
    direction = (CELL, 0)
    pending = direction
    food = random_food_position(snake)
    score = 0
    game_over = False

    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, CELL):
                    pending = (0, -CELL)
                elif event.key == pygame.K_DOWN and direction != (0, -CELL):
                    pending = (0, CELL)
                elif event.key == pygame.K_LEFT and direction != (CELL, 0):
                    pending = (-CELL, 0)
                elif event.key == pygame.K_RIGHT and direction != (-CELL, 0):
                    pending = (CELL, 0)

        if not game_over:
            direction = pending
            head_x, head_y = snake[0]
            new_head = (head_x + direction[0], head_y + direction[1])

            if new_head in snake or new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
                game_over = True
            else:
                snake.insert(0, new_head)
                if new_head == food:
                    score += 1
                    food = random_food_position(snake)
                else:
                    snake.pop()

        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, (*food, CELL, CELL))

        for i, (x, y) in enumerate(snake):
            color = GREEN if i == 0 else DARK_GREEN
            pygame.draw.rect(screen, color, (x, y, CELL, CELL))

        text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(text, (10, 10))

        if game_over:
            over = font.render("GAME OVER", True, WHITE)
            screen.blit(over, (WIDTH//2 - 100, HEIGHT//2))

        pygame.display.update()

if __name__ == "__main__":
    main()
