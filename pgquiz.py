import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Quiz Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up fonts
font = pygame.font.Font(None, 36)

# Quiz data
questions = [
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "answer": "Paris"},
    {"question": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "answer": "4"},
    {"question": "What is the color of the sky?", "options": ["Blue", "Green", "Red", "Yellow"], "answer": "Blue"}
]

current_question = 0
score = 0

def display_question(question_data):
    screen.fill(WHITE)
    question_text = font.render(question_data["question"], True, BLACK)
    screen.blit(question_text, (20, 20))
    
    for i, option in enumerate(question_data["options"]):
        option_text = font.render(f"{i + 1}. {option}", True, BLACK)
        screen.blit(option_text, (20, 80 + i * 40))

def check_answer(question_data, user_answer):
    global score
    if question_data["options"][user_answer] == question_data["answer"]:
        score += 1

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
                user_answer = event.key - pygame.K_1
                check_answer(questions[current_question], user_answer)
                current_question += 1
                if current_question >= len(questions):
                    running = False

    if current_question < len(questions):
        display_question(questions[current_question])
    else:
        screen.fill(WHITE)
        final_score_text = font.render(f"Your score: {score}/{len(questions)}", True, BLACK)
        screen.blit(final_score_text, (20, 20))

    pygame.display.flip()

pygame.quit()
sys.exit()
