import pygame
import random
from settings import screen, background, fruit_basket, scaled_fruit_images, fruit_speed, basket_x, basket_y, basket_speed, score, basket_width, fruit_width, fruit_height
from menu import main_menu

def game_loop():
    running = True
    global basket_x
    global score

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
        if keys[pygame.K_RIGHT] and basket_x < screen.get_width() - basket_width:
            basket_x += basket_speed

        # Nieuwe fruitstukken toevoegen
        next_fruit_time -= 1
        if next_fruit_time <= 0 and len(fruits) < 5: 
            fruit_x = random.randint(0, screen.get_width() - fruit_width) 
            fruit_img = random.choice(scaled_fruit_images)  
            fruits.append({"img": fruit_img, "x": fruit_x, "y": -fruit_height})  
            next_fruit_time = random.randint(60, 120)  # reset de timer

        # Beweeg fruitstukken naar beneden
        for fruit in fruits:
            fruit["y"] += fruit_speed

        # Verwijder fruitstukken die onderaan het scherm zijn of in de mand vallen
        new_fruits = []
        for fruit in fruits:
            if fruit["y"] >= screen.get_height():
                continue  # fruit is onderaan het scherm
            if fruit["y"] + fruit_height >= basket_y:  # controleer of het fruit de mand raakt
                if basket_x < fruit["x"] + fruit_width and basket_x + basket_width > fruit["x"]:
                    # fruit is in de mand gevallen
                    if fruit["img"] not in [scaled_fruit_images[3], scaled_fruit_images[4], scaled_fruit_images[5]]:  # geen rot fruit
                        score += 10
                    continue
            new_fruits.append(fruit)
        fruits = new_fruits

        # Tekent de achtergrond nadat je op play button hebt geklikt en de fruitmand op het scherm
        screen.blit(background, (0, 0))
        screen.blit(fruit_basket, (basket_x, basket_y))

        # Teken fruitstukken
        for fruit in fruits:
            screen.blit(fruit["img"], (fruit["x"], fruit["y"]))

        # Teken de score
        score_text = pygame.font.SysFont(None, 55).render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

        pygame.display.update()

        clock.tick(60)

    pygame.quit()

def main():
    if main_menu():
        game_loop()

main()
