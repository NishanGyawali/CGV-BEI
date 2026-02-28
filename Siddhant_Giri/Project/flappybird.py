import pygame, sys, random, math, os

pygame.init()
pygame.mixer.init()

# ── Screen Setup ───────────────────────────────────────────────────────────
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
FPS   = 60

# ── Asset Loader — looks inside "assets" folder ────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
def a(filename):
    return os.path.join(BASE_DIR, "assets", filename)

# ── Load Images ────────────────────────────────────────────────────────────
BG_IMG    = pygame.transform.scale(
                pygame.image.load(a("background-day.png")).convert(),
                (WIDTH, HEIGHT))

PIPE_IMG  = pygame.transform.scale(
                pygame.image.load(a("pipe.png")).convert_alpha(),
                (80, 450))

PIPE_FLIP = pygame.transform.flip(PIPE_IMG, False, True)   # flipped = top pipe

# Base (ground) — scale width to fit screen, keep original height
_raw_base = pygame.image.load(a("base.png")).convert()
BASE_H    = 80                                              # height of ground strip
BASE_IMG  = pygame.transform.scale(_raw_base, (WIDTH, BASE_H))
BASE_W    = WIDTH                                          # tiling width
GROUND_Y  = HEIGHT - BASE_H                               # where ground starts

BIRD_FRAMES = [
    pygame.transform.scale(pygame.image.load(a("bluebird-upflap.png")).convert_alpha(),  (51, 36)),
    pygame.transform.scale(pygame.image.load(a("bluebird-midflap.png")).convert_alpha(),  (51, 36)),
    pygame.transform.scale(pygame.image.load(a("bluebird-downflap.png")).convert_alpha(), (51, 36)),
]

# ── Load Sounds ────────────────────────────────────────────────────────────
def load_sound(filename):
    try:    return pygame.mixer.Sound(a(filename))
    except: return None


SND_POINT = load_sound("sfx_point.wav")
SND_HIT   = load_sound("sfx_hit.wav")

# ── Colors & Fonts ─────────────────────────────────────────────────────────
WHITE  = (255, 255, 255)
BLACK  = (0,   0,   0)
YELLOW = (255, 210, 0)
RED    = (220, 50,  50)

font_big   = pygame.font.SysFont("Arial", 60, bold=True)
font_small = pygame.font.SysFont("Arial", 30)

# ── Game Constants ─────────────────────────────────────────────────────────
GRAVITY       = 0.4
FLAP_VEL      = -8
MAX_FALL      = 10
PIPE_SPEED    = 4
PIPE_GAP      = 180
PIPE_INTERVAL = 90      # frames between each pipe spawn

# ── Scroll offsets ─────────────────────────────────────────────────────────
bg_x   = 0.0   # background scroll
base_x = 0.0   # base/ground scroll (moves faster with pipes)

def draw_background(scroll=True):
    """Draw scrolling background + scrolling base on top."""
    global bg_x, base_x

    # ── Background — slow scroll ───────────────────────────────────────
    if scroll:
        bg_x = (bg_x + 1) % WIDTH    # modulo scrolling
    x = -int(bg_x)
    screen.blit(BG_IMG, (x, 0))
    screen.blit(BG_IMG, (x + WIDTH, 0))   # second tile fills the gap

    # ── Base — scrolls at pipe speed for consistency ───────────────────
    if scroll:
        base_x = (base_x + PIPE_SPEED) % BASE_W   # modulo scrolling
    bx = -int(base_x)
    screen.blit(BASE_IMG, (bx, GROUND_Y))
    screen.blit(BASE_IMG, (bx + BASE_W, GROUND_Y))   # second tile


# ══════════════════════════════════════════════════════════════════════════
#  BIRD
# ══════════════════════════════════════════════════════════════════════════
class Bird:
    def __init__(self):
        self.x       = 200
        self.y       = float(HEIGHT // 2)
        self.vel     = 0.0
        self.angle   = 0.0
        self.alive   = True
        self.frame   = 0    # which sprite frame (0,1,2)
        self.frame_t = 0    # frame timer

    def flap(self):
        self.vel = FLAP_VEL              # Euler — push velocity upward

    def update(self):
        # ── Euler Integration ──────────────────────────────────────────
        self.vel  = min(self.vel + GRAVITY, MAX_FALL)
        self.y   += self.vel

        # ── Lerp — smoothly tilt angle toward target ───────────────────
        target      = max(-60.0, 20.0 - self.vel * 5)
        self.angle += (target - self.angle) * 0.15

        # ── Sprite Frame Cycling ───────────────────────────────────────
        self.frame_t += 1
        if self.frame_t >= 5:
            self.frame_t = 0
            self.frame   = (self.frame + 1) % 3   # 0 → 1 → 2 → 0

        # ── Death: hit ground or ceiling ───────────────────────────────
        if self.y >= GROUND_Y - 18 or self.y <= 0:
            self.alive = False

    def draw(self):
        # Rotozoom — rotate sprite by current angle
        rotated = pygame.transform.rotozoom(BIRD_FRAMES[self.frame], self.angle, 1)
        screen.blit(rotated, rotated.get_rect(center=(self.x, int(self.y))))

    def get_rect(self):
        m = 5   # shrink hitbox slightly for fair collision
        return pygame.Rect(self.x - 20 + m, int(self.y) - 15 + m, 40 - m*2, 30 - m*2)


# ══════════════════════════════════════════════════════════════════════════
#  PIPE
# ══════════════════════════════════════════════════════════════════════════
class Pipe:
    W = 80
    H = 450

    def __init__(self):
        # Constrained random — gap always within safe range
        self.gap_y  = random.randint(120, GROUND_Y - PIPE_GAP - 100)
        self.x      = float(WIDTH + 10)
        self.scored = False

    def update(self):
        self.x -= PIPE_SPEED       # move left each frame

    def draw(self):
        screen.blit(PIPE_FLIP, (int(self.x), self.gap_y - self.H))    # top pipe
        screen.blit(PIPE_IMG,  (int(self.x), self.gap_y + PIPE_GAP))  # bottom pipe

    def off_screen(self):
        return self.x < -self.W

    def hit(self, bird_rect):
        # AABB Collision — check top and bottom pipe separately
        top    = pygame.Rect(int(self.x), 0,                     self.W, self.gap_y)
        bottom = pygame.Rect(int(self.x), self.gap_y + PIPE_GAP, self.W, HEIGHT)
        return bird_rect.colliderect(top) or bird_rect.colliderect(bottom)


# ══════════════════════════════════════════════════════════════════════════
#  PARTICLE
# ══════════════════════════════════════════════════════════════════════════
class Particle:
    def __init__(self, x, y):
        angle         = random.uniform(0, math.pi * 2)   # polar → cartesian
        speed         = random.uniform(2, 5)
        self.x        = float(x)
        self.y        = float(y)
        self.vx       = math.cos(angle) * speed
        self.vy       = math.sin(angle) * speed - 2
        self.life     = random.randint(15, 30)
        self.max_life = self.life

    def update(self):
        self.x   += self.vx
        self.y   += self.vy
        self.vy  += 0.2        # particle gravity
        self.life -= 1

    def draw(self):
        alpha = int(255 * self.life / self.max_life)   # fade as life drops
        s = pygame.Surface((8, 8), pygame.SRCALPHA)
        pygame.draw.circle(s, (*YELLOW, alpha), (4, 4), 4)
        screen.blit(s, (int(self.x) - 4, int(self.y) - 4))


# ── Helper: centered text with shadow ─────────────────────────────────────
def show_text(text, font, color, cx, y):
    shadow = font.render(text, True, BLACK)
    surf   = font.render(text, True, color)
    screen.blit(shadow, (cx - shadow.get_width()//2 + 2, y + 2))
    screen.blit(surf,   (cx - surf.get_width()//2,       y))


# ══════════════════════════════════════════════════════════════════════════
#  MENU SCREEN
# ══════════════════════════════════════════════════════════════════════════
def menu_screen(best):
    t = 0
    while True:
        clock.tick(FPS)
        t += 1

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:            pygame.quit(); sys.exit()
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_SPACE:      return
                if ev.key == pygame.K_ESCAPE:     pygame.quit(); sys.exit()
            if ev.type == pygame.MOUSEBUTTONDOWN: return

        draw_background(scroll=True)

        # Sine wave — title bobs up and down
        bob = int(10 * math.sin(t * 0.07))
        show_text("FLAPPY BIRD", font_big,   YELLOW, WIDTH//2, 140 + bob)
        show_text("SPACE or CLICK to start", font_small, WHITE, WIDTH//2, 265)

        if best > 0:
            show_text(f"Best: {best}", font_small, YELLOW, WIDTH//2, 315)

        # Pulsing hint — sine controls alpha
        pulse = int(150 + 100 * math.sin(t * 0.08))
        hint  = font_small.render("Press SPACE", True, WHITE)
        hint.set_alpha(pulse)
        screen.blit(hint, (WIDTH//2 - hint.get_width()//2, 400))

        pygame.display.flip()


# ══════════════════════════════════════════════════════════════════════════
#  GAME SCREEN
# ══════════════════════════════════════════════════════════════════════════
def game_screen(best):
    bird      = Bird()
    pipes     = []
    particles = []
    score     = 0
    pipe_t    = 0
    started   = False

    while True:
        clock.tick(FPS)

        # ── Events ──────────────────────────────────────────────────────
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT: pygame.quit(); sys.exit()
            if ev.type == pygame.KEYDOWN:
                if ev.key in (pygame.K_SPACE, pygame.K_UP):
                    if not started: started = True
                    if bird.alive:  bird.flap()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if not started: started = True
                if bird.alive:  bird.flap()

        # ── Update ──────────────────────────────────────────────────────
        if started and bird.alive:
            bird.update()

            # Pipe spawn timer
            pipe_t += 1
            if pipe_t >= PIPE_INTERVAL:
                pipe_t = 0
                pipes.append(Pipe())

            for p in pipes:
                p.update()

                # Scoring
                if not p.scored and p.x + Pipe.W < bird.x:
                    p.scored = True
                    score   += 1
                    if SND_POINT: SND_POINT.play()
                    for _ in range(12):
                        particles.append(Particle(bird.x, bird.y))

                # Collision
                if p.hit(bird.get_rect()):
                    bird.alive = False
                    if SND_HIT: SND_HIT.play()

            # Filter — remove off-screen pipes
            pipes = [p for p in pipes if not p.off_screen()]

            # Update & filter particles
            for p in particles: p.update()
            particles = [p for p in particles if p.life > 0]

        elif not started:
            # Sine bob — idle float before game starts
            bird.y = HEIGHT//2 + math.sin(pygame.time.get_ticks() * 0.003) * 8

        # ── Draw ────────────────────────────────────────────────────────
        draw_background(scroll=started)   # draws bg + base together
        for p in pipes:     p.draw()
        for p in particles: p.draw()
        bird.draw()

        show_text(str(score), font_big, WHITE, WIDTH//2, 20)

        if not started:
            show_text("SPACE / CLICK to fly!", font_small, WHITE, WIDTH//2, HEIGHT//2 + 80)

        pygame.display.flip()

        if not bird.alive:
            pygame.time.delay(600)
            return score, max(score, best)


# ══════════════════════════════════════════════════════════════════════════
#  GAME OVER SCREEN
# ══════════════════════════════════════════════════════════════════════════
def gameover_screen(score, best):
    t = 0
    while True:
        clock.tick(FPS)
        t += 1

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:            pygame.quit(); sys.exit()
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_SPACE:      return "restart"
                if ev.key == pygame.K_ESCAPE:     return "menu"
            if ev.type == pygame.MOUSEBUTTONDOWN: return "restart"

        draw_background(scroll=False)

        # Dark overlay — alpha compositing
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        screen.blit(overlay, (0, 0))

        show_text("GAME OVER",        font_big,   RED,    WIDTH//2, 160)
        show_text(f"Score : {score}", font_small, WHITE,  WIDTH//2, 280)
        show_text(f"Best  : {best}",  font_small, YELLOW, WIDTH//2, 330)

        if score >= best and score > 0:
            show_text("NEW BEST!", font_small, YELLOW, WIDTH//2, 380)

        # Pulsing hint
        pulse = int(150 + 100 * math.sin(t * 0.08))
        hint  = font_small.render("SPACE / CLICK = Restart     ESC = Menu", True, WHITE)
        hint.set_alpha(pulse)
        screen.blit(hint, (WIDTH//2 - hint.get_width()//2, 450))

        pygame.display.flip()




def main():
    best = 0
    while True:
        menu_screen(best)                           # STATE 1 : Menu
        while True:
            score, best = game_screen(best)         # STATE 2 : Game
            action = gameover_screen(score, best)   # STATE 3 : Game Over
            if action == "menu": break

main()