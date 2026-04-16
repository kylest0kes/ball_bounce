class Sim:
    def __init__(self):
        self.balls = []
        self.gravity = 75 
        self.window_w = 1000
        self.window_h = 1000
        self.dampening = 0.9 
        self.is_paused = False
        
    def add_ball(self, ball):
        self.balls.append(ball)

    def clear_balls(self):
        self.balls = []

    def calculate_accelerations(self):
        for ball in self.balls:
            ball.acc[1] += self.gravity
            
    def check_for_border_collisions(self):
        for ball in self.balls:
            # has ball hit the bottom of the window?
            if ball.pos[1] + ball.radius >= self.window_h:
                # clamp ball to bottom of screen
                ball.pos[1] = self.window_h - ball.radius

                # before modifying y velocity, check if the y vel is above a certain threshold
                if abs(ball.vel[1]) > 5.0:
                    # y vel is above threshold so flip y vel and add dampening
                    ball.vel[1] = -(ball.vel[1]) * self.dampening 
                else:
                    # y vel is under threshold, set y vel to 0 to hard settle the ball
                    ball.vel[1] = 0
    
    def update(self, dt):
        self.calculate_accelerations()
        for ball in self.balls:
            ball.vel[1] += ball.acc[1] * dt

            ball.pos[1] += ball.vel[1] * dt

        self.check_for_border_collisions()
