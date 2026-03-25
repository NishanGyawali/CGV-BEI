import pygame
import sys

pygame.init()

# Screen settings
WIDTH = 600
HEIGHT = 600
CELL = 40

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Maze Escape Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)

# Maze layout (1 = wall, 0 = path)
maze = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,1,0,0,0,0,0,1,0,0,0,1],
    [1,0,1,0,1,0,1,1,1,0,1,0,1,0,1],
    [1,0,1,0,0,0,1,0,0,0,0,0,1,0,1],
    [1,0,1,1,1,0,1,0,1,1,1,0,1,0,1],
    [1,0,0,0,1,0,0,0,1,0,0,0,1,0,1],
    [1,1,1,0,1,1,1,0,1,0,1,1,1,0,1],
    [1,0,0,0,0,0,1,0,0,0,1,0,0,0,1],
    [1,0,1,1,1,0,1,1,1,0,1,0,1,1,1],
    [1,0,0,0,1,0,0,0,1,0,0,0,0,0,1],
    [1,1,1,0,1,1,1,0,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,1,0,1],
    [1,0,1,1,1,1,1,1,1,1,1,0,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

# Player start position
player_x = 1
player_y = 1

# Exit position
exit_x = 13
exit_y = 13

clock = pygame.time.Clock()

running = True
while running:
    clock.tick(10)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            new_x = player_x
            new_y = player_y

            if event.key == pygame.K_LEFT:
                new_x -= 1
            if event.key == pygame.K_RIGHT:
                new_x += 1
            if event.key == pygame.K_UP:
                new_y -= 1
            if event.key == pygame.K_DOWN:
                new_y += 1

            # Check wall collision
            if maze[new_y][new_x] == 0:
                player_x = new_x
                player_y = new_y

    # Draw maze
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == 1:
                pygame.draw.rect(screen, BLACK, (col*CELL, row*CELL, CELL, CELL))

    # Draw exit
    pygame.draw.rect(screen, GREEN, (exit_x*CELL, exit_y*CELL, CELL, CELL))

    # Draw player
    pygame.draw.rect(screen, BLUE, (player_x*CELL, player_y*CELL, CELL, CELL))

    # Check win condition
    if player_x == exit_x and player_y == exit_y:
        font = pygame.font.SysFont(None, 50)
        text = font.render("You Escaped!", True, RED)
        screen.blit(text, (180, 270))
        
        pygame.display.update()
        pygame.time.delay(3000)
        running = False

    pygame.display.update()

pygame.quit()
sys.exit()
