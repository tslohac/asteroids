#main.py module
# 
# 
# # That greeting comes from importing pygame. Hide it by setting an env var before pygame is imported.
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    p1 = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
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
        dt = game_time.tick(60)/1000
        updatable.update(dt)
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        # game_time.tick(60)
        

if __name__ == "__main__":
    main()
