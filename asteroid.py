import pygame
from circleshape import CircleShape
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        center = self.position.x, self.position.y
        return pygame.draw.circle(screen, (255,255,255), center, self.radius, 2)
    

    def update(self, dt):
        # sub-classes must override
        self.position += (self.velocity * dt)


    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20, 50)

        v1 = self.velocity.rotate(angle) * 1.2
        v2 = self.velocity.rotate(-angle) * 1.2

        new_radius = self.radius - ASTEROID_MIN_RADIUS


        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = v1
        a2.velocity = v2
