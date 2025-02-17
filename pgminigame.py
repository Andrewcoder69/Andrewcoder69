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

# Player settings
player_size = 50
player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT - 2 * player_size]
player_speed = 10

# Object settings
object_size = 50
object_pos = [random.randint(0, SCREEN_WIDTH - object_size), 0]
object_speed = 10

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch the Falling Objects")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Game loop
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < SCREEN_WIDTH - player_size:
        player_pos[0] += player_speed

    object_pos[1] += object_speed
    if object_pos[1] > SCREEN_HEIGHT:
        object_pos = [random.randint(0, SCREEN_WIDTH - object_size), 0]

    # Collision detection
    if (player_pos[0] < object_pos[0] < player_pos[0] + player_size or
        player_pos[0] < object_pos[0] + object_size < player_pos[0] + player_size) and \
       (player_pos[1] < object_pos[1] < player_pos[1] + player_size or
        player_pos[1] < object_pos[1] + object_size < player_pos[1] + player_size):
        game_over = True

    # Drawing
    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))
    pygame.draw.rect(screen, WHITE, (object_pos[0], object_pos[1], object_size, object_size))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
