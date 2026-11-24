
import pygame
from ball import Ball

pygame.init()

WIDTH = 600
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball Game")

WHITE = (255, 255, 255)

ball = Ball(WIDTH // 2, HEIGHT // 2)

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            ball.move(event.key, WIDTH, HEIGHT)

    screen.fill(WHITE)

    ball.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
