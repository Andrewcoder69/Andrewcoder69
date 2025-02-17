import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('2 Button Game')

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Define button properties
button1 = pygame.Rect(50, 100, 100, 50)
button2 = pygame.Rect(250, 100, 100, 50)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button1.collidepoint(event.pos):
                print("Button 1 clicked!")
            elif button2.collidepoint(event.pos):
                print("Button 2 clicked!")

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw buttons
    pygame.draw.rect(screen, RED, button1)
    pygame.draw.rect(screen, GREEN, button2)

    # Draw button text
    font = pygame.font.Font(None, 36)
    text1 = font.render('Button 1', True, BLACK)
    text2 = font.render('Button 2', True, BLACK)
    screen.blit(text1, (button1.x + 10, button1.y + 10))
    screen.blit(text2, (button2.x + 10, button2.y + 10))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
