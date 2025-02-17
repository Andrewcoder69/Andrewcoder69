import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Game settings
PLAYER_SIZE = 50
OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 100
OBSTACLE_SPEED = 5
GRAVITY = 1
JUMP_STRENGTH = 15

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("One Button Game")

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = SCREEN_HEIGHT - PLAYER_SIZE
        self.velocity = 0

    def update(self):
        self.velocity += GRAVITY
        self.rect.y += self.velocity

        # Prevent the player from falling below the ground
        if self.rect.y >= SCREEN_HEIGHT - PLAYER_SIZE:
            self.rect.y = SCREEN_HEIGHT - PLAYER_SIZE
            self.velocity = 0

    def jump(self):
        if self.rect.y == SCREEN_HEIGHT - PLAYER_SIZE:
            self.velocity = -JUMP_STRENGTH

# Obstacle class
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = SCREEN_HEIGHT - OBSTACLE_HEIGHT

    def update(self):
        self.rect.x -= OBSTACLE_SPEED
        if self.rect.x < -OBSTACLE_WIDTH:
            self.rect.x = SCREEN_WIDTH
            self.rect.y = SCREEN_HEIGHT - OBSTACLE_HEIGHT

# Create sprite groups
all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()

# Create player
player = Player()
all_sprites.add(player)

# Create obstacles
for _ in range(3):
    obstacle = Obstacle()
    obstacle.rect.x += random.randint(200, 800)
    all_sprites.add(obstacle)
    obstacles.add(obstacle)

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()

    # Update
    all_sprites.update()

    # Check for collisions
    if pygame.sprite.spritecollideany(player, obstacles):
        running = False

    # Draw
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

pygame.quit()
