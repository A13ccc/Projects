import pygame

pygame.init()

# Def all Variables
keys = pygame.key.get_pressed()


# Base Sprite Class
class Sprite:
    def __init__(self, file_name, x, y, width, height, scale):
        self.sprite_sheet = pygame.image.load(file_name).convert()
        self.sprite = self.get_image(x, y, width, height)
        self.sprite.set_colorkey((255, 255, 255))
        self.scaled_sprite = pygame.transform.scale(self.sprite, (scale, scale))
        self.pos = pygame.Vector2(0, 0)
        self.velocity = pygame.Vector2(0, 0)
        self.facing = 0

    def get_image(self, x, y, width, height):
        image = pygame.Surface((width, height), pygame.SRCALPHA)
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        return image

    def draw(self, screen):
        screen.blit(self.scaled_sprite, self.pos)


# Player Class
class Player(Sprite):
    def __init__(self, file_name, x, y, width, height, scale):
        super().__init__(file_name, x, y, width, height, scale)

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.pos.x -= 5
            self.facing = -1
        if keys[pygame.K_RIGHT]:
            self.pos.x += 5
            self.facing = 1
        if keys[pygame.K_UP]:
            self.velocity.y = 8


# Enemy Class
class Enemy(Sprite):
    def __init__(self, file_name, x, y, width, height, scale):
        super().__init__(file_name, x, y, width, height, scale)

    def move(self):
        pass


# Bullet Class
class Bullet(Sprite):
    def __init__(self, file_name, x, y, width, height, scale, direction):
        super().__init__(file_name, x, y, width, height, scale)
        self.direction = direction

    def move(self):
        if self.direction == 1:
            self.pos.x -= 10
        else:
            self.pos.x += 10


# Set Screen
WIDTH, HEIGHT = 720, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jump Game")

# Def Colors
black = (0, 0, 0)
darkBlue = (0, 0, 41)

# Def Clock
clock = pygame.time.Clock()

# Load Player Sprite
player = Player(r'./sprites/player/SpriteSheet.png', 0, 0, 16, 16, 32)

# Load Enemy Sprite
enemy = Enemy(r'./sprites/enemy/SpriteSheet.png', 0, 0, 16, 16, 32)

# Def Gravity and Velocity
player_velocity = pygame.Vector2(0, 0)
gravity = 0.5
enemy_velocity = pygame.Vector2(0, 0)

# Def Momentum
momentum = 0.1

# Def Excess Variables
last_projectile_time = 0
bullet_facing = 0

# Def Bullet List
bullets = []

# Game Loop
running = True
while running:
    screen.fill(darkBlue)

    # Draw Player
    player.draw(screen)

    # Move Player
    keys = pygame.key.get_pressed()
    player.move(keys)

    # Draw Enemy
    enemy.draw(screen)

    # Add Projectile
    if keys[pygame.K_SPACE]:
        current_time = pygame.time.get_ticks()
        if current_time - last_projectile_time >= 300:
            print("Space Key Pressed")
            last_projectile_time = current_time
            bullet = Bullet('./sprites/bullet/bullet.png', player.pos.x, player.pos.y, 16, 16, 32, player.facing)
            bullets.append(bullet)

    # Draw Bullets
    for bullet in bullets:
        bullet.draw(screen)
        bullet.move()

    # Remove Bullets that are out of the screen
    bullets = [bullet for bullet in bullets if 0 < bullet.pos.x < screen.get_width()]

    # Apply Momentum
    if player_velocity.x > 0:
        player_velocity.x = max(0, player_velocity.x - momentum)
    elif player_velocity.x < 0:
        player_velocity.x = min(0, player_velocity.x + momentum)

    # Apply velocity to position
    player.pos += player_velocity

    # Gravity
    player_velocity.y += gravity
    player.pos.y += player_velocity.y
    enemy_velocity.y += gravity
    enemy.pos.y += enemy_velocity.y

    # Check Boundaries
    if player.pos.y > screen.get_height() - player.scaled_sprite.get_height():
        player.pos.y = screen.get_height() - player.scaled_sprite.get_height()
        player_velocity.y = 0
    if player.pos.x < -1:
        player.pos.x = -1
    if player.pos.x > 690:
        player.pos.x = 690
    if enemy.pos.y > screen.get_height() - enemy.scaled_sprite.get_height():
        enemy.pos.y = screen.get_height() - enemy.scaled_sprite.get_height()
        enemy_velocity.y = 0
    if enemy.pos.x < -1:
        enemy.pos.x = -1
    if enemy.pos.x > 690:
        enemy.pos.x = 690

    # Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
