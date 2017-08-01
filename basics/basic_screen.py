import pygame
pygame.init()

screen = pygame.display.set_mode((640,480)) # Set screen size of pygame window
background = pygame.Surface(screen.get_size())  # Create empty pygame surface
background.fill((255,255,255))     # Fill the background white color (red,green,blue)
background = background.convert()  # Convert Surface to make blitting faster

screen.blit(background, (0, 0))

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        mainloop = False # pygame window closed by user
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            mainloop = False # user pressed ESC
