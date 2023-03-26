from pygame import*

background = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(background)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
ball = GameSprite('мяч.png', 200, 200, 4, 50, 50)
speed_x = 3
speed_y = 3
finish = False

game = True
clock = time.Clock()
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.fill(background)
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        ball.reset()
    display.update()
    clock.tick(60)