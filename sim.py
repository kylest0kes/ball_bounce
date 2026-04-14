import pygame

class Sim:
    def __init__(self):
        self.balls = []
        
    def add_ball(self, ball):
        self.balls.append(ball)

    def clear_balls(self):
        self.balls = []