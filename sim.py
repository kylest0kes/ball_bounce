import numpy as np 

class Sim:
    def __init__(self):
        self.balls = []
        self.gravity = 350
        
    def add_ball(self, ball):
        self.balls.append(ball)

    def clear_balls(self):
        self.balls = []

    def calculate_accelerations(self):
        for ball in self.balls:
            ball.acc[1] += self.gravity
            
    
    def update(self, dt):
        self.calculate_accelerations()
        for ball in self.balls:
            ball.vel[1] += ball.acc[1] * dt

            ball.pos[1] += ball.vel[1] * dt

            ball.vel *= 0.995