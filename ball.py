import pygame
import numpy as np

class Ball:
    def __init__(self):
        self.pos = np.array([0, 0], dtype=float)
        self.vx = 0.0
        self.vy = 0.0
        self.vel = np.array([self.vx, self.vy], dtype=float)
        self.acc = np.array([0.0, 0.0], dtype=float) 
        self.radius = 20

    def draw(self, screen):
        pygame.draw.circle(screen, "red", (self.pos[0], self.pos[1]), self.radius)

    def update(self, dt):
        self.vel += self.acc * dt
        self.pos += self.vel * dt