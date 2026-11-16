class Basket:
    def __init__(self, x, y):
        self.image = image.load("basket.png").convert_alpha()
        self.image = transform.scale(self.image, (80, 60))
        self.x = x
        self.y = y
        self.speed = 6
    def update(self, keys):
        if keys[K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[K_RIGHT] and self.x < width - 80:
            self.x += self.speed
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
    def get_rect(self):
        return self.image.get_rect(topleft=(self.x, self.y))
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
def load_image(path, size):
    img = image.load(path).convert_alpha()
    return transform.scale(img, size)