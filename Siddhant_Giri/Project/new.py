import pygame
import sys
import random
import math
import os

pygame.init()
pygame.mixer.init()

# ── Screen ────────────────────────────────────────────────────────────────────
WIDTH, HEIGHT = 1270, 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
CLOCK = pygame.time.Clock()
FPS = 60

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
def asset(f): return os.path.join(BASE_DIR, "Assets", f)

# ── Assets ────────────────────────────────────────────────────────────────────
_raw_bg  = pygame.image.load(asset("background-day.png")).convert()
BG_SCALE = (HEIGHT * 0.35) / _raw_bg.get_height()
BG_SW    = int(_raw_bg.get_width() * BG_SCALE)
BG_IMG   = pygame.transform.scale(_raw_bg, (BG_SW, HEIGHT))

_raw_base = pygame.image.load(asset("base.png")).convert()
BASE_H    = int(38 * HEIGHT / 720)
BASE_SW   = int(_raw_base.get_width() * BG_SCALE)
BASE_IMG  = pygame.transform.scale(_raw_base, (BASE_SW, BASE_H))
GROUND_Y  = HEIGHT - BASE_H

BIRD_SCALE  = 1.5
BIRD_FRAMES = [
    pygame.transform.scale(pygame.image.load(asset("bluebird-upflap.png")).convert_alpha(),
        (int(34*BIRD_SCALE), int(24*BIRD_SCALE))),
    pygame.transform.scale(pygame.image.load(asset("bluebird-midflap.png")).convert_alpha(),
        (int(34*BIRD_SCALE), int(24*BIRD_SCALE))),
    pygame.transform.scale(pygame.image.load(asset("bluebird-downflap.png")).convert_alpha(),
        (int(34*BIRD_SCALE), int(24*BIRD_SCALE))),
]
BIRD_W = BIRD_FRAMES[0].get_width()
BIRD_H = BIRD_FRAMES[0].get_height()

PIPE_W  = 80
PIPE_H  = 450
PIPE_LO = pygame.transform.scale(
    pygame.image.load(asset("pipe.png")).convert_alpha(), (PIPE_W, PIPE_H))
PIPE_UP = pygame.transform.scale(
    pygame.image.load(asset("rotated_pipe.png")).convert_alpha(), (PIPE_W, PIPE_H))

def load_snd(f):
    try: return pygame.mixer.Sound(asset(f))
    except: return None

SND_POINT = load_snd("sfx_point.wav")
SND_HIT   = load_snd("sfx_hit.wav")

# ── Constants ─────────────────────────────────────────────────────────────────
PIPE_SPEED    = 4
PIPE_INTERVAL = int(1.8 * FPS)
PIPE_GAP      = 185

GRAVITY  = 0.38    # gentle gravity — not snappy/jerky
FLAP_VEL = -7.5    # moderate flap impulse
MAX_FALL = 10      # cap so bird never rockets downward

# ── Colours ───────────────────────────────────────────────────────────────────
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
GOLD  = (255, 210,   0)
RED   = (220,  50,  50)

# ── Fonts (created once) ──────────────────────────────────────────────────────
def make_font(size, bold=False):
    for name in ("Bahnschrift", "Segoe UI", "Verdana", "Arial"):
        try: return pygame.font.SysFont(name, size, bold=bold)
        except: pass
    return pygame.font.Font(None, size)

F_TITLE = make_font(110, bold=True)
F_SUB   = make_font(30,  bold=True)
F_BTN   = make_font(40,  bold=True)
F_HINT  = make_font(22)
F_SCORE = make_font(60,  bold=True)
F_GO    = make_font(80,  bold=True)
F_MED   = make_font(52,  bold=True)
F_GAME  = make_font(34)

# ── Shared draw utilities ─────────────────────────────────────────────────────
_bg_x = 0.0

def draw_bg(scroll=True):
    global _bg_x
    if scroll: _bg_x = (_bg_x + 0.5) % BG_SW
    x = -int(_bg_x)
    while x < WIDTH:
        SCREEN.blit(BG_IMG, (x, 0))
        x += BG_SW

def draw_base(off):
    x = -int(off) % BASE_SW
    while x < WIDTH + BASE_SW:
        SCREEN.blit(BASE_IMG, (x - BASE_SW, GROUND_Y))
        x += BASE_SW

def draw_panel(x, y, w, h, alpha=215):
    s = pygame.Surface((w, h), pygame.SRCALPHA)
    s.fill((10, 10, 30, alpha))
    pygame.draw.rect(s, (*GOLD, 255), (0, 0, w, h), 3, border_radius=18)
    SCREEN.blit(s, (x, y))

def center_text(text, font, color, y, sh=3):
    if sh:
        ss = font.render(text, True, (20, 20, 20))
        SCREEN.blit(ss, (WIDTH//2 - ss.get_width()//2 + sh, y + sh))
    s = font.render(text, True, color)
    SCREEN.blit(s, (WIDTH//2 - s.get_width()//2, y))

def draw_btn(rect, text, font, col, hov, mx, my):
    c = hov if rect.collidepoint(mx, my) else col
    pygame.draw.rect(SCREEN, (10,10,10), rect.move(5, 6), border_radius=16)
    pygame.draw.rect(SCREEN, c,     rect, border_radius=16)
    pygame.draw.rect(SCREEN, WHITE, rect, 3, border_radius=16)
    lbl = font.render(text, True, WHITE)
    SCREEN.blit(lbl, lbl.get_rect(center=rect.center))

# ── Particle ──────────────────────────────────────────────────────────────────
class Particle:
    def __init__(self, x, y):
        a  = random.uniform(0, math.pi * 2)
        sp = random.uniform(2, 5)
        self.x, self.y   = x, y
        self.vx, self.vy = math.cos(a)*sp, math.sin(a)*sp - 2
        self.life = self.max_life = random.randint(18, 38)
        self.color = random.choice([GOLD, (255,255,120), (255,180,0)])
        self.r = random.randint(3, 6)

    def update(self):
        self.x += self.vx; self.y += self.vy
        self.vy += 0.2;    self.life -= 1

    def draw(self):
        al = int(255 * self.life / self.max_life)
        s  = pygame.Surface((self.r*2, self.r*2), pygame.SRCALPHA)
        pygame.draw.circle(s, (*self.color, al), (self.r, self.r), self.r)
        SCREEN.blit(s, (int(self.x)-self.r, int(self.y)-self.r))

# ════════════════════════════════════════════════════════════════════════════
#  MENU
# ════════════════════════════════════════════════════════════════════════════
class Menu:
    def __init__(self, best=0):
        self.best     = best
        self.t        = 0
        self.base_off = 0.0
        self.particles= []
        self.bird_f   = 0
        self.bird_ft  = 0
        bw, bh = 400, 72
        cx = WIDTH//2 - bw//2
        self.start_rect = pygame.Rect(cx, HEIGHT//2 + 60,  bw, bh)
        self.quit_rect  = pygame.Rect(cx, HEIGHT//2 + 155, bw, bh)

    def run(self):
        global _bg_x
        _bg_x = 0.0
        while True:
            CLOCK.tick(FPS)
            self.t       += 1
            self.base_off = (self.base_off + PIPE_SPEED) % BASE_SW
            self.bird_ft += 1
            if self.bird_ft >= 7:
                self.bird_ft = 0
                self.bird_f  = (self.bird_f + 1) % 3

            self.particles = [p for p in self.particles if p.life > 0]
            for p in self.particles: p.update()

            mx, my = pygame.mouse.get_pos()
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT: pygame.quit(); sys.exit()
                if ev.type == pygame.KEYDOWN:
                    if ev.key in (pygame.K_SPACE, pygame.K_RETURN): return
                    if ev.key == pygame.K_ESCAPE: pygame.quit(); sys.exit()
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_rect.collidepoint(mx, my):
                        for _ in range(14): self.particles.append(Particle(mx, my))
                        pygame.time.delay(80); return
                    if self.quit_rect.collidepoint(mx, my):
                        pygame.quit(); sys.exit()

            draw_bg(scroll=True)
            draw_base(self.base_off)

            # Title panel
            pw, ph = 760, 210
            px, py = WIDTH//2 - pw//2, 38
            draw_panel(px, py, pw, ph)

            sc  = 1.0 + 0.022 * math.sin(self.t * 0.065)
            ts  = pygame.transform.rotozoom(F_TITLE.render("FLAPPY BIRD", True, GOLD),     0, sc)
            tsh = pygame.transform.rotozoom(F_TITLE.render("FLAPPY BIRD", True, (70,40,0)),0, sc)
            SCREEN.blit(tsh, tsh.get_rect(center=(WIDTH//2+4, py+88+4)))
            SCREEN.blit(ts,  ts.get_rect( center=(WIDTH//2,   py+88)))

            tag = F_SUB.render("Tap  •  Fly  •  Survive", True, (210, 245, 255))
            SCREEN.blit(tag, tag.get_rect(center=(WIDTH//2, py+165)))

            if self.best > 0:
                bs  = F_MED.render(f"Best: {self.best}", True, GOLD)
                bsh = F_MED.render(f"Best: {self.best}", True, (60,40,0))
                bx  = WIDTH - bs.get_width() - 48
                SCREEN.blit(bsh, (bx+3, 48)); SCREEN.blit(bs, (bx, 45))

            bob    = int(18 * math.sin(self.t * 0.06))
            bangle = math.sin(self.t * 0.06) * 14
            big    = pygame.transform.rotozoom(BIRD_FRAMES[self.bird_f], bangle, 3.5)
            SCREEN.blit(big, big.get_rect(center=(WIDTH//2, HEIGHT//2 - 28 + bob)))

            pygame.draw.line(SCREEN, GOLD, (0, HEIGHT//2+48), (WIDTH, HEIGHT//2+48), 2)
            draw_btn(self.start_rect, "▶   START GAME", F_BTN, (30,140,30), (55,200,55), mx, my)
            draw_btn(self.quit_rect,  "✕   QUIT",        F_BTN, (155,35,35),(215,65,65),  mx, my)

            pulse = int(145 + 90 * math.sin(self.t * 0.07))
            hint  = F_HINT.render("SPACE / ENTER to start   •   ESC to quit", True, WHITE)
            hint.set_alpha(pulse)
            SCREEN.blit(hint, hint.get_rect(center=(WIDTH//2, HEIGHT - 24)))

            for p in self.particles: p.draw()
            pygame.display.flip()

# ════════════════════════════════════════════════════════════════════════════
#  GAME OVER
# ════════════════════════════════════════════════════════════════════════════
class GameOver:
    def __init__(self, score, best):
        self.score = score
        self.best  = best
        self.t     = 0
        bw, bh = 290, 68
        self.menu_rect   = pygame.Rect(WIDTH//2 - bw - 22, HEIGHT//2 + 130, bw, bh)
        self.replay_rect = pygame.Rect(WIDTH//2 + 22,       HEIGHT//2 + 130, bw, bh)

    def run(self, base_off):
        while True:
            self.t += 1
            CLOCK.tick(FPS)
            mx, my = pygame.mouse.get_pos()
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT: pygame.quit(); sys.exit()
                if ev.type == pygame.KEYDOWN:
                    if ev.key in (pygame.K_SPACE, pygame.K_RETURN, pygame.K_ESCAPE):
                        return "menu"
                    if ev.key == pygame.K_r:
                        return "restart"
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    if self.menu_rect.collidepoint(mx, my):   return "menu"
                    if self.replay_rect.collidepoint(mx, my): return "restart"

            draw_bg(scroll=False)
            draw_base(base_off)

            ov = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            ov.fill((0, 0, 0, 160))
            SCREEN.blit(ov, (0, 0))

            pw, ph = 580, 380
            px, py = WIDTH//2 - pw//2, HEIGHT//2 - ph//2 - 30
            draw_panel(px, py, pw, ph)

            center_text("GAME OVER", F_GO, RED, py+18, sh=5)
            pygame.draw.line(SCREEN, GOLD, (px+30, py+112), (px+pw-30, py+112), 2)
            center_text(f"Score   {self.score}", F_MED, WHITE, py+128)

            new_best = self.score >= self.best and self.score > 0
            blbl = "★  NEW BEST!" if new_best else f"Best    {self.best}"
            center_text(blbl, F_MED, GOLD if new_best else (200,200,200), py+200)

            pulse = int(140 + 85 * math.sin(self.t * 0.08))
            hint  = F_HINT.render("SPACE · ESC → Menu      R → Replay", True, (215,215,215))
            hint.set_alpha(pulse)
            SCREEN.blit(hint, hint.get_rect(center=(WIDTH//2, py+300)))

            draw_btn(self.menu_rect,   "⏪  MENU",  F_BTN, (45,75,190), (75,115,230), mx, my)
            draw_btn(self.replay_rect, "▶  REPLAY", F_BTN, (35,155,35), (65,205,65),  mx, my)
            pygame.display.flip()

# ════════════════════════════════════════════════════════════════════════════
#  GAME
# ════════════════════════════════════════════════════════════════════════════
class Game:
    def __init__(self, best=0):
        self.best = best
        self.reset()

    def reset(self):
        pygame.mixer.stop()
        global _bg_x; _bg_x = 0.0
        self.bird_x   = 200.0
        self.bird_y   = float(HEIGHT//2 - BIRD_H//2)
        self.vel_y    = 0.0
        self.angle    = 0.0
        self.frame    = 0
        self.frame_t  = 0
        self.score    = 0
        self.pipes    = []
        self.pipe_t   = PIPE_INTERVAL
        self.base_off = 0.0
        self.alive    = True
        self.started  = False
        self.flash    = 0
        self.particles= []

    def _spawn(self):
        gap_y = random.randint(140, GROUND_Y - PIPE_GAP - 140)
        self.pipes.append({'x': float(WIDTH + 10), 'gap_y': gap_y, 'scored': False})

    def flap(self):
        if self.alive:
            self.vel_y   = FLAP_VEL
            self.angle   = 25.0
            self.started = True

    def update(self):
        for p in self.particles: p.update()
        self.particles = [p for p in self.particles if p.life > 0]

        if not self.alive: return

        if not self.started:
            self.bird_y = HEIGHT//2 - BIRD_H//2 + math.sin(pygame.time.get_ticks()*0.003) * 8
            return

        # Smooth physics
        self.vel_y  = min(self.vel_y + GRAVITY, MAX_FALL)
        self.bird_y += self.vel_y

        # Gradual nose-down as falling, instant nose-up on flap
        target = max(-75.0, 25.0 - self.vel_y * 6)
        self.angle += (target - self.angle) * 0.15

        self.frame_t += 1
        if self.frame_t >= 5:
            self.frame_t = 0
            self.frame   = (self.frame + 1) % 3

        self.pipe_t += 1
        if self.pipe_t >= PIPE_INTERVAL:
            self.pipe_t = 0
            self._spawn()
        for p in self.pipes: p['x'] -= PIPE_SPEED
        self.pipes = [p for p in self.pipes if p['x'] > -PIPE_W - 10]

        for p in self.pipes:
            if not p['scored'] and p['x'] + PIPE_W < self.bird_x:
                p['scored'] = True
                self.score += 1
                if SND_POINT: SND_POINT.play()
                bx = int(self.bird_x) + BIRD_W//2
                by = int(self.bird_y) + BIRD_H//2
                for _ in range(14): self.particles.append(Particle(bx, by))

        self.base_off = (self.base_off + PIPE_SPEED) % BASE_SW

        m  = 4
        hb = pygame.Rect(int(self.bird_x)+m, int(self.bird_y)+m, BIRD_W-m*2, BIRD_H-m*2)
        if hb.bottom >= GROUND_Y or hb.top <= 0:
            self._die(); return
        for p in self.pipes:
            px = int(p['x'])
            if (hb.colliderect(pygame.Rect(px, 0, PIPE_W, p['gap_y'])) or
                    hb.colliderect(pygame.Rect(px, p['gap_y']+PIPE_GAP, PIPE_W, HEIGHT))):
                self._die(); return

    def _die(self):
        self.alive = False
        self.flash = 10
        if self.score > self.best: self.best = self.score
        if SND_HIT: SND_HIT.play()

    def draw(self):
        draw_bg(scroll=self.started)

        for p in self.pipes:
            SCREEN.blit(PIPE_UP, (int(p['x']), p['gap_y'] - PIPE_H))
            SCREEN.blit(PIPE_LO, (int(p['x']), p['gap_y'] + PIPE_GAP))

        draw_base(self.base_off)

        rotated = pygame.transform.rotozoom(BIRD_FRAMES[self.frame], self.angle, 1)
        SCREEN.blit(rotated, rotated.get_rect(
            center=(int(self.bird_x) + BIRD_W//2, int(self.bird_y) + BIRD_H//2)))

        for p in self.particles: p.draw()

        sh = F_SCORE.render(str(self.score), True, BLACK)
        sc = F_SCORE.render(str(self.score), True, WHITE)
        cx = WIDTH//2 - sc.get_width()//2
        SCREEN.blit(sh, (cx+3, 33)); SCREEN.blit(sc, (cx, 30))

        if self.flash > 0:
            fl = pygame.Surface((WIDTH, HEIGHT))
            fl.fill(WHITE); fl.set_alpha(self.flash * 24)
            SCREEN.blit(fl, (0, 0))
            self.flash -= 1

        if not self.started:
            pulse = int(155 + 95 * math.sin(pygame.time.get_ticks() * 0.004))
            hint  = F_GAME.render("PRESS SPACE TO FLY!", True, WHITE)
            sh2   = F_GAME.render("PRESS SPACE TO FLY!", True, BLACK)
            hx = WIDTH//2 - hint.get_width()//2
            hy = HEIGHT//2 + 90
            sh2.set_alpha(pulse); hint.set_alpha(pulse)
            SCREEN.blit(sh2, (hx+2, hy+2)); SCREEN.blit(hint, (hx, hy))

    def run(self):
        while True:
            CLOCK.tick(FPS)
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT: pygame.quit(); sys.exit()
                if ev.type == pygame.KEYDOWN:
                    if ev.key in (pygame.K_SPACE, pygame.K_UP) and self.alive:
                        self.flap()
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    if ev.button == 1 and self.alive:
                        self.flap()

            self.update()
            self.draw()
            pygame.display.flip()

            if not self.alive and self.flash == 0:
                pygame.time.delay(400)
                return self.score, self.best, self.base_off

# ════════════════════════════════════════════════════════════════════════════
#  ENTRY POINT
# ════════════════════════════════════════════════════════════════════════════
def main():
    best = 0
    while True:
        Menu(best).run()
        while True:
            g = Game(best)
            score, best, base_off = g.run()
            if GameOver(score, best).run(base_off) == "menu":
                break

main()