import pygame


# SpriteSheet Class
class SpriteSheet:
    def __init__(self, file_name):
        self.sprite_sheet = pygame.image.load(file_name).convert()

    def get_image(self, x, y, width, height):
        image = pygame.Surface((width, height), pygame.SRCALPHA)
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        return image


pygame.init()

# Set Screen
WIDTH, HEIGHT = 720, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jump Game")

# Def Colors
black = (0, 0, 0)

# Def Clock
clock = pygame.time.Clock()

# Define Initial Player Position
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# Load SpriteSheet
sprite_sheet = SpriteSheet(r'C:\Users\Alec\Documents\Projects\Python\Game\sprites\player\SpriteSheet.png')

# Extract and scale the sprite (assuming the sprite is at position (0, 0) with width and height of 16)
player_sprite = sprite_sheet.get_image(0, 0, 16, 16)

# Set the color key to remove the background (assuming the background color is white)
player_sprite.set_colorkey((255, 255, 255))

# Scale the sprite
scaled_player_sprite = pygame.transform.scale(player_sprite, (32, 32))

# Game Loop
running = True
while running:
    screen.fill(black)

    # Draw Player
    screen.blit(scaled_player_sprite, player_pos)

    # Move Player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos.x -= 5
    if keys[pygame.K_RIGHT]:
        player_pos.x += 5
    if keys[pygame.K_UP]:
        player_pos.y -= 5
    if keys[pygame.K_DOWN]:
        player_pos.y += 5

    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
