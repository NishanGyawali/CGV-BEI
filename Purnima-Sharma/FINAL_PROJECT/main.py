import pygame
import random
import sys
import os

# Ensure correct working directory
os.chdir(os.path.dirname(__file__))

pygame.init()

# Window size 
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball Catch Challenge 🏀")

clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GOLD = (255, 215, 0)

# Fonts
font = pygame.font.SysFont("comicsans", 28)
big_font = pygame.font.SysFont("comicsans", 60)
small_font = pygame.font.SysFont("comicsans", 20)

# Load images
background = pygame.image.load("background.png")
basket = pygame.image.load("basket.png")
ball_img = pygame.image.load("ball.png") 

# Resize images
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
basket = pygame.transform.scale(basket, (60, 80))
ball_img = pygame.transform.scale(ball_img, (40, 40))

# Game Variables
basket_x = WIDTH // 2 - 25
basket_y = HEIGHT - 100
basket_speed = 8

ball_x = random.randint(0, WIDTH - 50)
ball_y = -50
ball_speed = 3

score = 0
game_state = "START" # States: "START", "PLAYING", "GAMEOVER"

def reset_game():
    global score, ball_y, ball_speed, ball_x, basket_x
    score = 0
    ball_y = -50
    ball_speed = 3
    ball_x = random.randint(0, WIDTH - 50)
    basket_x = WIDTH // 2 - 25

# Main Loop
while True:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if game_state == "START":
                if event.key == pygame.K_SPACE:
                    game_state = "PLAYING"
            
            elif game_state == "GAMEOVER":
                if event.key == pygame.K_r:
                    reset_game()
                    game_state = "PLAYING"
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

    if game_state == "START":
        # --- START MENU ---

        title = big_font.render("BALL CATCHER", True, GOLD)
        start_text = font.render("Press SPACE to Start", True, WHITE)
        instr = small_font.render("Use LEFT and RIGHT arrows to move", True, WHITE)
        
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 150))
        screen.blit(start_text, (WIDTH//2 - start_text.get_width()//2, 250))
        screen.blit(instr, (WIDTH//2 - instr.get_width()//2, 320))

    elif game_state == "PLAYING":
        # --- GAME LOGIC ---
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and basket_x > 2:
            basket_x -= basket_speed
        if keys[pygame.K_RIGHT] and basket_x < WIDTH - 60:
            basket_x += basket_speed

        ball_y += ball_speed

        # Collision Detection
        basket_rect = pygame.Rect(basket_x, basket_y, 60, 80)
        ball_rect = pygame.Rect(ball_x, ball_y, 40, 40)

        if basket_rect.colliderect(ball_rect):
            score += 1
            ball_y = -50
            ball_x = random.randint(0, WIDTH - 50)
            ball_speed += 0.3

        if ball_y > HEIGHT:
            game_state = "GAMEOVER"

        # Draw Game Objects
        screen.blit(basket, (basket_x, basket_y))
        screen.blit(ball_img, (ball_x, ball_y))
        
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (20, 20))

    elif game_state == "GAMEOVER":

        over_title = big_font.render("GAME OVER", True, (255, 50, 50))
        final_score = font.render(f"Final Score: {score}", True, WHITE)
        restart_instr = font.render("Press R to Restart", True, GOLD)
        quit_instr = font.render("Press Q to Quit", True, WHITE)

        screen.blit(over_title, (WIDTH//2 - over_title.get_width()//2, 120))
        screen.blit(final_score, (WIDTH//2 - final_score.get_width()//2, 200))
        screen.blit(restart_instr, (WIDTH//2 - restart_instr.get_width()//2, 280))
        screen.blit(quit_instr, (WIDTH//2 - quit_instr.get_width()//2, 330))

    pygame.display.update()
    clock.tick(60)
    