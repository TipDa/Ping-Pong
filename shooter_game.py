from pygame import *
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Ping-Pong')
back = (200,255,255)
window.fill(back)

FPS=60
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, win_width, win_height):
    
        self.image = transform.scale(image.load(player_image), (win_width,win_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

ball = GameSprite("мячик.png", 200, 200, 4, 50, 50)
racket_l = Player('ракетка.png', 30, 200, 4, 50, 80)
racket_r = Player('ракетка.png', 520, 200, 4, 50, 80)

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))
win1 = font.render('PLAYER 1 WIN!', True, (180, 0, 0))
win2 = font.render('PLAYER 2 WIN!', True, (180, 0, 0))
speed_x = 3
speed_y = 3
finish = False
game = True

score_l = 0
score_r = 0

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        racket_l.update_l()
        racket_r.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket_l, ball):
            speed_x *= -1
            speed_y *= 1
            score_l += 1

        if sprite.collide_rect(racket_r, ball):
            speed_x *= -1
            speed_y *= 1
            score_r += 1

        if score_l >= 5:
            finish = True
            window.blit(win1, (200, 200))
        if score_r >= 5:
            finish = True
            window.blit(win2, (200, 200))

        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1

    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200, 200))
        game_over = True

    if ball.rect.x > win_width:
        finish = True
        window.blit(lose2, (200, 200))
        game_over = True


        
    ball.reset()
    racket_l.update()
    racket_l.reset()
    racket_r.update()
    racket_r.reset()


    display.update()
    clock.tick(FPS)
