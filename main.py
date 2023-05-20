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

rocket1 = Player('russia.jpg', 10,50,50,50,150)
rocket2 = Player('ukraine.jpg',10,600,20,50,150)

krim = GameSprite('krim.png',10,350,250,150,70)

window = display.set_mode((700,500))
clock = time.Clock()
game = True

finish = False

speed_x = 3

speed_y = 3

font.init()

font1 = font.Font(None, 35)
lose1 = font1.render('Россия сдала Крым!',True,(180,0,0))
lose2 = font1.render('Украине не удалось взять Крым!',True,(180,0,0))

while game:
    if finish != True:

        window.fill((0,0,0))
        rocket1.reset()
        rocket1.update_l()
        rocket2.reset()
        rocket2.update_r()
        krim.reset()


        krim.rect.x += speed_x
        krim.rect.y += speed_y

        if sprite.collide_rect(rocket1,krim) or sprite.collide_rect(rocket2,krim):
            speed_x *= -1

        if krim.rect.y > 500-70 or krim.rect.y < 0:
            speed_y *= -1
        if krim.rect.x < 0:
            finish = True
            window.blit(lose1,(200,200))

        if krim.rect.x > 550:
            finish = True
            window.blit(lose2,(200,200))

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(60)
