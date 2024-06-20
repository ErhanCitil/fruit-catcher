import pygame
import random
from settings import screen, background, fruit_basket, scaled_fruit_images, bomb_img, fruit_speed, basket_x, basket_y, basket_speed, score, basket_width, fruit_width, fruit_height
from menu import main_menu, end_menu

def game_loop():
    running = True
    global basket_x
    global score
    score = 0

    # Lijst van fruitstukken en bommen
    objects = []

    # Bepaalt na hoeveel frames er een nieuw object wordt neergevallen
    next_object_time = random.randint(60, 120)

    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and basket_x > 0:
            basket_x -= basket_speed
        if keys[pygame.K_RIGHT] and basket_x < screen.get_width() - basket_width:
            basket_x += basket_speed

        # Nieuwe objecten toevoegen (fruit of bom)
        next_object_time -= 1
        if next_object_time <= 0 and len(objects) < 5:
            object_x = random.randint(0, screen.get_width() - fruit_width)
            if random.random() < 0.1:  # 10% kans op een bom
                object_img = bomb_img
            else:
                object_img = random.choice(scaled_fruit_images)
            objects.append({"img": object_img, "x": object_x, "y": -fruit_height})
            next_object_time = random.randint(60, 120)  # reset de timer

        # Beweeg objecten naar beneden
        for obj in objects:
            obj["y"] += fruit_speed

        # Verwijder objecten die onderaan het scherm zijn of in de mand vallen
        new_objects = []
        for obj in objects:
            if obj["y"] >= screen.get_height():
                continue  # object is onderaan het scherm
            if obj["y"] + fruit_height >= basket_y:  # controleer of het object de mand raakt
                if basket_x < obj["x"] + fruit_width and basket_x + basket_width > obj["x"]:
                    # object is in de mand gevallen
                    if obj["img"] == bomb_img:
                        running = False 
                    elif obj["img"] in [scaled_fruit_images[3], scaled_fruit_images[4], scaled_fruit_images[5]]: # Min punten voor halve fruitstukken
                        score -= 10
                    else:
                        score += 10
                    continue
            new_objects.append(obj)
        objects = new_objects

        # Tekent de achtergrond nadat je op play button hebt geklikt en de fruitmand op het scherm
        screen.blit(background, (0, 0))
        screen.blit(fruit_basket, (basket_x, basket_y))

        # Teken objecten (fruit en bommen)
        for obj in objects:
            screen.blit(obj["img"], (obj["x"], obj["y"]))

        # Teken de score
        score_text = pygame.font.SysFont(None, 55).render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

        pygame.display.update()

        clock.tick(60)

def main():
    while True:
        if main_menu():
            game_loop()
        if end_menu() == False:
            break
    pygame.quit()  # Sluit Pygame af als we de loop verlaten

main()
