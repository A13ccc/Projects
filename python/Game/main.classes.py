import pygame

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game")
screen.fill((0, 0, 90))


# noinspection DuplicatedCode
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

    # noinspection PyShadowingNames
    def draw(self, screen):
        screen.blit(self.scaled_sprite, self.pos)


# Bullet Class
class Bullet(Sprite):
    def __init__(self, file_name, x, y, width, height, scale, direction):
        super().__init__(file_name, x, y, width, height, scale)
        self.direction = direction
        self.pos = pygame.Vector2(x, y)
        print(f"Bullet sprite loaded: {file_name}")

    def move(self):
        if self.direction == 1:
            self.pos.x += 10
        else:
            self.pos.x -= 10

    def draw(self, screen):
        screen.blit(self.scaled_sprite, self.pos)
        print(f"Drawing bullet at position: {self.pos}")


# Player Class
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


# Enemy Class
class Enemy(Sprite):
    def __init__(self, file_name, x, y, width, height, scale):
        super().__init__(file_name, x, y, width, height, scale)
        self.direction = 1

    def move(self):

        if self.pos.y == 570:
            self.pos.x += self.direction * 4.6

            if self.pos.x <= 5:
                self.direction = 1
            elif self.pos.x >= 765:
                self.direction = -1


# Main Game Class
class Game:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Player("./sprites/player/SpriteSheet.png", 0, 0, 16, 16, 32)
        self.enemies = [Enemy("./sprites/enemy/SpriteSheet.png", 0, 0, 16, 16, 32) for _ in range(5)]
        self.bullets = []

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
                    self.shoot()

            self.update_bullets(self.screen)

    def shoot(self):
        bullet_x = self.player.pos.x
        bullet_y = self.player.pos.y
        bullet = Bullet("./sprites/bullet/bullet.png", bullet_x, bullet_y, 16, 16, 32, self.player.facing)
        self.bullets.append(bullet)
        print(f"Bullet created at position: {bullet.pos}")

    def update_bullets(self, screen):
        for bullet in self.bullets:
            bullet.move()
            bullet.draw(screen)
            print(f"Bullet position: {bullet.pos}")
        self.bullets = [bullet for bullet in self.bullets if 0 < bullet.pos.x < screen.get_width()]

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
        self.screen.fill((5, 0, 20))
        self.player.draw(self.screen)
        for enemy in self.enemies:
            enemy.draw(self.screen)
        for bullet in self.player.bullets:
            bullet.draw(self.screen)
        pygame.display.update()
        self.clock.tick(80)

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


if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.run()
    pygame.quit()
