import tkinter as tk
import random

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.canvas = tk.Canvas(root, width=400, height=400, bg="black")
        self.canvas.pack()
        self.snake = [(20, 20), (20, 30), (20, 40)]
        self.food = self.create_food()
        self.direction = "Down"
        self.running = True
        self.root.bind("<KeyPress>", self.change_direction)
        self.update()

    def create_food(self):
        x = random.randint(0, 19) * 20
        y = random.randint(0, 19) * 20
        return (x, y)

    def change_direction(self, event):
        if event.keysym in ["Up", "Down", "Left", "Right"]:
            self.direction = event.keysym

    def update(self):
        if self.running:
            self.move_snake()
            self.check_collisions()
            self.draw_elements()
            self.root.after(100, self.update)

    def move_snake(self):
        head_x, head_y = self.snake[0]
        if self.direction == "Up":
            new_head = (head_x, head_y - 20)
        elif self.direction == "Down":
            new_head = (head_x, head_y + 20)
        elif self.direction == "Left":
            new_head = (head_x - 20, head_y)
        elif self.direction == "Right":
            new_head = (head_x + 20, head_y)
        self.snake = [new_head] + self.snake[:-1]

    def check_collisions(self):
        head_x, head_y = self.snake[0]
        if head_x < 0 or head_x >= 400 or head_y < 0 or head_y >= 400 or (head_x, head_y) in self.snake[1:]:
            self.running = False
        if (head_x, head_y) == self.food:
            self.snake.append(self.snake[-1])
            self.food = self.create_food()

    def draw_elements(self):
        self.canvas.delete(tk.ALL)
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x + 20, y + 20, fill="green")
        food_x, food_y = self.food
        self.canvas.create_rectangle(food_x, food_y, food_x + 20, food_y + 20, fill="red")

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
