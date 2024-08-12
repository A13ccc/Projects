print("""
### Plan
1. **Check Bullet Initialization**: Ensure the bullet's position is correctly set during initialization.
2. **Verify Player Position**: Ensure the player's position is correctly passed to the bullet.
3. **Debug Bullet Drawing**: Add debug statements to verify the bullet's position during drawing.

### Code

#### Update `Bullet` Class
```python
class Bullet(Sprite):
    def __init__(self, file_name, x, y, width, height, scale, direction):
        super().__init__(file_name, x, y, width, height, scale)
        self.direction = direction
        self.pos = pygame.Vector2(x, y)  # Ensure position is set correctly
        print(f"Bullet initialized at position: {self.pos}")

    def move(self):
        if self.direction == 1:
            self.pos.x += 10
        else:
            self.pos.x -= 10

    def draw(self, screen):
        screen.blit(self.scaled_sprite, self.pos)
        print(f"Drawing bullet at position: {self.pos}")
```

#### Update `Player` Class
```python
class Player(Sprite):
    def __init__(self, file_name, x, y, width, height, scale):
        super().__init__(file_name, x, y, width, height, scale)
        self.is_jumping = False
        self.bullets = []

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.pos.x -= 5
            self.facing = -1
        if keys[pygame.K_RIGHT]:
            self.pos.x += 5
            self.facing = 1
        if keys[pygame.K_UP] and not self.is_jumping:
            self.velocity.y = 8
            self.is_jumping = True

    def shoot(self):
        bullet_x = self.pos.x
        bullet_y = self.pos.y
        bullet = Bullet("./sprites/bullet/bullet.png", bullet_x, bullet_y, 16, 16, 32, self.facing)
        self.bullets.append(bullet)
        print(f"Bullet created at position: {bullet.pos}")

    def update_bullets(self, screen):
        for bullet in self.bullets:
            bullet.move()
            bullet.draw(screen)
            print(f"Bullet position: {bullet.pos}")
        self.bullets = [bullet for bullet in self.bullets if 0 < bullet.pos.x < screen.get_width()]
```

#### Update `Game` Class
```python
class Game:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Player("./sprites/player/SpriteSheet.png", 0, 0, 16, 16, 32)
        self.enemies = [Enemy("./sprites/enemy/SpriteSheet.png", 0, 0, 16, 16, 32) for _ in range(5)]

    def run(self):
        last_projectile_time = 0
        while self.running:
            self.events()
            self.update()
            self.draw()
            self.gravity()
            self.boundaries()
            if self.player.pos.y == 570:
                self.player.is_jumping = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                current_time = pygame.time.get_ticks()
                if current_time - last_projectile_time >= 300:
                    print("Shooting")
                    last_projectile_time = current_time
                    self.player.shoot()

            self.player.update_bullets(self.screen)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        keys = pygame.key.get_pressed()
        self.player.move(keys)
        for enemy in self.enemies:
            enemy.move()

    def draw(self):
        self.screen.fill((0, 0, 90))
        self.player.draw(self.screen)
        for enemy in self.enemies:
            enemy.draw(self.screen)
        for bullet in self.player.bullets:
            bullet.draw(self.screen)
        pygame.display.flip()
        self.clock.tick(70)

    def gravity(self):
        self.player.velocity.y -= 0.5
        self.player.pos.y -= self.player.velocity.y
        for enemy in self.enemies:
            enemy.velocity.y -= 0.5
            enemy.pos.y -= enemy.velocity.y

    def boundaries(self):
        if self.player.pos.y > 570:
            self.player.pos.y = 570
            self.player.velocity.y = 0
        if self.player.pos.y < 0:
            self.player.pos.y = 0
            self.player.velocity.y = 0
        if self.player.pos.x >= 765:
            self.player.pos.x = 765
        if self.player.pos.x <= 5:
            self.player.pos.x = 5
        for enemy in self.enemies:
            if enemy.pos.y > 570:
                enemy.pos.y = 570
                enemy.velocity.y = 0
            if enemy.pos.y < 0:
                enemy.pos.y = 0
                enemy.velocity.y = 0
            if enemy.pos.x >= 765:
                enemy.pos.x = 765
            if enemy.pos.x <= 5:
                enemy.pos.x = 5
```
""")
