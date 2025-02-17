import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Button Quiz Game')

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Define fonts
font = pygame.font.Font(None, 36)

# Define button class
class Button:
    def __init__(self, text, pos, color, action=None):
        self.text = text
        self.pos = pos
        self.color = color
        self.action = action
        self.rect = pygame.Rect(pos[0], pos[1], 200, 50)
        self.text_surf = font.render(text, True, WHITE)
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.text_surf, self.text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                if self.action:
                    self.action()

# Define quiz question and answers
question = "What is the capital of France?"
answers = ["Paris", "London", "Berlin", "Madrid"]
correct_answer = "Paris"

# Define actions for buttons
def show_question():
    global current_question
    current_question = True

def check_answer(answer):
    global current_question
    if answer == correct_answer:
        print("Correct!")
    else:
        print("Wrong!")
    current_question = False

# Create buttons
start_button = Button("Start Quiz", (300, 250), BLUE, show_question)
answer_buttons = [Button(answer, (300, 350 + i * 60), GREEN, lambda a=answer: check_answer(a)) for i, answer in enumerate(answers)]

# Main loop
running = True
current_question = False
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if current_question:
            for button in answer_buttons:
                if button.is_clicked(event):
                    button.action()
        else:
            if start_button.is_clicked(event):
                start_button.action()

    if current_question:
        question_surf = font.render(question, True, BLACK)
        question_rect = question_surf.get_rect(center=(width // 2, 150))
        screen.blit(question_surf, question_rect)
        for button in answer_buttons:
            button.draw(screen)
    else:
        start_button.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()
