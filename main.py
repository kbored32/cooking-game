import pygame

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((960, 480))
clock = pygame.time.Clock()
running = True

# Adds an icon image to the window
pygame.display.set_caption("Kanade Cooking!")
programIcon = pygame.image.load('./sprites/icon.png')
pygame.display.set_icon(programIcon)

# Loads necessary sprites
coffee_image = pygame.transform.scale(pygame.image.load("sprites/coffee.png"), (128, 128))
instant_ramen_image = pygame.transform.scale(pygame.image.load("./sprites/instant_ramen.png"), (128, 128))
omelette_image = pygame.transform.scale(pygame.image.load("./sprites/omelette.png"), (128, 128))
pancake_image = pygame.transform.scale(pygame.image.load("./sprites/pancake.jpg"), (128, 128))
play_btn = pygame.transform.scale(pygame.image.load("sprites/play_btn.png"), (200, 100))
bg = pygame.image.load("./sprites/background.png")
sticky_note = pygame.image.load("./sprites/stickynote.png")

coffe_recipe = pygame.image.load("./sprites/coffee_recipe.png")
pancake_recipee = pygame.image.load("./sprites/pancake_recipe.png")
instant_ramen_recipee = pygame.image.load("./sprites/instant_ramen_recipee.png")
omelette_recipee = pygame.image.load("./sprites/omlette recipe.png")

# Initializes the ability to create text using Comic Sans MS
text_surface = pygame.font.SysFont('Comic Sans MS', 30).render("", True, (0, 0, 0))

# Program variables
main_screen = True
game_start = False


def debug(msg):
    print(f"[DEBUG LOGGER] - {msg}")


has_run = False

while running:
    screen.fill("white")
    screen.blit(bg, (0,0))

    class Recipe:
        def __init__(self, name):
            self.name = name


    coffee_recipe = Recipe("Coffee")
    instant_ramen_recipe = Recipe("Instant Ramen")
    omelette_recipe = Recipe("Omelette")
    pancake_recipe = Recipe("Pancake")

    if not has_run:
        text_surface = pygame.font.SysFont('Comic Sans MS', 30).render(coffee_recipe.name, True, (0, 0, 0))
        has_run = True

    if main_screen:
        coffee_screen = screen.blit(coffee_image, (50, 75))
        instant_ramen_screen = screen.blit(instant_ramen_image, (50, 300))
        omelette_screen = screen.blit(omelette_image, (300, 75))
        pancake_screen = screen.blit(pancake_image, (300, 300))

        play_btn_screen = screen.blit(play_btn, (600, 200))
        screen.blit(text_surface, (630, 120))

    if game_start:
        screen.blit(text_surface, (425, 50))

        screen.blit(sticky_note, (700, 60))

        if recipe == 0:
            screen.blit(coffee_image, (25, 25))
            recipe_text = pygame.font.SysFont('Comic Sans MS', 12).render("Coffee recipe:", True, (0, 0, 0))
            screen.blit(coffe_recipe, (725, 100))
        elif recipe == 1:
            screen.blit(instant_ramen_image, (25, 25))
            recipe_text = pygame.font.SysFont('Comic Sans MS', 12).render("Instant Ramen recipe:", True, (0, 0, 0))
            screen.blit(instant_ramen_recipee, (725, 100))
        elif recipe == 2:
            screen.blit(omelette_image, (25, 25))
            recipe_text = pygame.font.SysFont('Comic Sans MS', 12).render("Omelette recipe:", True, (0, 0, 0))
            screen.blit(omelette_recipee, (725, 100))
        elif recipe == 3:
            screen.blit(pancake_image, (25, 25))
            recipe_text = pygame.font.SysFont('Comic Sans MS', 12).render("Pancake recipe:", True, (0, 0, 0))
            screen.blit(pancake_recipee, (725, 100))

        screen.blit(recipe_text, (705, 65))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Image button detection
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if coffee_screen.collidepoint(mouse_x, mouse_y):
                recipe = 0
                text_surface = pygame.font.SysFont('Comic Sans MS', 30).render(coffee_recipe.name, True, (0, 0, 0))
            if instant_ramen_screen.collidepoint(mouse_x, mouse_y):
                recipe = 1
                text_surface = pygame.font.SysFont('Comic Sans MS', 30).render(instant_ramen_recipe.name, True,
                                                                               (0, 0, 0))
            if omelette_screen.collidepoint(mouse_x, mouse_y):
                recipe = 2
                text_surface = pygame.font.SysFont('Comic Sans MS', 30).render(omelette_recipe.name, True, (0, 0, 0))
            if pancake_screen.collidepoint(mouse_x, mouse_y):
                recipe = 3
                text_surface = pygame.font.SysFont('Comic Sans MS', 30).render(pancake_recipe.name, True, (0, 0, 0))
            if play_btn_screen.collidepoint(mouse_x, mouse_y):
                try:
                    recipe
                except NameError:
                    recipe = 0
                debug(f"Game starting : Recipe {recipe}")
                main_screen = False
                game_start = True

    clock.tick(60)

pygame.quit()
quit()
