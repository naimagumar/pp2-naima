
import pygame
from pathlib import Path
from player import MusicPlayer



pygame.init()


WIDTH = 700
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")


WHITE = (255, 255, 255)
BLACK = (30, 30, 30)
BLUE = (50, 120, 220)
GRAY = (200, 200, 200)


font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 26)

# Music folder
music_folder = (
    Path(__file__).parent / "music" / "sample_tracks"
)

# Create music player
player = MusicPlayer(music_folder)

# Clock
clock = pygame.time.Clock()

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_p:
                player.play()

            elif event.key == pygame.K_s:
                player.stop()

            elif event.key == pygame.K_n:
                player.next_track()

            elif event.key == pygame.K_b:
                player.previous_track()

            elif event.key == pygame.K_q:
                running = False

    # Background
    screen.fill(WHITE)

    # Title
    title = font.render(
        "MY MUSIC PLAYER", True, BLUE
    )
    screen.blit(title, (220, 40))

    # Current track
    track_text = font.render(
        "Track: " + player.get_track_name(),
        True, BLACK
    )
    screen.blit(track_text, (100, 120))

    # Playback time
    position = player.get_position()
    duration = player.get_duration()

    time_text = small_font.render(
        f"Time: {position} / {int(duration)} seconds",
        True, BLACK
    )
    screen.blit(time_text, (100, 180))

    # Progress bar
    bar_x = 100
    bar_y = 230
    bar_width = 500
    bar_height = 15

    pygame.draw.rect(
        screen, GRAY,
        (bar_x, bar_y, bar_width, bar_height)
    )

    if duration > 0:
        progress = min(position / duration, 1)

        pygame.draw.rect(
            screen, BLUE,
            (bar_x, bar_y,
             int(bar_width * progress), bar_height)
        )

    # Keyboard instructions
    instructions = [
        "P - Play",
        "S - Stop",
        "N - Next",
        "B - Previous",
        "Q - Quit"
    ]

    for i, instruction in enumerate(instructions):
        text = small_font.render(
            instruction, True, BLACK
        )
        screen.blit(text, (100 + i * 110, 300))

    pygame.display.flip()

    clock.tick(30)

# Close application
player.quit()
pygame.quit()
