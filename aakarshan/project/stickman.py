import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 900, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stickman Run Adventure")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)
big_font = pygame.font.SysFont(None, 60)

# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (180,180,180)
BLUE = (0,0,200)
RED = (200,0,0)
GOLD = (255,215,0)

# Load Images
crow_img = pygame.image.load("crow.png").convert_alpha()
crow_img = pygame.transform.scale(crow_img, (60, 50))

dog_img = pygame.image.load("dog.png").convert_alpha()
dog_img = pygame.transform.scale(dog_img, (70, 60))

# High Scores
high_scores = {"easy":0,"medium":0,"hard":0}

# ---------------- PLAYER ----------------
def draw_stickman(x,y,run):
    pygame.draw.circle(screen, BLACK, (x+10,y+10),10)
    pygame.draw.line(screen, BLACK, (x+10,y+20),(x+10,y+40),3)

    if run:
        pygame.draw.line(screen, BLACK, (x+10,y+40),(x+20,y+55),3)
        pygame.draw.line(screen, BLACK, (x+10,y+40),(x,y+55),3)
    else:
        pygame.draw.line(screen, BLACK, (x+10,y+40),(x+15,y+55),3)
        pygame.draw.line(screen, BLACK, (x+10,y+40),(x+5,y+55),3)

    pygame.draw.line(screen, BLACK, (x+10,y+25),(x+20,y+35),3)
    pygame.draw.line(screen, BLACK, (x+10,y+25),(x,y+35),3)

# ---------------- OBSTACLE ----------------
class Obstacle:
    def __init__(self,level):
        self.type = random.choice(["crow","dog","enemy"])
        self.x = WIDTH

        if level=="easy": self.speed=5
        elif level=="medium": self.speed=8
        else: self.speed=12

        if self.type=="crow":
            self.image = crow_img
            self.y = HEIGHT-180
        elif self.type=="dog":
            self.image = dog_img
            self.y = HEIGHT-100
        else:
            self.image = None
            self.y = HEIGHT-90

    def move(self):
        self.x -= self.speed

    def draw(self):
        if self.type=="enemy":
            draw_stickman(self.x,self.y,True)
        else:
            screen.blit(self.image,(self.x,self.y))

    def rect(self):
        if self.type=="enemy":
            return pygame.Rect(self.x,self.y,30,60)
        else:
            return self.image.get_rect(topleft=(self.x,self.y))

# ---------------- COIN (GROUND ONLY) ----------------
class Coin:
    def __init__(self,level):
        self.x = WIDTH
        self.y = HEIGHT-60   # ALWAYS ON GROUND
        self.radius = 10

        if level=="easy": self.speed=5
        elif level=="medium": self.speed=8
        else: self.speed=12

    def move(self):
        self.x -= self.speed

    def draw(self):
        pygame.draw.circle(screen,GOLD,(self.x,self.y),self.radius)

    def rect(self):
        return pygame.Rect(self.x-10,self.y-10,20,20)

# ---------------- SIMPLE MENU ----------------
def menu():
    while True:
        screen.fill(WHITE)
        title = big_font.render("STICKMAN RUN",True,BLUE)
        screen.blit(title,(250,100))

        screen.blit(font.render("1 - Easy",True,BLACK),(380,220))
        screen.blit(font.render("2 - Medium",True,BLACK),(380,260))
        screen.blit(font.render("3 - Hard",True,BLACK),(380,300))
        screen.blit(font.render("Q - Quit",True,RED),(380,340))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_1: return "easy"
                if event.key==pygame.K_2: return "medium"
                if event.key==pygame.K_3: return "hard"
                if event.key==pygame.K_q:
                    pygame.quit(); sys.exit()

# ---------------- GAME ----------------
def game(level):

    player_x=100
    player_y=HEIGHT-90
    velocity_y=0
    gravity=0.8
    jump_power=-15
    is_jump=False
    run=False

    score=0
    score_value = 10 if level=="easy" else 15 if level=="medium" else 20

    obstacles=[]
    coins=[]

    spawn_timer=0
    coin_timer=0
    paused=False
    game_over=False

    while True:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit(); sys.exit()

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_p:
                    paused = not paused

                if not paused and not game_over:
                    if event.key==pygame.K_SPACE and not is_jump:
                        velocity_y=jump_power
                        is_jump=True

                if game_over and event.key==pygame.K_r:
                    return

        if not paused and not game_over:

            run = not run

            velocity_y+=gravity
            player_y+=velocity_y

            if player_y>=HEIGHT-90:
                player_y=HEIGHT-90
                is_jump=False

            spawn_timer+=1
            coin_timer+=1

            # Spawn obstacles
            if spawn_timer>80:
                obstacles.append(Obstacle(level))
                spawn_timer=0

            # Spawn coins safely away from obstacles
            if coin_timer>120:
                safe_x = WIDTH
                if obstacles:
                    # Ensure coin spawns at least 150 pixels ahead of the last obstacle
                    last_obstacle = obstacles[-1]
                    safe_x = max(WIDTH, last_obstacle.x + 150)
                coin = Coin(level)
                coin.x = safe_x
                coins.append(coin)
                coin_timer = 0

            for o in obstacles: o.move()
            for c in coins: c.move()

            player_rect=pygame.Rect(player_x,player_y,25,60)

            # Collision
            for o in obstacles:
                if player_rect.colliderect(o.rect()):
                    game_over=True

            # Coin collection (+5)
            for c in coins[:]:
                if player_rect.colliderect(c.rect()):
                    score+=5
                    coins.remove(c)

            # Passed obstacle score
            for o in obstacles[:]:
                if o.x<-100:
                    score+=score_value
                    obstacles.remove(o)

        pygame.draw.line(screen,GRAY,(0,HEIGHT-40),(WIDTH,HEIGHT-40),5)

        draw_stickman(player_x,player_y,run)

        for o in obstacles: o.draw()
        for c in coins: c.draw()

        if score>high_scores[level]:
            high_scores[level]=score

        screen.blit(font.render(f"Score: {score}",True,BLUE),(20,20))
        screen.blit(font.render(f"High ({level}): {high_scores[level]}",True,BLACK),(20,50))

        if paused:
            screen.blit(big_font.render("PAUSED",True,RED),(320,200))

        if game_over:
            screen.blit(big_font.render("GAME OVER",True,RED),(260,200))
            screen.blit(font.render("Press R to Restart",True,BLACK),(330,260))

        pygame.display.update()
        clock.tick(60)

# ---------------- MAIN ----------------
while True:
    level = menu()
    game(level)