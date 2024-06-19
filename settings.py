import pygame

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

score = 0
