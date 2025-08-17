# That greeting comes from importing pygame. Hide it by setting an env var before pygame is imported.
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    game_time = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))

        pygame.display.flip()
        game_time.tick(60)
        dt = game_time.tick(60)/1000

if __name__ == "__main__":
    main()
