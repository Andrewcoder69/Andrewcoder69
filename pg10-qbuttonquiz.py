import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("10 Question Quiz")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Define font
font = pygame.font.Font(None, 36)

# Define questions and answers
questions = [
    "What is the capital of France?",
    "What is 2 + 2?",
    "What is the color of the sky?",
    "What is the capital of Spain?",
    "What is 5 * 6?",
    "What is the largest planet?",
    "What is the capital of Italy?",
    "What is 9 / 3?",
    "What is the color of grass?",
    "What is the capital of Germany?"
]

answers = [
    ["Paris", "London", "Berlin", "Madrid"],
    ["3", "4", "5", "6"],
    ["Blue", "Green", "Red", "Yellow"],
    ["Madrid", "Barcelona", "Seville", "Valencia"],
    ["30", "25", "20", "35"],
    ["Jupiter", "Mars", "Earth", "Saturn"],
    ["Rome", "Milan", "Naples", "Turin"],
    ["2", "3", "4", "5"],
    ["Green", "Blue", "Red", "Yellow"],
    ["Berlin", "Munich", "Hamburg", "Frankfurt"]
]

correct_answers = [0, 1, 0, 0, 0, 0, 0, 1, 0, 0]

# Quiz state
current_question = 0
score = 0

# Button class
class Button:
    def __init__(self, text, x, y, width, height, callback):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.callback = callback

    def draw(self, screen):
        pygame.draw.rect(screen, BLUE, self.rect)
        text_surf = font.render(self.text, True, WHITE)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def click(self):
        self.callback()

# Button callback functions
def answer_callback(index):
    global current_question, score
    if index == correct_answers[current_question]:
        score += 1
    current_question += 1
    if current_question >= len(questions):
        print(f"Quiz finished! Your score: {score}/{len(questions)}")
        pygame.quit()
        sys.exit()

# Create buttons
buttons = []
button_width, button_height = 200, 50
for i in range(4):
    button = Button("", 300, 200 + i * 60, button_width, button_height, lambda i=i: answer_callback(i))
    buttons.append(button)

# Main loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for button in buttons:
                if button.rect.collidepoint(event.pos):
                    button.click()

    if current_question < len(questions):
        question_text = font.render(questions[current_question], True, BLACK)
        screen.blit(question_text, (50, 50))
        for i, button in enumerate(buttons):
            button.text = answers[current_question][i]
            button.draw(screen)
    else:
        final_text = font.render(f"Quiz finished! Your score: {score}/{len(questions)}", True, BLACK)
        screen.blit(final_text, (50, 50))

    pygame.display.flip()

pygame.quit()
