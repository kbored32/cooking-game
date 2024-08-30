import pygame

pygame.init()
screen = pygame.display.set_mode((960, 480))
clock = pygame.time.Clock()
running = True

pygame.display.set_caption("Kanad Cooking!")  # Sets window title
programIcon = pygame.image.load('./sprites/icon.png')  # Sets window icon
pygame.display.set_icon(programIcon)

coffee_image = pygame.image.load("./sprites/coffee.jpg")
instant_ramen_image = pygame.image.load("./sprites/instant_ramen.jpg")
omelette_image = pygame.image.load("./sprites/omelette.jpg")
pancake_image = pygame.image.load("./sprites/pancake.jpg")

play_btn = pygame.image.load("sprites/play_btn.png")

pygame.font.init()
comic_sans = pygame.font.SysFont('Comic Sans MS', 30)

text_surface = comic_sans.render("", True, (0, 0, 0))

main_screen = True

while running:
    screen.fill("white")

    class Recipe:
        def __init__(self, name, filename):
            self.name = name
            self.filename = filename

    if main_screen:
        coffee_recipe = Recipe("Coffee", "recipe_scripts/coffee.py")
        instant_ramen_recipe = Recipe("Instant Ramen", "recipe_scripts/instant_ramen.py")
        omelette_recipe = Recipe("Omelette", "recipe_scripts/omelette.py")
        pancake_recipe = Recipe("Pancake", "recipe_scripts/pancake.py")

        coffee_screen = screen.blit(coffee_image, (50, 75))
        instant_ramen_screen = screen.blit(instant_ramen_image, (50, 300))
        omelette_screen = screen.blit(omelette_image, (300, 75))
        pancake_screen = screen.blit(pancake_image, (300, 300))

        play_btn_screen = screen.blit(play_btn, (650, 300))
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
                main_screen = False

    clock.tick(10)

pygame.quit()
quit()
