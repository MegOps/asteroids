# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from circleshape import *

def main():
    updatable  = pygame.sprite.Group()
    drawable   = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    game_state = True

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x,y,PLAYER_RADIUS)

    while (game_state == True):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for item in updatable:
            item.update(dt)
        

        screen.fill("black")  # Clear the screen before drawing
        for item in drawable:
            player.draw(screen)   # Draw the player on the screen

        pygame.display.flip() # Update the screen after drawing
        dt = clock.tick(60)/1000
        




if __name__ == "__main__":
    main()