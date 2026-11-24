
import pygame

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 25
        self.speed = 20
        self.color = (255, 0, 0)

    def move(self, key, screen_width, screen_height):
        if key == pygame.K_UP:
            if self.y - self.radius - self.speed >= 0:
                self.y -= self.speed

        elif key == pygame.K_DOWN:
            if self.y + self.radius + self.speed <= screen_height:
                self.y += self.speed

        elif key == pygame.K_LEFT:
            if self.x - self.radius - self.speed >= 0:
                self.x -= self.speed

        elif key == pygame.K_RIGHT:
            if self.x + self.radius + self.speed <= screen_width:
                self.x += self.speed

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            self.color,
            (self.x, self.y),
            self.radius
        )
