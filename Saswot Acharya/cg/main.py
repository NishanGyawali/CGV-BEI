import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Ping Pong Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Paddle properties
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
paddle_speed = 7

# Ball properties
BALL_SIZE = 20

# Font
font = pygame.font.SysFont("comicsans", 40)

# Clock
clock = pygame.time.Clock()

# Load background image for start menu
start_bg = pygame.image.load("start_background.jpg")  # Put your image in the same folder
start_bg = pygame.transform.scale(start_bg, (WIDTH, HEIGHT))  # Scale to fit screen

def draw_game(player_y, opponent_y, ball_x, ball_y, player_score, opponent_score):
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (0, player_y, PADDLE_WIDTH, PADDLE_HEIGHT))  # Player paddle
    pygame.draw.rect(screen, WHITE, (WIDTH - PADDLE_WIDTH, opponent_y, PADDLE_WIDTH, PADDLE_HEIGHT))  # Opponent paddle
    pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))  # Ball
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))  # Center line

    # Display scores
    player_text = font.render(str(player_score), True, WHITE)
    opponent_text = font.render(str(opponent_score), True, WHITE)
    screen.blit(player_text, (WIDTH // 4, 20))
    screen.blit(opponent_text, (WIDTH * 3 // 4, 20))

    pygame.display.flip()

def start_menu():
    while True:
        screen.blit(start_bg, (0, 0))  # Draw background image
        title = font.render("PING PONG GAME", True, GREEN)
        prompt = font.render("Press ENTER to Start", True, BLACK)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, HEIGHT//3))
        screen.blit(prompt, (WIDTH//2 - prompt.get_width()//2, HEIGHT//2))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return

def end_menu(winner):
    while True:
        screen.fill(BLACK)
        message = font.render(f"{winner} Wins!", True, RED)
        prompt = font.render("Press R to Restart or Q to Quit", True, WHITE)
        screen.blit(message, (WIDTH//2 - message.get_width()//2, HEIGHT//3))
        screen.blit(prompt, (WIDTH//2 - prompt.get_width()//2, HEIGHT//2))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main_game()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

def main_game():
    # Initial positions
    player_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
    opponent_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
    ball_x, ball_y = WIDTH // 2, HEIGHT // 2
    ball_speed_x = random.choice([-5, 5])
    ball_speed_y = random.choice([-5, 5])

    player_score = 0
    opponent_score = 0

    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and player_y > 0:
            player_y -= paddle_speed
        if keys[pygame.K_s] and player_y < HEIGHT - PADDLE_HEIGHT:
            player_y += paddle_speed

        # Opponent AI
        if opponent_y + PADDLE_HEIGHT / 2 < ball_y:
            opponent_y += paddle_speed
        if opponent_y + PADDLE_HEIGHT / 2 > ball_y:
            opponent_y -= paddle_speed
        opponent_y = max(min(opponent_y, HEIGHT - PADDLE_HEIGHT), 0)

        # Ball movement
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        # Ball collision with walls
        if ball_y <= 0 or ball_y >= HEIGHT - BALL_SIZE:
            ball_speed_y *= -1

        # Ball collision with paddles
        if (ball_x <= PADDLE_WIDTH and player_y < ball_y < player_y + PADDLE_HEIGHT) or \
           (ball_x >= WIDTH - PADDLE_WIDTH - BALL_SIZE and opponent_y < ball_y < opponent_y + PADDLE_HEIGHT):
            ball_speed_x *= -1

        # Scoring
        if ball_x < 0:
            opponent_score += 1
            ball_x, ball_y = WIDTH // 2, HEIGHT // 2
            ball_speed_x = random.choice([-5, 5])
            ball_speed_y = random.choice([-5, 5])
        elif ball_x > WIDTH:
            player_score += 1
            ball_x, ball_y = WIDTH // 2, HEIGHT // 2
            ball_speed_x = random.choice([-5, 5])
            ball_speed_y = random.choice([-5, 5])

        # Check for winner (first to 5 points)
        if player_score >= 5:
            end_menu("Player")
        elif opponent_score >= 5:
            end_menu("Opponent")

        # Draw everything
        draw_game(player_y, opponent_y, ball_x, ball_y, player_score, opponent_score)
        clock.tick(60)

# Run the game
start_menu()
main_game()