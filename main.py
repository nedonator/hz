import pygame

from player import Player
import game_map

# Initialize the pygame library
pygame.init()

# Create a game window
screen = pygame.display.set_mode((800, 600), vsync=1)

# Set the title of the window
pygame.display.set_caption("2D Graphics Application")
clock = pygame.time.Clock()

# Main game loop
running = True
fps = 30

player = Player()

while running:
    time = clock.get_time()
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.KEYUP or event.type == pygame.KEYDOWN:
            print('event: ' + str(event))
            print(event.__dict__)
            player.handle(event.type, event.scancode)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.QUIT:
            running = False
    
    player.update(time)

    # Clear the screen
    screen.fill((255, 255, 255))

    f1 = pygame.font.Font(None, 36)
    text1 = f1.render('Hello Привет', True, (180, 0, 0))
    screen.blit(text1, (10 - player.x, 50 - player.y))
    
    game_map.render(screen, player)
    # Draw a rectangle
    
    
    # Update the display
    pygame.display.flip()

    clock.tick(fps)

# Quit the game
pygame.quit()
