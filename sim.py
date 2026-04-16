class Sim:
    def __init__(self):
        self.balls = []
        self.gravity = 75 
        self.window_w = 1000
        self.window_h = 1000
        self.dampening = 0.9 
        
    def add_ball(self, ball):
        self.balls.append(ball)

    def clear_balls(self):
        self.balls = []

    def calculate_accelerations(self):
        for ball in self.balls:
            ball.acc[1] += self.gravity
            
    def check_for_border_collisions(self):
        for ball in self.balls:
            if ball.pos[1] + ball.radius >= self.window_h:
                ball.pos[1] = self.window_h - ball.radius

                if abs(ball.vel[1]) > 5.0:
                    ball.vel[1] = -(ball.vel[1]) * self.dampening 
                else:
                    ball.vel[1] = 0
    
    def update(self, dt):
        self.calculate_accelerations()
        for ball in self.balls:
            ball.vel[1] += ball.acc[1] * dt

            ball.pos[1] += ball.vel[1] * dt

        self.check_for_border_collisions()
