
import pygame
import sys
from datetime import datetime
from tools import DrawingTools

pygame.init()

# Window settings
WIDTH = 1000
HEIGHT = 700
TOOLBAR_HEIGHT = 100

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Application")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (210, 210, 210)
DARK_GRAY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0, 180, 0)
BLUE = (0, 100, 255)
YELLOW = (255, 220, 0)
PINK = (255, 100, 180)
PURPLE = (150, 50, 200)

# Fonts
font = pygame.font.SysFont("Arial", 20)
small_font = pygame.font.SysFont("Arial", 16)

# Canvas
canvas = pygame.Surface((WIDTH, HEIGHT - TOOLBAR_HEIGHT))
canvas.fill(WHITE)

tools = DrawingTools()

current_tool = "Pencil"
drawing = False
start_pos = None
last_pos = None

# Text tool variables
text_active = False
text_position = None
text_content = ""

text_font = pygame.font.SysFont("Arial", 24)

# Toolbar buttons
tool_buttons = [
    ("Pencil", pygame.Rect(10, 10, 85, 30)),
    ("Line", pygame.Rect(105, 10, 85, 30)),
    ("Rectangle", pygame.Rect(200, 10, 100, 30)),
    ("Circle", pygame.Rect(310, 10, 85, 30)),
    ("Square", pygame.Rect(405, 10, 85, 30)),
    ("Triangle", pygame.Rect(500, 10, 90, 30)),
    ("Equilateral", pygame.Rect(600, 10, 105, 30)),
    ("Rhombus", pygame.Rect(715, 10, 90, 30)),
    ("Eraser", pygame.Rect(815, 10, 80, 30)),
    ("Fill", pygame.Rect(905, 10, 80, 30)),
    ("Text", pygame.Rect(10, 50, 80, 30))
]

# Color buttons
color_buttons = [
    (BLACK, pygame.Rect(110, 50, 25, 25)),
    (RED, pygame.Rect(145, 50, 25, 25)),
    (GREEN, pygame.Rect(180, 50, 25, 25)),
    (BLUE, pygame.Rect(215, 50, 25, 25)),
    (YELLOW, pygame.Rect(250, 50, 25, 25)),
    (PINK, pygame.Rect(285, 50, 25, 25)),
    (PURPLE, pygame.Rect(320, 50, 25, 25))
]

brush_buttons = [
    (2, pygame.Rect(370, 50, 45, 25)),
    (5, pygame.Rect(420, 50, 45, 25)),
    (10, pygame.Rect(470, 50, 45, 25))
]

clock = pygame.time.Clock()
running = True


def draw_toolbar():
    pygame.draw.rect(screen, GRAY, (0, 0, WIDTH, TOOLBAR_HEIGHT))

    for name, rect in tool_buttons:
        color = BLUE if current_tool == name else WHITE
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, DARK_GRAY, rect, 1)

        label = small_font.render(name, True, BLACK)
        screen.blit(label, label.get_rect(center=rect.center))

    for color, rect in color_buttons:
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, BLACK, rect, 1)

        if tools.color == color:
            pygame.draw.rect(screen, BLUE, rect, 3)

    for size, rect in brush_buttons:
        color = BLUE if tools.brush_size == size else WHITE
        pygame.draw.rect(screen, color, rect)
        pygame.draw.rect(screen, BLACK, rect, 1)

        label = small_font.render(str(size), True, BLACK)
        screen.blit(label, label.get_rect(center=rect.center))

    info = small_font.render(
        "Brush: 1=2px  2=5px  3=10px | Ctrl+S: Save",
        True,
        BLACK
    )
    screen.blit(info, (550, 55))


def draw_preview():
    if not drawing or start_pos is None:
        return

    mouse_pos = pygame.mouse.get_pos()

    if mouse_pos[1] < TOOLBAR_HEIGHT:
        return

    canvas_end = (mouse_pos[0], mouse_pos[1] - TOOLBAR_HEIGHT)

    preview_color = tools.color

    if current_tool == "Line":
        pygame.draw.line(
            screen,
            preview_color,
            (start_pos[0], start_pos[1] + TOOLBAR_HEIGHT),
            mouse_pos,
            tools.brush_size
        )

    elif current_tool == "Rectangle":
        rect = pygame.Rect(start_pos, (
            canvas_end[0] - start_pos[0],
            canvas_end[1] - start_pos[1]
        ))
        rect.normalize()

        if rect.width > 0 and rect.height > 0:
            pygame.draw.rect(
                screen,
                preview_color,
                (rect.x, rect.y + TOOLBAR_HEIGHT,
                 rect.width, rect.height),
                tools.brush_size
            )

    elif current_tool == "Circle":
        radius = int(
            ((canvas_end[0] - start_pos[0]) ** 2 +
             (canvas_end[1] - start_pos[1]) ** 2) ** 0.5
        )

        pygame.draw.circle(
            screen,
            preview_color,
            (start_pos[0], start_pos[1] + TOOLBAR_HEIGHT),
            radius,
            tools.brush_size
        )


while running:

    # Draw canvas and toolbar
    screen.fill(WHITE)
    screen.blit(canvas, (0, TOOLBAR_HEIGHT))
    draw_toolbar()

    # Text preview
    if text_active:
        preview = text_font.render(text_content + "|", True, tools.color)
        screen.blit(
            preview,
            (text_position[0], text_position[1] + TOOLBAR_HEIGHT)
        )

    draw_preview()

    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Keyboard events
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                if text_active:
                    text_active = False
                    text_content = ""

            elif text_active:
                if event.key == pygame.K_RETURN:
                    text_surface = text_font.render(
                        text_content, True, tools.color
                    )
                    canvas.blit(text_surface, text_position)
                    text_active = False
                    text_content = ""

                elif event.key == pygame.K_BACKSPACE:
                    text_content = text_content[:-1]

                elif event.unicode.isprintable():
                    text_content += event.unicode

            elif event.key == pygame.K_1:
                tools.set_brush_size(2)

            elif event.key == pygame.K_2:
                tools.set_brush_size(5)

            elif event.key == pygame.K_3:
                tools.set_brush_size(10)

            elif event.key == pygame.K_s and (
                pygame.key.get_mods() & pygame.KMOD_CTRL
            ):
                filename = datetime.now().strftime(
                    "drawing_%Y%m%d_%H%M%S.png"
                )
                pygame.image.save(canvas, filename)
                print("Saved:", filename)

        # Mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_x, mouse_y = event.pos

            # Toolbar area
            if mouse_y < TOOLBAR_HEIGHT:

                for name, rect in tool_buttons:
                    if rect.collidepoint(event.pos):
                        current_tool = name
                        text_active = False

                for color, rect in color_buttons:
                    if rect.collidepoint(event.pos):
                        tools.set_color(color)

                for size, rect in brush_buttons:
                    if rect.collidepoint(event.pos):
                        tools.set_brush_size(size)

            # Canvas area
            else:
                canvas_pos = (
                    mouse_x,
                    mouse_y - TOOLBAR_HEIGHT
                )

                if current_tool == "Text":
                    text_active = True
                    text_position = canvas_pos
                    text_content = ""

                elif current_tool == "Fill":
                    tools.flood_fill(canvas, canvas_pos)

                else:
                    drawing = True
                    start_pos = canvas_pos
                    last_pos = canvas_pos

        # Mouse movement while drawing
        if event.type == pygame.MOUSEMOTION and drawing:

            mouse_x, mouse_y = event.pos

            if mouse_y >= TOOLBAR_HEIGHT:
                current_pos = (
                    mouse_x,
                    mouse_y - TOOLBAR_HEIGHT
                )

                if current_tool == "Pencil":
                    tools.draw_pencil(
                        canvas,
                        last_pos,
                        current_pos
                    )

                elif current_tool == "Eraser":
                    tools.erase(
                        canvas,
                        last_pos,
                        current_pos
                    )

                last_pos = current_pos

        # Mouse release
        if event.type == pygame.MOUSEBUTTONUP and drawing:

            mouse_x, mouse_y = event.pos

            if mouse_y >= TOOLBAR_HEIGHT:
                end_pos = (
                    mouse_x,
                    mouse_y - TOOLBAR_HEIGHT
                )

                if current_tool == "Line":
                    tools.draw_line(canvas, start_pos, end_pos)

                elif current_tool == "Rectangle":
                    tools.draw_rectangle(canvas, start_pos, end_pos)

                elif current_tool == "Circle":
                    tools.draw_circle(canvas, start_pos, end_pos)

                elif current_tool == "Square":
                    tools.draw_square(canvas, start_pos, end_pos)

                elif current_tool == "Triangle":
                    tools.draw_triangle(canvas, start_pos, end_pos)

                elif current_tool == "Equilateral":
                    tools.draw_equilateral_triangle(
                        canvas, start_pos, end_pos
                    )

                elif current_tool == "Rhombus":
                    tools.draw_rhombus(canvas, start_pos, end_pos)

            drawing = False
            start_pos = None
            last_pos = None

    clock.tick(60)


pygame.quit()
sys.exit()
