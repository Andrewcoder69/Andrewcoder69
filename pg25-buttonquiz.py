import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("25 Question Quiz")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Font
font = pygame.font.Font(None, 36)

# Questions and answers
questions = [
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "answer": "Paris"},
    # Add more questions here
]

# Button class
class Button:
    def __init__(self, text, x, y, width, height, color, hover_color):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.hover_color = hover_color

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, self.hover_color, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)
        text_surf = font.render(self.text, True, BLACK)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
        return False

# Create buttons for options
buttons = []
for i in range(4):
    buttons.append(Button("", 150, 200 + i * 100, 500, 50, BLUE, (0, 0, 200)))

# Quiz logic
current_question = 0
score = 0

def display_question(question_data):
    screen.fill(WHITE)
    question_text = font.render(question_data["question"], True, BLACK)
    screen.blit(question_text, (150, 100))
    for i, option in enumerate(question_data["options"]):
        buttons[i].text = option
        buttons[i].draw(screen)
    pygame.display.flip()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        for button in buttons:
            if button.is_clicked(event):
                if button.text == questions[current_question]["answer"]:
                    score += 1
                current_question += 1
                if current_question < len(questions):
                    display_question(questions[current_question])
                else:
                    screen.fill(WHITE)
                    final_score_text = font.render(f"Your score: {score}/{len(questions)}", True, BLACK)
                    screen.blit(final_score_text, (300, 300))
                    pygame.display.flip()
                    pygame.time.wait(3000)
                    running = False

    if current_question < len(questions):
        display_question(questions[current_question])

pygame.quit()
sys.exit()
