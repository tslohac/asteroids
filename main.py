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
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroidfield = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = (asteroidfield, updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    p1 = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroidfield_obj = AsteroidField()
    print("updatable:", len(updatable), "drawable:", len(drawable),
      "asteroids:", len(asteroids), "field:", len(asteroidfield))
# Expect: updatable >= 2 (player + field), drawable >= 1 (player)
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

        for ast in asteroids:
            if ast.check_collision(p1):
                print("Game over!")
                pygame.quit()
                sys.exit()

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        # game_time.tick(60)
        

if __name__ == "__main__":
    main()
