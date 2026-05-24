from pygame import *
from random import * 
import random
class GameSprite(sprite.Sprite):
    def __init__(self, image_file, x, y, speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(image_file), (size_x, size_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < height - 150:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < height - 150:
            self.rect.y += self.speed


width = 600
height = 500
window = display.set_mode((width, height))
display.set_caption("Ping-Pong")
back = (138, 43, 226)
window.fill(back)
clock = time.Clock()
FPS = 60


font.init()
font1 = font.SysFont("Arial", 36)
font_score = font.SysFont("Arial", 36)
lose1 = font1.render("PLAYER 1 LOSER!", True, (240, 255, 240))
lose2 = font1.render("PLAYER 2 LOSER!", True, (240, 255, 240))


score1 = 0
score2 = 0


racket1 = Player("platform.png", 30, 200, 5, 50, 150)
racket2 = Player("platform.png", 520, 200, 5, 50, 150)
ball = GameSprite("tenisping.png", width//2, height//2, 4, 50, 50)


ball_x = randint(3, 5)
ball_y = randint(1, 4)

finish = False
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.fill(back)

       
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += ball_x
        ball.rect.y += ball_y

      
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            ball_x *= -1 
            ball_x = randint(2, 5) * (1 if ball_x > 0 else -1)
            ball_y = randint(2, 5) * (1 if ball_y > 0 else -1)

        if ball.rect.y < 0 or ball.rect.y > height - ball.rect.height:
            ball_y *= -1
            ball_y = randint(2, 5) * (1 if ball_y > 0 else -1)
            ball_x = randint(2, 5) * (1 if ball_x > 0 else -1)

        if ball.rect.x < 0: 
            score2 += 1
            ball.rect.x = width//2
            ball.rect.y = height//2
            ball_x = randint(2, 5)
            ball_y = randint(2, 5) * (random.choice([-1, 1]))

        if ball.rect.x > width - ball.rect.width: 
            score1 += 1
            ball.rect.x = width//2
            ball.rect.y = height//2
            ball_x = -randint(2, 5) 
            ball_y = randint(2, 5) * (random.choice([-1, 1])) 

       
        text_score1 = font_score.render(f"Player 1: {score1}", True, (255, 255, 255))
        text_score2 = font_score.render(f"Player 2: {score2}", True, (255, 255, 255))
        window.blit(text_score1, (30, 10))
        window.blit(text_score2, (width - text_score2.get_width() - 30, 10))

     
        racket1.reset()
        racket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)