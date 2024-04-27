from pygame import *

class Game(sprite.Sprite):
    def __init__(self,player_image, p_x, p_y, p_s):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(50,50))
        self.speed = p_s
        self.rect = self.image.get_rect()
        self.rect.x = p_x
        self.rect.y = p_y

    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
class Move1(Game):
    def move1(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 620:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        

class Move2(Game):
    def move2(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 620:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

        


window = display.set_mode((700,500))
display.set_caption("Вогонь і Вода")

bg = transform.scale(image.load("wall.jpg"),(700,500))
player1 = Move1("fire.png",50,350,4)
player2 = Move2("water.png",50,420,4)


FPS = 60
clock = time.Clock()

game = True

font.init()
font = font.Font(None,70)
win = font.render("YOU WIN!", True, (255,215,0))
lose = font.render("GAME OVER", True, (180,0,0))



#mixer.init()
#mixer.music.load("hghgh.mp3")
#mixer.music.play()
finish = False
a = 0
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(bg,(0,0))
        player1.move1()
        player1.reset()
        player2.move2()
        player2.reset()

    display.update()
    clock.tick(FPS)