import tkinter as tk
import random

class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake Game")
        self.master.resizable(False, False)
        
       
        self.board_width = 500
        self.board_height = 500
        self.cell_size = 20
        self.snake = [(100, 100), (80, 100), (60, 100)]  
        self.snake_direction = "Right"
        self.food = None
        self.score = 0  
        
        
        self.canvas = tk.Canvas(self.master, width=self.board_width, height=self.board_height, bg="black")
        self.canvas.pack()
        
        
        self.score_label = tk.Label(self.master, text="Score: 0", font=('Helvetica', 12), bg="black", fg="white")
        self.score_label.pack()
        
        
        self.create_food()
        self.update_game()
        
        
        self.master.bind("<Left>", lambda e: self.change_direction("Left"))
        self.master.bind("<Right>", lambda e: self.change_direction("Right"))
        self.master.bind("<Up>", lambda e: self.change_direction("Up"))
        self.master.bind("<Down>", lambda e: self.change_direction("Down"))
    
    def create_food(self):
        
        self.food = (random.randint(0, (self.board_width - self.cell_size) // self.cell_size) * self.cell_size,
                    random.randint(0, (self.board_height - self.cell_size) // self.cell_size) * self.cell_size)
        self.canvas.create_rectangle(self.food[0], self.food[1], self.food[0] + self.cell_size, self.food[1] + self.cell_size, fill="red")
    
    def change_direction(self, new_direction):
        
        if (self.snake_direction == "Left" and new_direction != "Right") or \
           (self.snake_direction == "Right" and new_direction != "Left") or \
           (self.snake_direction == "Up" and new_direction != "Down") or \
           (self.snake_direction == "Down" and new_direction != "Up"):
            self.snake_direction = new_direction
    
    def update_game(self):
        
       
        head_x, head_y = self.snake[0]
        if self.snake_direction == "Left":
            head_x -= self.cell_size
        elif self.snake_direction == "Right":
            head_x += self.cell_size
        elif self.snake_direction == "Up":
            head_y -= self.cell_size
        elif self.snake_direction == "Down":
            head_y += self.cell_size
        
        new_head = (head_x, head_y)
        self.snake = [new_head] + self.snake[:-1]
        
        
        if (head_x < 0 or head_x >= self.board_width or 
            head_y < 0 or head_y >= self.board_height or 
            new_head in self.snake[1:]):
            self.game_over()
            return
        
       
        if new_head == self.food:
            self.snake.append(self.snake[-1])  
            self.create_food()  
            self.score += 1  
            self.update_score()  
            
        
        self.canvas.delete("all")
        self.draw_snake()
        self.draw_food()
        
        
        self.master.after(100, self.update_game)
    
    def draw_snake(self):
        
        for segment in self.snake:
            self.canvas.create_rectangle(segment[0], segment[1], segment[0] + self.cell_size, segment[1] + self.cell_size, fill="green")
    
    def draw_food(self):
        
        self.canvas.create_rectangle(self.food[0], self.food[1], self.food[0] + self.cell_size, self.food[1] + self.cell_size, fill="red")
    
    def update_score(self):
        
        self.score_label.config(text=f"Score: {self.score}")
    
    def game_over(self):
        
        self.canvas.create_text(self.board_width // 2, self.board_height // 2, text="Game Over!", fill="white", font=('Helvetica', 24))
        self.master.after(1000, self.master.quit)  


if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
