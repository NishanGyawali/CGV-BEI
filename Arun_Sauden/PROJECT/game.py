import pygame as pg
import sys
import time
import os
from bird import Bird
from pipe import Pipe

pg.init()
pg.mixer.init()  #For the sound 


class Game:

    def __init__(self):

        # Window
        self.width = 600
        self.height = 768
        self.scale_factor = 1.5
        self.win = pg.display.set_mode((self.width, self.height))
        pg.display.set_caption("Flappy Bird Ultimate")
        self.clock = pg.time.Clock()

        # Game settings
        self.move_speed = 250
        self.pipe_spawn_time = 100
        self.difficulty = "Easy"

        # Game objects
        self.bird = Bird(self.scale_factor)
        self.is_enter_pressed = False
        self.first_flap_done = False
        self.pipes = []
        self.pipe_generate_counter = 0
        self.game_over = False

        # Score
        self.score = 0
        self.high_score = self.loadHighScore()

        # Load sounds
        self.loadSounds()
        self.setUpBgAndGround()

        # Start menu
        self.mainMenu()
        self.gameLoop()

    # -->HIGH SCORE<--
    def loadHighScore(self):
        if os.path.exists("highscore.txt"):
            with open("highscore.txt", "r") as f:#used to open text in read mode
                return int(f.read())
        return 0

    def saveHighScore(self):
        with open("highscore.txt", "w") as f:
            f.write(str(self.high_score))

    #Sound
    def loadSounds(self):
        try:
            base_path = os.path.join("assets", "sfx")
            self.flap_sound = pg.mixer.Sound(os.path.join(base_path, "flap.wav"))
            self.hit_sound = pg.mixer.Sound(os.path.join(base_path, "dead.mp3"))
            self.point_sound = pg.mixer.Sound(os.path.join(base_path, "score.wav"))
            
            #SOUND VOLUME SETTING

            self.flap_sound.set_volume(1)
            self.hit_sound.set_volume(0.1)
            self.point_sound.set_volume(0.1)

        except Exception as e:
            print("Error loading sounds:", e)
            self.flap_sound = None
            self.hit_sound = None
            self.point_sound = None

    # MAIN MENU 
    def mainMenu(self):

        font = pg.font.SysFont("Arial", 50)
        small_font = pg.font.SysFont("Arial", 30)
        menu_active = True

        while menu_active:

            self.win.fill((135, 206, 235))

            title = font.render("Flappy Bird", True, (0, 0, 0))
            start_game = small_font.render("1 - Start Game", True, (0, 0, 0))
            difficulty_opt = small_font.render("2 - Difficulty", True, (0, 0, 0))
            quit_game = small_font.render("Q - Quit", True, (0, 0, 0))

            self.win.blit(title, (170, 180))
            self.win.blit(start_game, (200, 300))
            self.win.blit(difficulty_opt, (200, 350))
            self.win.blit(quit_game, (200, 400))

            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_1:
                        menu_active = False
                        return

                    if event.key == pg.K_2:
                        self.difficultyMenu()

                    if event.key == pg.K_q:
                        pg.quit()
                        sys.exit()

    # DIFFICULTY MENU
    def difficultyMenu(self):

        font = pg.font.SysFont("Arial", 50)
        small_font = pg.font.SysFont("Arial", 30)
        diff_active = True

        while diff_active:

            self.win.fill((135, 206, 235))

            title = font.render("Select Difficulty", True, (0, 0, 0))
            easy = small_font.render("1 - Easy", True, (0, 0, 0))
            medium = small_font.render("2 - Medium", True, (0, 0, 0))
            hard = small_font.render("3 - Hard", True, (0, 0, 0))
            back = small_font.render("B - Back", True, (0, 0, 0))

            self.win.blit(title, (120, 180))
            self.win.blit(easy, (240, 300))
            self.win.blit(medium, (240, 350))
            self.win.blit(hard, (240, 400))
            self.win.blit(back, (240, 450))

            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_1:
                        self.setDifficulty("Easy")
                        diff_active = False

                    if event.key == pg.K_2:
                        self.setDifficulty("Medium")
                        diff_active = False

                    if event.key == pg.K_3:
                        self.setDifficulty("Hard")
                        diff_active = False

                    if event.key == pg.K_b:
                        diff_active = False

    #Set Difficulty
    def setDifficulty(self, level):

        self.difficulty = level
        #More move speed=faster Bird
        if level == "Easy":
            self.move_speed = 200
            self.pipe_spawn_time = 100

        elif level == "Medium":
            self.move_speed = 250
            self.pipe_spawn_time = 70

        elif level == "Hard":
            self.move_speed = 320
            self.pipe_spawn_time = 50

    # ======= GAME RESTART PART ==========
    def restartGame(self):

        self.pipes.clear()
        self.pipe_generate_counter = 0
        self.game_over = False
        self.is_enter_pressed = False
        self.first_flap_done = False
        self.score = 0

        self.bird.rect.center = (150, 300)
        self.bird.velocity = 0
        self.bird.update_on = False

    # ********GAME LOOP*********
    def gameLoop(self):

        last_time = time.time()

        while True:

            new_time = time.time()
            dt = new_time - last_time
            last_time = new_time

            for event in pg.event.get():

                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                if event.type == pg.KEYDOWN:

                    if event.key == pg.K_RETURN and not self.game_over:
                        self.is_enter_pressed = True

                    if event.key == pg.K_SPACE and self.is_enter_pressed and not self.game_over:
                        self.bird.flap(dt)
                        self.bird.update_on = True
                        self.first_flap_done = True

                        if self.flap_sound:
                            self.flap_sound.play()

                    if event.key == pg.K_r and self.game_over:
                        self.restartGame()

                    if event.key == pg.K_m and self.game_over:
                        self.restartGame()
                        self.mainMenu()

                    if event.key == pg.K_q:
                        pg.quit()
                        sys.exit()

            if self.is_enter_pressed and self.first_flap_done and not self.game_over:
                self.updateEverything(dt)
                self.checkCollisions()

            self.drawEverything()
            pg.display.update()
            self.clock.tick(60)

    # COLLISIONS
    def checkCollisions(self):

        if len(self.pipes):

            if self.bird.rect.bottom >= 568:
                self.bird.rect.bottom = 568
                self.bird.velocity = 0
                self.bird.update_on = False
                self.is_enter_pressed = False
                self.game_over = True

                if self.hit_sound:
                    self.hit_sound.play()

            if (self.bird.rect.colliderect(self.pipes[0].rect_down) or
                    self.bird.rect.colliderect(self.pipes[0].rect_up)):

                self.bird.velocity = 0
                self.bird.update_on = False
                self.is_enter_pressed = False
                self.game_over = True

                if self.hit_sound:
                    self.hit_sound.play()

    # UPDATE
    def updateEverything(self, dt):

        self.ground1_rect.x -= int(self.move_speed * dt)
        self.ground2_rect.x -= int(self.move_speed * dt)

        if self.ground1_rect.right < 0:
            self.ground1_rect.x = self.ground2_rect.right

        if self.ground2_rect.right < 0:
            self.ground2_rect.x = self.ground1_rect.right

        if self.pipe_generate_counter > self.pipe_spawn_time:
            self.pipes.append(Pipe(self.scale_factor, self.move_speed))
            self.pipe_generate_counter = 0

        self.pipe_generate_counter += 1

        for pipe in self.pipes:
            pipe.update(dt)

        for pipe in self.pipes:
            if not hasattr(pipe, "passed"):
                pipe.passed = False

            if pipe.rect_up.right < self.bird.rect.left and not pipe.passed:
                pipe.passed = True
                self.score += 1

                if self.point_sound:
                    self.point_sound.play()

        if len(self.pipes) != 0:
            if self.pipes[0].rect_up.right < 0:
                self.pipes.pop(0)

        self.bird.update(dt)

        if self.score > self.high_score:
            self.high_score = self.score
            self.saveHighScore()

    # Draw
    def drawEverything(self):

        self.win.blit(self.bg_img, (0, -300))

        for pipe in self.pipes:
            pipe.drawPipe(self.win)

        self.win.blit(self.ground1_img, self.ground1_rect)
        self.win.blit(self.ground2_img, self.ground2_rect)
        self.win.blit(self.bird.image, self.bird.rect)

        font = pg.font.SysFont("Arial", 30)

        score_text = font.render(f"Score: {self.score}", True, (0, 0, 0))
        high_text = font.render(f"High Score: {self.high_score}", True, (0, 0, 0))

        self.win.blit(score_text, (20, 20))
        self.win.blit(high_text, (20, 60))

        if self.game_over:

            big_font = pg.font.SysFont("Arial", 50)

            over_text = big_font.render("Game Over", True, (255, 0, 0))
            restart_text = font.render("R - Restart", True, (0, 0, 0))
            menu_text = font.render("M - Menu", True, (0, 0, 0))
            quit_text = font.render("Q - Quit", True, (0, 0, 0))

            self.win.blit(over_text, (170, 250))
            self.win.blit(restart_text, (170, 320))
            self.win.blit(menu_text, (170, 360))
            self.win.blit(quit_text, (170, 400))

    #SETUP 
    def setUpBgAndGround(self):

        self.bg_img = pg.transform.scale_by(
            pg.image.load("assets/bg.png").convert(),
            self.scale_factor
        )

        self.ground1_img = pg.transform.scale_by(
            pg.image.load("assets/ground.png").convert(),
            self.scale_factor
        )

        self.ground2_img = pg.transform.scale_by(
            pg.image.load("assets/ground.png").convert(),
            self.scale_factor
        )

        self.ground1_rect = self.ground1_img.get_rect()
        self.ground2_rect = self.ground2_img.get_rect()

        self.ground1_rect.x = 0
        self.ground2_rect.x = self.ground1_rect.right

        self.ground1_rect.y = 568
        self.ground2_rect.y = 568


#Run Game
game = Game()
