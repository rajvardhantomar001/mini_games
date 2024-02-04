import pygame
from pygame.locals import *
import time
import random

class Apple:
    global size, BACKGROUND_COLOR
    def __init__(self, parent_screen):
        self.parent_Screen = parent_screen
        self.image = pygame.image.load("APPLE.png").convert()
        self.x = 120
        self.y = 120

    def draw(self):
        self.parent_Screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1, 19) * size
        self.y = random.randint(1, 14) * size


class Snake:
    global size, BACKGROUND_COLOR
    def __init__(self, parent_screen):
        self.parent_Screen = parent_screen
        self.block = pygame.image.load("circle.png").convert()
        self.direction = "down"

        self.length = 1
        self.x = [40]
        self.y = [40]

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self):
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        if self.direction == 'left':
            self.x[0] -= size
        if self.direction == 'right':
            self.x[0] += size
        if self.direction == 'up':
            self.y[0] -= size
        if self.direction == 'down':
            self.y[0] += size

        self.draw()

    def draw(self):
        self.parent_Screen.fill(BACKGROUND_COLOR)
        for i in range(self.length):
            self.parent_Screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.update()

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)


class Game:
    global size, BACKGROUND_COLOR
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.play_background_music()
        pygame.display.set_caption("Codebasics Snake And Apple Game")
        self.surface = pygame.display.set_mode((800, 600))
        self.snake = Snake(self.surface)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def reset(self):
        self.snake = Snake(self.surface)
        self.apple = Apple(self.surface)

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + size:
            if y1 >= y2 and y1 < y2 + size:
                return True
        return False

    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(score, (250, 10))
        
    def play_sound(self, sound):
        sound = pygame.mixer.Sound(f"{sound}.mp3")
        pygame.mixer.Sound.play(sound)

    def play_background_music(self):
        pygame.mixer.music.load("bg_music_1.mp3")
        pygame.mixer.music.play(-1, 0)

    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.update()

        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.play_sound("ding")
            self.snake.increase_length()
            self.apple.move()

        for i in range(2, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.play_sound("crash")
                raise "GAME OVER"

    def show_game_over(self):
        self.surface.fill(BACKGROUND_COLOR)
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Game is over! Your score is {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(line1, (250, 200))
        line2 = font.render("To play again press Enter. To exit press Escape!", True, (255, 255, 255))
        self.surface.blit(line2, (150, 250))

        pygame.display.flip()
        pygame.mixer.music.pause()

    def run(self):
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()

                    if event.key == K_RETURN:
                        pygame.mixer.music.unpause()

                        pause = False

                    if not pause:
                        if event.key == K_LEFT:
                            self.snake.move_left()

                        if event.key == K_RIGHT:
                            self.snake.move_right()

                        if event.key == K_UP:
                            self.snake.move_up()

                        if event.key == K_DOWN:
                            self.snake.move_down()

                elif event.type == QUIT:
                    running = False

            try:
                if not pause:
                    self.play()

            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()
            
            if(pause == False):
                for i in range(self.snake.length):
                    try:
                        if(self.snake.x[i] > 760 or self.snake.x[i] < -2 or self.snake.y[i] > 560 or self.snake.y[i] < -2):
                            self.show_game_over()
                            pause = True
                            self.reset()
                    except:
                        pass

            time.sleep(.20)

def start_abhi():
    global size, BACKGROUND_COLOR
    size = 40
    BACKGROUND_COLOR = (80, 199, 90)
    game = Game()
    game.run()
