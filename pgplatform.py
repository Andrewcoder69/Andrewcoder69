import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Platformer")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Player settings
player_size = 50
player_color = BLUE
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT - player_size
player_speed = 5
player_jump = 10
player_velocity_y = 0
gravity = 0.5

# Platform settings
platforms = [
    pygame.Rect(100, 500, 200, 20),
    pygame.Rect(400, 400, 200, 20),
    pygame.Rect(200, 300, 200, 20)
]

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_SPACE]:
        if player_y == SCREEN_HEIGHT - player_size or any(player_x.colliderect(platform) for platform in platforms):
            player_velocity_y = -player_jump

    # Apply gravity
    player_velocity_y += gravity
    player_y += player_velocity_y

    # Collision with the ground
    if player_y >= SCREEN_HEIGHT - player_size:
        player_y = SCREEN_HEIGHT - player_size
        player_velocity_y = 0

    # Collision with platforms
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    for platform in platforms:
        if player_rect.colliderect(platform) and player_velocity_y > 0:
            player_y = platform.top - player_size
            player_velocity_y = 0

    # Clear screen
    screen.fill(WHITE)

    # Draw player
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_size, player_size))

    # Draw platforms
    for platform in platforms:
        pygame.draw.rect(screen, BLACK, platform)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
