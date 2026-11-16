from pygame import*
init()
WIDTH = 500
HEIGHT = 600
screen = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Кликер")
clock = time.Clock()
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 220, 0)
ORANGE = (255, 150, 50)
GREEN = (0, 200, 0)
GRAY = (150, 150, 150)
font_big = font.Font(None, 64)
font_med = font.Font(None, 48)
font_small = font.Font(None, 36)
coins = 0
click_power = 1
upgrade_price = 10

run = True

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == MOUSEBUTTONDOWN:
            mx, my = mouse.get_pos()
            if 175 < mx < 325 and 150 < my < 300:
                coins += click_power
            if 150 < mx < 350 and 420 < my < 480:
                if coins >= upgrade_price:
                    coins -= upgrade_price
                    click_power += 1
                    upgrade_price = int(upgrade_price * 1.6)
    screen.fill(WHITE)
    draw.circle(screen, YELLOW, (250, 225), 75)
    draw.circle(screen, ORANGE, (250, 225), 75, 5)
    coin_text = font_big.render(str(coins), True, ORANGE)
    text_rect = coin_text.get_rect(center=(250, 225))
    screen.blit(coin_text, text_rect)
    power_text = font_med.render(f"Сила: {click_power}", True, BLACK)
    power_rect = power_text.get_rect(center=(250, 360))
    screen.blit(power_text, power_rect)
    draw.rect(screen, GREEN, (150, 420, 200, 60))
    draw.rect(screen, BLACK, (150, 420, 200, 60), 3)
    upgrade_text = font_small.render("Клик +1", True, BLACK)
    upgrade_rect = upgrade_text.get_rect(center=(250, 440))
    screen.blit(upgrade_text, upgrade_rect)
    price_text = font_small.render(f"Цена: {upgrade_price}", True, BLACK)
    price_rect = price_text.get_rect(center=(250, 468))
    screen.blit(price_text, price_rect)
    if coins < upgrade_price:
        overlay = Surface((200, 60))
        overlay.set_alpha(150)
        overlay.fill(GRAY)
        screen.blit(overlay, (150, 420))
        screen.blit(upgrade_text, upgrade_rect)
        screen.blit(price_text, price_rect)
    display.update()
    clock.tick(FPS)

