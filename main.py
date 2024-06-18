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
logo_img = pygame.image.load(
    "Bijlagen voor de kandidaat/Bijlage 2 - Logos/Bijlage 2 - Logo zonder text.png"
)

logo_width = 100  # breedte in pixels
logo_height = 100  # hoogte in pixels
logo_img = pygame.transform.scale(logo_img, (logo_width, logo_height))


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
                if (
                    button_x <= mouse_x <= button_x + start_button_img.get_width()
                    and button_y <= mouse_y <= button_y + start_button_img.get_height()
                ):
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

        logo_x = screen_width - logo_img.get_width() - 10  # 10 pixels van de rand
        logo_y = 10  # 10 pixels van de bovenkant
        screen.blit(logo_img, (logo_x, logo_y))

        pygame.display.update()

    return True


def game_loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(background, (0, 0))

        pygame.display.update()

    pygame.quit()


def main():
    if main_menu():
        game_loop()


main()
