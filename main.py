import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
from sim import Sim
from ball import Ball

def add_ball_to_sim(sim, ball_count, m_x, m_y):
    ball_count[0] += 1
    for _ in range(ball_count[0]):
        ball = Ball()
        ball.pos[0], ball.pos[1] = m_x, m_y
        sim.add_ball(ball)

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption("bounce")
    clock = pygame.time.Clock()
    
    ball_count = [0]

    sim = Sim()
    
    running = True

    while running:
        
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    running = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                add_ball_to_sim(sim, ball_count, m_x, m_y)

        dt = clock.tick(60) / 1000.0 * 3.5
        
        sim.update(dt)
        
        screen.fill("black")

        for ball in sim.balls:
            ball.draw(screen)
        
        pygame.display.flip()
    
    pygame.quit()