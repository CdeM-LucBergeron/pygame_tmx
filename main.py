import pygame
import pytmx

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Create the game screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TMX Example")
clock = pygame.time.Clock()

# Load the map
tmx_data = pytmx.util_pygame.load_pygame("essaie_map.tmx")

# Get the first layer of the map
layer = tmx_data.layers[0]

# Set up the game variables
running = True
while running:
    # Keep the loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # Check for closing the window
        if event.type == pygame.QUIT:
            running = False

    # Update

    # Draw / render
    screen.fill((0, 0, 0))
    # Draw the layers
    for layer in tmx_data.layers:
        for x, y, gid in layer:
            tile = tmx_data.get_tile_image_by_gid(gid)
            if tile:
                screen.blit(tile, (x * tmx_data.tilewidth, y * tmx_data.tileheight))

    # After drawing everything, flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()