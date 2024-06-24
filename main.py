import pygame
import random
from settings import screen, background, fruit_basket, healthy_fruit_images, rotten_fruit_images, bomb_img, basket_x, basket_y, basket_speed, score, basket_width, fruit_width, fruit_height, basket_height
from menu import main_menu, end_menu

def game_loop():
    running = True
    global basket_x
    global score
    score = 0
    fruit_speed = 3  # Start snelheid van vallend fruit
    difficulty_timer = 0  # Timer om de moeilijkheid te verhogen
    bomb_chance = 0.1  # Start kans op een bom

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

        difficulty_timer += 1
        if difficulty_timer % 600 == 0:  # Elke 10 seconden (aangenomen dat de FPS 60 is)
            fruit_speed += 0.5  # Verhoog de snelheid van vallend fruit
            next_object_time = max(20, next_object_time - 10)  # Verhoog de frequentie van nieuwe objecten
            bomb_chance = min(0.5, bomb_chance + 0.05)  # Verhoog de kans op bommen

        # Nieuwe objecten toevoegen (fruit of bom)
        next_object_time -= 1
        if next_object_time <= 0 and len(objects) < 10:
            object_x = random.randint(0, screen.get_width() - fruit_width)
            if random.random() < bomb_chance:  # Kans op een bom
                object_img = bomb_img
            else:
                if random.random() < 0.5:  # Gelijke kans op gezond of rot fruit
                    object_img = random.choice(healthy_fruit_images)
                else:
                    object_img = random.choice(rotten_fruit_images)
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
            
            # Definieer de nauwkeurigere hitbox van de fruitmand
            hitbox_width = basket_width * 0.8  # 80% van de breedte
            hitbox_height = basket_height * 0.5  #  50% van de hoogte
            hitbox_x = basket_x + (basket_width - hitbox_width) / 2  # centreren in de fruitmand
            hitbox_y = basket_y + (basket_height - hitbox_height) / 2  # centreren in de fruitmand
            
            basket_rect = pygame.Rect(hitbox_x, hitbox_y, hitbox_width, hitbox_height)
            # Definieer de hitbox van het vallende object
            obj_rect = pygame.Rect(obj["x"], obj["y"], fruit_width, fruit_height)
            
            # Controleer op collision
            if basket_rect.colliderect(obj_rect):
                if obj["img"] == bomb_img:
                    running = False  # beëindig het spel als een bom wordt gevangen
                elif obj["img"] in rotten_fruit_images:  # rot fruit
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
