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

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Racing Game")

# Load car image
car_image = pygame.image.load("car.png")
car_rect = car_image.get_rect()
car_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100)

# Car speed
car_speed = 5

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_rect.left > 0:
        car_rect.x -= car_speed
    if keys[pygame.K_RIGHT] and car_rect.right < SCREEN_WIDTH:
        car_rect.x += car_speed

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the car
    screen.blit(car_image, car_rect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
