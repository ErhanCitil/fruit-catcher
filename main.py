import pygame
import random

# Initialiseer Pygame
pygame.init()

# Scherminstellingen
screen_width = 1920
screen_height = 1050
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Fruit Catcher")

# Afbeeldingen
background = pygame.image.load("Bijlagen voor de kandidaat/background_image.jpeg")
start_button_img = pygame.image.load("Bijlagen voor de kandidaat/play_button.png")
logo_img = pygame.image.load("Bijlagen voor de kandidaat/Bijlage 2 - Logos/Bijlage 2 - Logo zonder text.png")
fruit_basket = pygame.image.load("Bijlagen voor de kandidaat/fruit_basket.png")

# Fruit afbeeldingen
apple_img = pygame.image.load("Bijlagen voor de kandidaat/Fruits/apple.png")
cherry_img = pygame.image.load("Bijlagen voor de kandidaat/Fruits/cherry.png")
pear_img = pygame.image.load("Bijlagen voor de kandidaat/Fruits/pear.png")

# Rotte fruitstukken
half_apple_img = pygame.image.load("Bijlagen voor de kandidaat/Fruits/appleHalf.png")
half_lemon_img = pygame.image.load("Bijlagen voor de kandidaat/Fruits/lemonHalf.png")
half_pear_img = pygame.image.load("Bijlagen voor de kandidaat/Fruits/pearHalf.png")

# Fruit afbeeldingen instellingen
fruit_width = 100
fruit_height = 100

# Schaal de fruitafbeeldingen
scaled_fruit_images = []
for img in [apple_img, cherry_img, pear_img, half_apple_img, half_lemon_img, half_pear_img]:
    scaled_img = pygame.transform.scale(img, (fruit_width, fruit_height))
    scaled_fruit_images.append(scaled_img)

# Snelheid van vallend fruit
fruit_speed = 3

# Hier zorgen we er voor dat de logo 100 bij 100 pixels is
logo_width = 100 
logo_height = 100 
logo_img = pygame.transform.scale(logo_img, (logo_width, logo_height))

# Hier zetten we de instellingen voor de fruitmand
basket_width = fruit_basket.get_width()
basket_height = fruit_basket.get_height()
basket_x = screen_width // 2 - basket_width // 2
basket_y = screen_height - basket_height - 10
basket_speed = 4.5

def main_menu():
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                button_x = screen_width // 2 - start_button_img.get_width() // 2
                button_y = screen_height // 2 - start_button_img.get_height() // 2
                if (button_x <= mouse_x <= button_x + start_button_img.get_width()
                    and button_y <= mouse_y <= button_y + start_button_img.get_height()):
                    menu = False

        screen.blit(background, (0, 0))

        title = pygame.font.SysFont(None, 55).render(
            "Best Education B.V.", True, (0, 0, 0)
        )
        paragraph = pygame.font.SysFont(None, 30).render(
            "Wij lanceren je de toekomst in!", True, (0, 0, 0)
        )
        screen.blit(
            title, (screen_width // 2 - title.get_width() // 2, screen_height // 3)
        )
        screen.blit(
            paragraph,
            (screen_width // 2 - paragraph.get_width() // 2, screen_height // 3 + 50),
        )

        button_x = screen_width // 2 - start_button_img.get_width() // 2
        button_y = screen_height // 2 - start_button_img.get_height() // 2
        screen.blit(start_button_img, (button_x, button_y))

        logo_x = screen_width - logo_img.get_width() - 10
        logo_y = 10
        screen.blit(logo_img, (logo_x, logo_y))

        pygame.display.update()

    return True

def game_loop():
    running = True
    global basket_x

    # Lijst van fruitstukken
    fruits = []

    # Bepaalt na hoeveel frames er een nieuw fruit wordt neergevallen
    next_fruit_time = random.randint(60, 120)

    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and basket_x > 0:
            basket_x -= basket_speed
        if keys[pygame.K_RIGHT] and basket_x < screen_width - basket_width:
            basket_x += basket_speed

        # Nieuwe fruitstukken toevoegen
        next_fruit_time -= 1
        if next_fruit_time <= 0 and len(fruits) < 5: 
            fruit_x = random.randint(0, screen_width - fruit_width) 
            fruit_img = random.choice(scaled_fruit_images)  
            fruits.append({"img": fruit_img, "x": fruit_x, "y": -fruit_height})  
            next_fruit_time = random.randint(60, 120)  # reset de timer

        # Beweeg fruitstukken naar beneden
        for fruit in fruits:
            fruit["y"] += fruit_speed

        # Verwijder fruitstukken die onderaan het scherm zijn
        fruits = [fruit for fruit in fruits if fruit["y"] < screen_height]

        # Tekent de achtergrond nadat je op play button hebt geklikt en de fruitmand op het scherm
        screen.blit(background, (0, 0))
        screen.blit(fruit_basket, (basket_x, basket_y))

        # Teken fruitstukken
        for fruit in fruits:
            screen.blit(fruit["img"], (fruit["x"], fruit["y"]))

        pygame.display.update()

        clock.tick(60)

    pygame.quit()

def main():
    if main_menu():
        game_loop()

main()
