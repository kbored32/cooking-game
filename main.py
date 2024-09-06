import pygame

pygame.init()
screen = pygame.display.set_mode((960, 480))
clock = pygame.time.Clock()
running = True

pygame.display.set_caption("Kanade Cooking!")
programIcon = pygame.image.load('./sprites/icon.png')
pygame.display.set_icon(programIcon)

coffee_image = pygame.image.load("./sprites/coffee.jpg")
instant_ramen_image = pygame.image.load("./sprites/instant_ramen.jpg")
omelette_image = pygame.image.load("./sprites/omelette.jpg")
pancake_image = pygame.image.load("./sprites/pancake.jpg")

play_btn = pygame.transform.scale(pygame.image.load("sprites/play_btn.png"), (200, 100))

pygame.font.init()
comic_sans = pygame.font.SysFont('Comic Sans MS', 30)

text_surface = comic_sans.render("", True, (0, 0, 0))

main_screen = True


def debug(msg):
    print(f"[DEBUG LOGGER] - {msg}")


has_run = False

while running:
    screen.fill("white")

    class Recipe:
        def __init__(self, name, filename):
            self.name = name
            self.filename = filename


    coffee_recipe = Recipe("Coffee", "recipe_scripts/coffee.py")
    instant_ramen_recipe = Recipe("Instant Ramen", "recipe_scripts/instant_ramen.py")
    omelette_recipe = Recipe("Omelette", "recipe_scripts/omelette.py")
    pancake_recipe = Recipe("Pancake", "recipe_scripts/pancake.py")

    if not has_run:
        text_surface = comic_sans.render(coffee_recipe.name, True, (0, 0, 0))
        has_run = True

    if main_screen:
        coffee_screen = screen.blit(coffee_image, (50, 75))
        instant_ramen_screen = screen.blit(instant_ramen_image, (50, 300))
        omelette_screen = screen.blit(omelette_image, (300, 75))
        pancake_screen = screen.blit(pancake_image, (300, 300))

        play_btn_screen = screen.blit(play_btn, (600, 200))
        screen.blit(text_surface, (630, 120))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Image button detection
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if coffee_screen.collidepoint(mouse_x, mouse_y):
                recipe = 0
                text_surface = comic_sans.render(coffee_recipe.name, True, (0, 0, 0))
            if instant_ramen_screen.collidepoint(mouse_x, mouse_y):
                recipe = 1
                text_surface = comic_sans.render(instant_ramen_recipe.name, True, (0, 0, 0))
            if omelette_screen.collidepoint(mouse_x, mouse_y):
                recipe = 2
                text_surface = comic_sans.render(omelette_recipe.name, True, (0, 0, 0))
            if pancake_screen.collidepoint(mouse_x, mouse_y):
                recipe = 3
                text_surface = comic_sans.render(pancake_recipe.name, True, (0, 0, 0))
            if play_btn_screen.collidepoint(mouse_x, mouse_y):
                try:
                    recipe
                except NameError:
                    recipe = 0
                else:
                    recipe = recipe
                debug(f"Game starting : Recipe {recipe}")
                main_screen = False

    clock.tick(60)

pygame.quit()
quit()
