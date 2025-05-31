import tkinter as tk                       
import random 

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")  # Set the title of the window
        
        # Create a canvas widget, which will serve as the game's playing field
        self.canvas = tk.Canvas(root, width=600, height=400, bg='black')
        self.canvas.pack()  # Pack the canvas into the window

        # Initialize the snake with three segments
        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.snake_direction = 'Right'  # Set the initial direction of the snake
        self.food = self.create_food()  # Create the first food item

        self.score = 0  # Initialize the score to 0

        self.game_running = True  # Set the game running flag to True

        self.root.bind("<KeyPress>", self.change_direction)  # Bind the key press event to the change_direction method
        self.update_snake()  # Start the snake update loop
        self.run_game()  # Start the game loop

    def create_food(self):
        # Generate a random position for the food
        while True:
            x = random.randint(0, 59) * 10  # Random x position in increments of 10
            y = random.randint(0, 39) * 10  # Random y position in increments of 10
            if (x, y) not in self.snake:  # Ensure the food is not placed on the snake
                return (x, y)

    def change_direction(self, event):
        new_direction = event.keysym  # Get the key symbol of the pressed key
        # Dictionary to prevent the snake from reversing
        all_directions = {'Left': 'Right', 'Right': 'Left', 'Up': 'Down', 'Down': 'Up'}
        # Change the snake's direction only if it's not directly opposite to the current direction
        if new_direction in all_directions and new_direction != all_directions[self.snake_direction]:
            self.snake_direction = new_direction

    def update_snake(self):
        if not self.game_running:
            return  # Exit if the game is not running
        
        head_x, head_y = self.snake[0]  # Get the current head position of the snake
        # Update the head position based on the current direction
        if self.snake_direction == 'Left':
            head_x -= 10
        elif self.snake_direction == 'Right':
            head_x += 10
        elif self.snake_direction == 'Up':
            head_y -= 10
        elif self.snake_direction == 'Down':
            head_y += 10

        new_head = (head_x, head_y)  # Create a new head position

        # Check if the snake collides with the wall or itself
        if (
            head_x < 0 or head_x >= 600 or
            head_y < 0 or head_y >= 400 or
            new_head in self.snake
        ):
            self.game_running = False  # Stop the game
            # Display "Game Over" text
            self.canvas.create_text(300, 200, text="Game Over", fill="red", font=('Arial', 24))
            return
        # Add the new head to the snake's body
        self.snake = [new_head] + self.snake[:-1]
        if new_head == self.food:  # Check if the snake has eaten the food
            self.snake.append(self.snake[-1])  # Grow the snake
            self.food = self.create_food()  # Create new food
            self.score += 1  # Increase the score

        self.draw_elements()  # Draw the snake and food
        self.root.after(200, self.update_snake)  # Call update_snake again after 200 milliseconds

    def draw_elements(self):
        self.canvas.delete(tk.ALL)  # Clear the canvas
        # Draw the snake
        for (x, y) in self.snake:
            self.canvas.create_rectangle(x, y, x + 10, y + 10, fill='green')
        # Draw the food
        food_x, food_y = self.food
        self.canvas.create_oval(food_x, food_y, food_x + 10, food_y + 10, fill='red')

    def run_game(self):
        self.root.after(200, self.update_snake)  # Start the update loop with a delay of 200 milliseconds

if __name__ == "__main__":
    root = tk.Tk()  # Create the main window
    game = SnakeGame(root)  # Create an instance of the SnakeGame class
    root.mainloop()  # Start the Tkinter event loop
