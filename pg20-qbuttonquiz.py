import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("20 Question Quiz")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Fonts
font = pygame.font.Font(None, 36)

# Sample questions and answers
questions = [
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "answer": "Paris"},
    {"question": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "answer": "4"},
    # Add more questions here
]

# Button class
class Button:
    def __init__(self, text, x, y, width, height):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = GRAY

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = font.render(self.text, True, BLACK)
        screen.blit(text_surface, (self.rect.x + 10, self.rect.y + 10))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# Create buttons for options
buttons = []
for i in range(4):
    buttons.append(Button("", 150, 200 + i * 60, 500, 50))

# Main quiz loop
current_question = 0
score = 0

def display_question(question):
    screen.fill(WHITE)
    question_text = font.render(question["question"], True, BLACK)
    screen.blit(question_text, (150, 100))
    for i, option in enumerate(question["options"]):
        buttons[i].text = option
        buttons[i].draw(screen)
    pygame.display.flip()

running = True
while running:
    display_question(questions[current_question])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for button in buttons:
                if button.is_clicked(pos):
                    if button.text == questions[current_question]["answer"]:
                        score += 1
                    current_question += 1
                    if current_question >= len(questions):
                        running = False
                    break

# Display final score
screen.fill(WHITE)
final_score_text = font.render(f"Your score: {score}/{len(questions)}", True, BLACK)
screen.blit(final_score_text, (300, 250))
pygame.display.flip()
pygame.time.wait(3000)

pygame.quit()
sys.exit()
