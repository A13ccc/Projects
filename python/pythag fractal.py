import pygame
import math

# Initialize Pygame
pygame.init()

# Set up display
width, height = 1200, 800  # Larger screen size
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pythagoras Tree Fractal")

# Define initial color
color = (0, 128, 0)


def draw_square(screen, x, y, size, angle, color):
    """Draw a square based on the top-left corner, size, angle, and color."""
    points = []
    for i in range(4):
        angle_rad = math.radians(angle + i * 90)
        point_x = x + size * math.cos(angle_rad)
        point_y = y - size * math.sin(angle_rad)
        points.append((point_x, point_y))
        x, y = point_x, point_y

    pygame.draw.polygon(screen, color, points)


def draw_pythagoras_tree(screen, x, y, size, angle, depth, color):
    """Draw the Pythagoras tree fractal with color variation."""
    if depth == 0:
        return

    # Draw the base square
    draw_square(screen, x, y, size, angle, color)
    pygame.display.flip()
    pygame.time.delay(100)  # Add delay to watch the drawing process

    # Slightly change the color for the next squares
    new_color = ((color[0] + 15) % 256, (color[1] + 10) % 256, (color[2] + 5) % 256)

    # Calculate the new squares' position and size
    new_size = size * math.sqrt(2) / 2

    # Calculate positions for left and right branches
    angle_rad = math.radians(angle - 45)
    new_x1 = x + size * math.cos(angle_rad)
    new_y1 = y - size * math.sin(angle_rad)

    angle_rad = math.radians(angle + 45)
    new_x2 = x + size * math.cos(angle_rad + math.radians(90))
    new_y2 = y - size * math.sin(angle_rad + math.radians(90))

    # Left branch
    draw_pythagoras_tree(screen, new_x1, new_y1, new_size, angle - 45, depth - 1, new_color)

    # Right branch
    draw_pythagoras_tree(screen, new_x2, new_y2, new_size, angle + 45, depth - 1, new_color)


def main():
    running = True
    depth = 10  # Depth of recursion
    size = 150  # Initial size of the square
    angle = 0  # Initial angle

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))  # White background

        # Starting position for the tree, close to middle and near bottom
        start_x = width // 2 - size // 2
        start_y = height - 100

        # Draw the Pythagoras tree
        draw_pythagoras_tree(screen, start_x, start_y, size, angle, depth, color)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
