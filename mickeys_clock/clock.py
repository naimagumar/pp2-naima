
import pygame
import math
from datetime import datetime


def create_hand(length, color):
    hand = pygame.Surface((length, 50), pygame.SRCALPHA)

    # Draw the Mickey-style glove
    pygame.draw.rect(hand, color, (0, 17, 35, 16), border_radius=5)
    pygame.draw.ellipse(hand, color, (25, 10, 45, 30))
    pygame.draw.ellipse(hand, color, (55, 5, length - 50, 16))
    pygame.draw.ellipse(hand, color, (48, 23, 25, 17))
    pygame.draw.ellipse(hand, color, (38, 5, 22, 17))

    # Black outline
    pygame.draw.ellipse(hand, (0, 0, 0), (25, 10, 45, 30), 2)
    pygame.draw.ellipse(hand, (0, 0, 0), (55, 5, length - 50, 16), 2)

    return hand


def draw_rotated_hand(screen, hand, angle, center):
    rotated = pygame.transform.rotate(hand, angle)
    rect = rotated.get_rect()

    radians = math.radians(angle)
    offset_x = -hand.get_width() / 2 * math.cos(radians)
    offset_y = hand.get_width() / 2 * math.sin(radians)

    rect.center = (
        center[0] - offset_x,
        center[1] - offset_y
    )

    screen.blit(rotated, rect)


def draw_clock(screen, font):
    center = (400, 300)

    # Clock face
    pygame.draw.circle(screen, (240, 240, 240), center, 220)
    pygame.draw.circle(screen, (0, 0, 0), center, 220, 4)

    # Clock numbers
    for i in range(12):
        angle = math.radians(i * 30 - 90)
        x = center[0] + 180 * math.cos(angle)
        y = center[1] + 180 * math.sin(angle)
        pygame.draw.circle(screen, (0, 0, 0), (int(x), int(y)), 4)

    # Get current system time
    now = datetime.now()
    minutes = now.minute
    seconds = now.second

    # Calculate angles
    minute_angle = 90 - (minutes * 6 + seconds * 0.1)
    second_angle = 90 - seconds * 6

    # Create Mickey hands
    minute_hand = create_hand(150, (255, 255, 255))
    second_hand = create_hand(110, (220, 0, 0))

    # Draw hands
    draw_rotated_hand(screen, minute_hand, minute_angle, center)
    draw_rotated_hand(screen, second_hand, second_angle, center)

    # Center circle
    pygame.draw.circle(screen, (0, 0, 0), center, 10)

    # Display digital time
    time_text = f"{minutes:02d}:{seconds:02d}"
    text = font.render(time_text, True, (0, 0, 0))
    screen.blit(text, (345, 540))
