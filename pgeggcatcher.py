import tkinter as tk
import random

# Initialize the main window
root = tk.Tk()
root.title("Egg Catcher Game")
root.resizable(False, False)
canvas = tk.Canvas(root, width=400, height=400, bg='sky blue')
canvas.pack()

# Basket
basket = canvas.create_rectangle(160, 360, 240, 380, fill='brown')

# Egg
egg = canvas.create_oval(190, 50, 210, 70, fill='white')

# Variables
egg_speed = 5
basket_speed = 20
score = 0

# Score display
score_text = canvas.create_text(10, 10, anchor='nw', font=('Arial', 14), fill='black', text=f'Score: {score}')

# Functions to move the basket
def move_left(event):
    canvas.move(basket, -basket_speed, 0)

def move_right(event):
    canvas.move(basket, basket_speed, 0)

# Function to drop the egg
def drop_egg():
    global score
    canvas.move(egg, 0, egg_speed)
    egg_pos = canvas.coords(egg)
    basket_pos = canvas.coords(basket)
    
    # Check if the egg is caught
    if egg_pos[3] >= basket_pos[1] and basket_pos[0] < egg_pos[0] < basket_pos[2]:
        score += 1
        canvas.itemconfig(score_text, text=f'Score: {score}')
        reset_egg()
    elif egg_pos[3] > 400:
        reset_egg()
    
    root.after(50, drop_egg)

# Function to reset the egg position
def reset_egg():
    x = random.randint(10, 390)
    canvas.coords(egg, x-10, 50, x+10, 70)

# Bind keys to move the basket
root.bind('<Left>', move_left)
root.bind('<Right>', move_right)

# Start the game
drop_egg()
root.mainloop()
