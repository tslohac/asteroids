# That greeting comes from importing pygame. Hide it by setting an env var before pygame is imported.
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *




def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
