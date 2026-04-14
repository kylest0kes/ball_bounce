import pygame

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen, radius=20):
        pygame.draw.circle(screen, "red", (self.x, self.y), radius)