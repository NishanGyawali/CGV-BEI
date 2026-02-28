# Full game using Pygame

import pygame
import os
import sys

# ==========================
# 1. Setup & Constants
# ==========================
pygame.init()
pygame.mixer.init()

TILE = 60
FPS = 60
PLAYER_SPEED = 5

# Colors (Fallbacks if images are missing)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
FLOOR_COLOR = (200, 200, 200)

# ==========================
# 2. Map Matrix (Task 1: New Level)
# 1=Wall, 0=Floor, 2=Goal
# ==========================
map_data = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

ROWS = len(map_data)
COLS = len(map_data[0])
screen = pygame.display.set_mode((COLS * TILE, ROWS * TILE))
pygame.display.set_caption("Lab 10: Final Game")
clock = pygame.time.Clock()

# ==========================
# 3. Asset Loading (Task 2 & 5)
# ==========================
# Look for assets in ../assets/ relative to this script
base_path = os.path.dirname(__file__)
assets_path = os.path.join(base_path, "..", "assets")

def load_asset(name, type="img"):
    full_path = os.path.join(assets_path, name)
    if not os.path.exists(full_path):
        print(f"Warning: Asset {name} not found at {full_path}")
        return None
    if type == "img":
        img = pygame.image.load(full_path).convert_alpha()
        return pygame.transform.scale(img, (TILE, TILE))
    else:
        return pygame.mixer.Sound(full_path)

# Load Sprites
player_img = load_asset("player.png")
wall_img   = load_asset("wall.png")
floor_img  = load_asset("floor.png")
goal_img   = load_asset("goal.png")

# Load Sounds
move_sound = load_asset("move.wav", "sound")
win_sound  = load_asset("win.wav", "sound")

# ==========================
# 4. Game Logic Functions
# ==========================
player_x, player_y = TILE, TILE
score = 0
game_won = False
font = pygame.font.SysFont("Arial", 36, bold=True)

def can_move(nx, ny):
    """Checks if the next position hits a wall."""
    # Check all four corners of the player sprite (to prevent bleeding into walls)
    corners = [(nx+5, ny+5), (nx+TILE-5, ny+5), (nx+5, ny+TILE-5), (nx+TILE-5, ny+TILE-5)]
    for cx, cy in corners:
        row, col = cy // TILE, cx // TILE
        if map_data[int(row)][int(col)] == 1:
            return False
    return True

# ==========================
# 5. Main Game Loop
# ==========================
running = True
while running:
    # A. Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # B. Movement (Task 5: Sound)
    if not game_won:
        keys = pygame.key.get_pressed()
        old_x, old_y = player_x, player_y
        
        dx, dy = 0, 0
        if keys[pygame.K_LEFT]:  dx = -PLAYER_SPEED
        if keys[pygame.K_RIGHT]: dx = PLAYER_SPEED
        if keys[pygame.K_UP]:    dy = -PLAYER_SPEED
        if keys[pygame.K_DOWN]:  dy = PLAYER_SPEED

        if dx != 0 or dy != 0:
            if can_move(player_x + dx, player_y + dy):
                player_x += dx
                player_y += dy
                # Play sound occasionally during movement (not every frame)
                if not pygame.mixer.get_busy() and move_sound:
                    move_sound.play()

    # C. Check Win Condition (Task 3 & 4)
    grid_r, grid_c = (player_y + TILE//2) // TILE, (player_x + TILE//2) // TILE
    if map_data[int(grid_r)][int(grid_c)] == 2 and not game_won:
        game_won = True
        score += 10
        if win_sound: win_sound.play()

    # D. Drawing
    screen.fill(BLACK)
    
    for r in range(ROWS):
        for c in range(COLS):
            pos = (c * TILE, r * TILE)
            # Draw floors/walls/goals
            if map_data[r][c] == 1:
                if wall_img: screen.blit(wall_img, pos)
                else: pygame.draw.rect(screen, BLACK, (*pos, TILE, TILE))
            elif map_data[r][c] == 2:
                if goal_img: screen.blit(goal_img, pos)
                else: pygame.draw.rect(screen, GREEN, (*pos, TILE, TILE))
            else:
                if floor_img: screen.blit(floor_img, pos)
                else: pygame.draw.rect(screen, FLOOR_COLOR, (*pos, TILE, TILE))

    # Draw Player
    if player_img:
        screen.blit(player_img, (player_x, player_y))
    else:
        pygame.draw.rect(screen, BLUE, (player_x, player_y, TILE-10, TILE-10))

    # Draw UI (Score & Win)
    score_txt = font.render(f"Score: {score}", True, RED)
    screen.blit(score_txt, (10, 10))

    if game_won:
        win_msg = font.render("YOU WIN!", True, GREEN)
        screen.blit(win_msg, (COLS*TILE//2 - 60, ROWS*TILE//2))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()