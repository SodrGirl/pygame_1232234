from pygame import*
import random
init()

w=600
h=400
FPS =60

screen = display.set_mode((w, h))#КАРТЕЖ!!!
display.set_caption("MAKE A SALAD")#makes a name
clock = time.Clock()
class You:
    def __init__(self, x, y):
        self.image = transform.scale(image.load("basket.png"), (80, 60))
        self.x = x
        self.y = y
        self.speed = 10
    def update(self, keys):#your's reaction on the keyboard
        if keys[K_LEFT] and self.x>0:#check if there any spase to go + is the key pressed
            self.x -= self.speed
        if keys[K_RIGHT] and self.x < w - 80:#check if there any spase to go + is the key pressed
            self.x += self.speed
    def appear(self, screen):#draws you on the window "screen"
        screen.blit(self.image, (self.x, self.y))
    def get_rect(self):#placing
        return self.image.get_rect(topleft=(self.x, self.y))

class Vegetables:
    def __init__(self, x, y, v_type, v_images):
        self.image = veg_images[v_type]
        self.x = x
        self.y = y
        self.speed = 4
    def update(self):
        self.y+=self.speed
    def appear(self, screen):#draws you on the window "screen"
        screen.blit(self.image, (self.x, self.y))
    def get_rect(self):#placing
        return self.image.get_rect(topleft=(self.x, self.y))
def load_image(path, size):
    img = image.load(path)
    return transform.scale(img, size)

veg_images = {
    "apple": load_image("apple.png", (40, 40)),
    "banana": load_image("banana.png", (40, 40)),
    "orange": load_image("orange.png", (40, 40)),
}


bowl =You(250,  h - 70)
vegs = []
points = 0
lives = 3
v_speed_amount = 0
font = font.SysFont(None, 36)
game = True
game_over=False


while game:
    for e in event.get():
        if e.type == QUIT:#how to close
            game = False
        if e.type == KEYDOWN:
            if e.key == K_r and game_over:#change it later
                bowl =You(250, h-70)
                vegs = []
                points = 0
                lives = 3
                v_speed_amount = 0
                game_over = False
            if e.key == K_q:
                game = False
    if not game_over:
        keys= key.get_pressed()
        bowl.update(keys)
        v_speed_amount +=1
        if v_speed_amount%60==0:
            v_type = random.choice(["apple", "banana", "orange"])
            x = random.randint(20, w - 60)
            vegs.append(Vegetables(x, 0, v_type, veg_images))

        bowl_rect = bowl.get_rect()
        for v in vegs[:]:
            v.update()
            if bowl_rect.colliderect(v.get_rect()):
                vegs.remove(v)
                points+=1
            if v.y>h :
                vegs.remove(v)
                lives-=1
                if lives <=0:
                    game_over=True
    screen.fill((15, 91, 115))
    for v in vegs:
        v.appear(screen)
    bowl.appear(screen)
    score_txt = font.render(f"Score: {points}", True, (225, 225,225))
    lives_txt = font.render(f"Lives: {lives}", True, (225, 100,100))
    screen.blit(score_txt, (10, 10))
    screen.blit(lives_txt, (w - 120, 10))
    if game_over:
        overlay = Surface((w, h))
        overlay.set_alpha(200)
        ovwrlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))

        game_over_txt = font.render(f"GAME OVER! Score: {points}", True, (225, 100,100))
        restart_txt = font.render("Press R to restart or Q to quit", True, (225, 225,225))
        screen.blit(game_over_txt (w//2 - 150, 150))
        screen.blit(resart_txt, (w//2-230, 250))
        
    display.update()
    clock.tick(FPS)