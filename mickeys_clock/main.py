
import pygame
from clock import draw_clock

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mickey's Clock")

font = pygame.font.SysFont("Arial", 40)

clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    draw_clock(screen, font)

    pygame.display.update()

    clock.tick(60)

pygame.quit()
