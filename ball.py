import pygame
import numpy as np

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pos = np.array([x, y], dtype=float)
        self.vx = 0.0
        self.vy = 0.0
        self.vel = np.array([self.vx, self.vy], dtype=float)
        self.acc = np.array([0.0, 0.0], dtype=float) 

    def draw(self, screen, radius=20):
        pygame.draw.circle(screen, "red", (self.pos[0], self.pos[1]), radius)

    def update(self, dt):
        self.vel += self.acc * dt
        self.pos += self.vel * dt