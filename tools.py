
import pygame


class DrawingTools:
    def __init__(self):
        self.color = (0, 0, 0)
        self.brush_size = 5

    def set_color(self, color):
        self.color = color

    def set_brush_size(self, size):
        self.brush_size = size

    def draw_pencil(self, surface, start_pos, end_pos):
        pygame.draw.line(
            surface,
            self.color,
            start_pos,
            end_pos,
            self.brush_size
        )

        pygame.draw.circle(
            surface,
            self.color,
            start_pos,
            self.brush_size // 2
        )

    def draw_line(self, surface, start_pos, end_pos):
        pygame.draw.line(
            surface,
            self.color,
            start_pos,
            end_pos,
            self.brush_size
        )

    def draw_rectangle(self, surface, start_pos, end_pos):
        rect = pygame.Rect(
            start_pos,
            (end_pos[0] - start_pos[0],
             end_pos[1] - start_pos[1])
        )
        rect.normalize()

        if rect.width > 0 and rect.height > 0:
            pygame.draw.rect(
                surface,
                self.color,
                rect,
                self.brush_size
            )

    def draw_circle(self, surface, start_pos, end_pos):
        radius = int(
            ((end_pos[0] - start_pos[0]) ** 2 +
             (end_pos[1] - start_pos[1]) ** 2) ** 0.5
        )

        pygame.draw.circle(
            surface,
            self.color,
            start_pos,
            radius,
            self.brush_size
        )

    def draw_square(self, surface, start_pos, end_pos):
        side = min(
            abs(end_pos[0] - start_pos[0]),
            abs(end_pos[1] - start_pos[1])
        )

        x = start_pos[0]
        y = start_pos[1]

        rect = pygame.Rect(
            min(x, end_pos[0]),
            min(y, end_pos[1]),
            side,
            side
        )

        pygame.draw.rect(
            surface,
            self.color,
            rect,
            self.brush_size
        )

    def draw_triangle(self, surface, start_pos, end_pos):
        x1, y1 = start_pos
        x2, y2 = end_pos

        points = [
            (x1, y1),
            (x2, y2),
            ((x1 + x2) // 2, y2)
        ]

        pygame.draw.polygon(
            surface,
            self.color,
            points,
            self.brush_size
        )

    def draw_equilateral_triangle(self, surface, start_pos, end_pos):
        x1, y1 = start_pos
        x2, y2 = end_pos

        side = abs(x2 - x1)
        height = int(side * 0.866)

        points = [
            (x1, y2),
            (x2, y2),
            ((x1 + x2) // 2, y2 - height)
        ]

        pygame.draw.polygon(
            surface,
            self.color,
            points,
            self.brush_size
        )

    def draw_rhombus(self, surface, start_pos, end_pos):
        x1, y1 = start_pos
        x2, y2 = end_pos

        center_x = (x1 + x2) // 2
        center_y = (y1 + y2) // 2

        points = [
            (center_x, y1),
            (x2, center_y),
            (center_x, y2),
            (x1, center_y)
        ]

        pygame.draw.polygon(
            surface,
            self.color,
            points,
            self.brush_size
        )

    def erase(self, surface, start_pos, end_pos):
        pygame.draw.line(
            surface,
            (255, 255, 255),
            start_pos,
            end_pos,
            self.brush_size
        )

        pygame.draw.circle(
            surface,
            (255, 255, 255),
            start_pos,
            self.brush_size // 2
        )

    def flood_fill(self, surface, position):
        width, height = surface.get_size()

        x, y = position

        if not (0 <= x < width and 0 <= y < height):
            return

        target_color = surface.get_at((x, y))
        fill_color = self.color

        if target_color == fill_color:
            return

        pixels = [(x, y)]
        surface.set_at((x, y), fill_color)

        while pixels:
            current_x, current_y = pixels.pop()

            neighbors = [
                (current_x + 1, current_y),
                (current_x - 1, current_y),
                (current_x, current_y + 1),
                (current_x, current_y - 1)
            ]

            for nx, ny in neighbors:
                if 0 <= nx < width and 0 <= ny < height:
                    if surface.get_at((nx, ny)) == target_color:
                        surface.set_at((nx, ny), fill_color)
                        pixels.append((nx, ny))
