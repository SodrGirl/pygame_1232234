from pygame import *
import random

# ===== ИНИЦИАЛИЗАЦИЯ =====
init()

# ===== КОНСТАНТЫ =====
WIDTH = 600
HEIGHT = 400
FPS = 60

# ===== КЛАСС КОРЗИНЫ =====
class Basket:
    def __init__(self, x, y):
        self.image = image.load("basket.png")
        self.image = transform.scale(self.image, (80, 60))
        self.x = x
        self.y = y
        self.speed = 6
    
    def update(self, keys):
        if keys[K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[K_RIGHT] and self.x < WIDTH - 80:
            self.x += self.speed
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
    
    def get_rect(self):
        return self.image.get_rect(topleft=(self.x, self.y))


# ===== КЛАСС ФРУКТА =====
class Fruit:
    def __init__(self, x, y, fruit_type, fruit_images):
        self.image = fruit_images[fruit_type]
        self.x = x
        self.y = y
        self.speed = 4
    
    def update(self):
        self.y += self.speed
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
    
    def get_rect(self):
        return self.image.get_rect(topleft=(self.x, self.y))


# ===== ЗАГРУЗКА КАРТИНКИ =====
def load_image(path, size):
    img = image.load(path)
    return transform.scale(img, size)


# ===== НАСТРОЙКА ЭКРАНА =====
screen = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Лови фрукты!")
clock = time.Clock()

# ===== ЗАГРУЗКА КАРТИНОК =====
fruit_images = {
    "apple": load_image("apple.png", (40, 40)),
    "banana": load_image("banana.png", (40, 40)),
    "orange": load_image("orange.png", (40, 40)),
}

# ===== ИГРОВЫЕ ПЕРЕМЕННЫЕ =====
basket = Basket(250, HEIGHT - 70)
fruits = []
score = 0
lives = 3
frame_count = 0
game_over = False
running = True

# ===== ШРИФТ =====
font = font.SysFont(None, 36)


# ===== ГЛАВНЫЙ ИГРОВОЙ ЦИКЛ =====
while running:
    
    # ----- 1. СОБЫТИЯ -----
    for e in event.get():
        if e.type == QUIT:
            running = False
        
        if e.type == KEYDOWN:
            if e.key == K_r and game_over:
                basket = Basket(250, HEIGHT - 70)
                fruits = []
                score = 0
                lives = 3
                frame_count = 0
                game_over = False
            
            if e.key == K_q:
                running = False
    
    # ----- 2. ЛОГИКА -----
    if not game_over:
        keys = key.get_pressed()
        basket.update(keys)
        
        for fruit in fruits[:]:
            fruit.update()
        
        frame_count += 1
        if frame_count % 60 == 0:
            fruit_type = random.choice(["apple", "banana", "orange"])
            x = random.randint(20, WIDTH - 60)
            fruits.append(Fruit(x, 0, fruit_type, fruit_images))
        
        basket_rect = basket.get_rect()
        for fruit in fruits[:]:
            if basket_rect.colliderect(fruit.get_rect()):
                fruits.remove(fruit)
                score += 1
        
        for fruit in fruits[:]:
            if fruit.y > HEIGHT:
                fruits.remove(fruit)
                lives -= 1
                if lives <= 0:
                    game_over = True
    
    # ----- 3. ОТРИСОВКА -----
    screen.fill((30, 30, 60))
    
    for fruit in fruits:
        fruit.draw(screen)
    
    basket.draw(screen)
    
    score_text = font.render(f"Счёт: {score}", True, (255, 255, 255))
    lives_text = font.render(f"Жизни: {lives}", True, (255, 100, 100))
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (WIDTH - 120, 10))
    
    if game_over:
        overlay = Surface((WIDTH, HEIGHT))
        overlay.set_alpha(200)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))
        
        game_over_text = font.render(f"GAME OVER! Счёт: {score}", True, (255, 100, 100))
        restart_text = font.render("Нажми R для рестарта или Q для выхода", True, (255, 255, 255))
        screen.blit(game_over_text, (WIDTH//2 - 150, 150))
        screen.blit(restart_text, (WIDTH//2 - 230, 250))
    
    display.flip()
    clock.tick(FPS)

# ===== ВЫХОД =====
quit()