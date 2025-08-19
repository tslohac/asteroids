import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        center = self.position.x, self.position.y
        pygame.draw.circle(screen, (255, 255, 255), center, self.radius, 2)