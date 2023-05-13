from pygame import*

class GameSprite(sprite.Sprite):
    def __init__(self, image1, speed, rect_x, rect_y, width,height):
        super().__init__()
        self.image = transform.scale(image.load(image1), (width,height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
        self.width = width
        self.height = height

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 500 - self.height - 5:
            self.rect.y += self.speed

    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 500 - self.height - 5:
            self.rect.y += self.speed

rocket1 = Player('himars.png', 5,50,50,50,150)
rocket2 = Player('ukraine.png',5,600,20,50,150)


window = display.set_mode((700,500))
clock = time.Clock()
game = True
while game:
    window.fill((255,255,0))
    rocket1.reset()
    rocket1.update_l()
    rocket2.reset()
    rocket2.update_r()
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(60)
