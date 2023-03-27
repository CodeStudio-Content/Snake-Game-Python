import tkinter as tk
import random

# Constants for the game
BOARD_WIDTH = 600
BOARD_HEIGHT = 600
CELL_SIZE = 20
INITIAL_SPEED = 200
OBSTACLE_COUNT = 10
COLORS = ["green", "red", "blue", "yellow"]
DIRECTIONS = {"Up": (0, -1), "Down": (0, 1), "Left": (-1, 0), "Right": (1, 0)}

# Snake class to hold information about the snake
class Snake:
    def __init__(self, canvas):
        self.canvas = canvas
        self.head_x = BOARD_WIDTH // 2
        self.head_y = BOARD_HEIGHT // 2
        self.body = [(self.head_x, self.head_y)]
        self.direction = DIRECTIONS["Right"]
        self.color = "black"
    
    # Move the snake in the current direction
    def move(self):
        new_head_x = self.head_x + CELL_SIZE * self.direction[0]
        new_head_y = self.head_y + CELL_SIZE * self.direction[1]
        
        # Check if the snake has collided with the wall or itself
        if (new_head_x < 0 or new_head_x >= BOARD_WIDTH or
            new_head_y < 0 or new_head_y >= BOARD_HEIGHT or
            (new_head_x, new_head_y) in self.body[:-1]):
            return False
        
        # Update the body of the snake
        self.body.insert(0, (new_head_x, new_head_y))
        if len(self.body) > 1:
            self.body.pop()
        
        # Update the head of the snake
        self.head_x = new_head_x
        self.head_y = new_head_y
        
        return True
    
    # Change the direction of the snake
    def change_direction(self, event):
        for key in DIRECTIONS:
            if event.keysym == key:
                new_direction = DIRECTIONS[key]
                if (new_direction[0] != -self.direction[0] and
                    new_direction[1] != -self.direction[1]):
                    self.direction = new_direction
                    break
    
    # Draw the snake on the canvas
    def draw(self):
        for segment in self.body:
            x = segment[0]
            y = segment[1]
            self.canvas.create_rectangle(x, y, x+CELL_SIZE, y+CELL_SIZE, fill=self.color, outline="")
    
    # Check if the snake has eaten the food
    def check_food(self, food):
        return self.head_x == food.x and self.head_y == food.y
    
    # Grow the snake by one segment
    def grow(self):
        tail_x = self.body[-1][0]
        tail_y = self.body[-1][1]
        self.body.append((tail_x, tail_y))
    
    # Check if the snake has collided with an obstacle
    def check_obstacle(self, obstacle_list):
        return (self.head_x, self.head_y) in obstacle_list


# Food class to hold information about the food
class Food:
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = 0
        self.y = 0
        self.color = COLORS[random.randint(0, len(COLORS)-1)]
        self.draw()
    
    # Move the food to a new location
    def move(self):
        self.canvas.delete("food")
        self.x = (random.randint(0, BOARD_WIDTH // CELL_SIZE - 1)) * CELL_SIZE
        self.y = (random.randint(0, BOARD_HEIGHT // CELL_SIZE - 1)) * CELL_SIZE
        self.draw()
    
    # Draw the food on the canvas
    def draw(self):
        self.canvas.create_oval(self.x, self.y, self.x+CELL_SIZE, self.y+CELL_SIZE, fill=self.color, outline="", tags="food")


# Obstacle class to hold information about the obstacles
class Obstacle:
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = 0
        self.y = 0
        self.color = "brown"
        self.draw()
    
    # Move the obstacle to a new location
    def move(self):
        self.canvas.delete("obstacle")
        self.x = (random.randint(0, BOARD_WIDTH // CELL_SIZE - 1)) * CELL_SIZE
        self.y = (random.randint(0, BOARD_HEIGHT // CELL_SIZE - 1)) * CELL_SIZE
        self.draw()
    
    # Draw the obstacle on the canvas
    def draw(self):
        self.canvas.create_rectangle(self.x, self.y, self.x+CELL_SIZE, self.y+CELL_SIZE,
                                       fill=self.color, outline="", tags="obstacle")


class Game:
    high_scores = []
    def __init__(self):
        self.window = tk.Tk()
        self.canvas = tk.Canvas(self.window, width=BOARD_WIDTH, height=BOARD_HEIGHT)
        self.canvas.pack()
        self.snake = Snake(self.canvas)
        self.food = Food(self.canvas)
        self.obstacle_list = []
        self.score = 0
        self.speed = INITIAL_SPEED
        self.level = 1
        self.setup_obstacles()
        self.paused = False 
        
        self.high_score = 0

        # Bind arrow keys to snake movement
        self.window.bind("<Up>", self.snake.change_direction)
        self.window.bind("<Down>", self.snake.change_direction)
        self.window.bind("<Left>", self.snake.change_direction)
        self.window.bind("<Right>", self.snake.change_direction)
        # Bind spacebar to toggle pause
        self.window.bind("<space>", self.toggle_pause)

    def toggle_pause(self, event):
        self.paused = not self.paused

    def setup_obstacles(self):
        for i in range(OBSTACLE_COUNT):
            obstacle = Obstacle(self.canvas)
            
            # Check if the obstacle overlaps with the snake or the food
            while self.snake.check_obstacle(self.obstacle_list) or \
                (obstacle.x, obstacle.y) == (self.food.x, self.food.y):
                obstacle.move()
            
            # If the current level is 2, generate additional obstacles
            if self.level == 2:
                for j in range(2):
                    obstacle2 = Obstacle(self.canvas)
                    
                    # Check if the obstacle overlaps with the snake, food or other obstacles
                    while self.snake.check_obstacle(self.obstacle_list) or \
                        (obstacle2.x, obstacle2.y) == (self.food.x, self.food.y) or \
                        (obstacle2.x, obstacle2.y) in self.obstacle_list:
                        obstacle2.move()
                    
                    # Add the new obstacle to the list
                    self.obstacle_list.append((obstacle2.x, obstacle2.y))
            
            # Add the original obstacle to the list
            self.obstacle_list.append((obstacle.x, obstacle.y))


    def update_score(self):
        self.score += 1
        
        if self.score % 10 == 0:
            if self.level < 3:
                self.level += 1
            else:
                print("Game over")
            self.speed = 200
            self.canvas.delete("obstacle")
            self.obstacle_list = []
            self.setup_obstacles()
            
        
        #  code for initializing the game window and canvas
        if len(Game.high_scores) < 10: # check if there are less than 10 high scores
            Game.high_scores += [0] * (10 - len(Game.high_scores)) # pad with zeros

            
        # Update the current score and the highest score
        if self.score > self.high_score:
            self.high_score = self.score
            
            if self.high_score > Game.high_scores[-1]:
                Game.high_scores.append(self.high_score)
                Game.high_scores = sorted(Game.high_scores, reverse=True)[:10]
        
        self.window.title(f"Snake - Level {self.level} - Score {self.score} - High Score {Game.high_scores[0]}")
    
    def game_loop(self):
        if not self.paused:   # Pause game if paused is True

            # Move the snake
            if not self.snake.move():
                # Open a new window with restart option
                loss_window = tk.Toplevel()
                loss_window.geometry("400x200")  # set width to 300 pixels and height to 200 pixels
                loss_label = tk.Label(loss_window, text="You lost!")
                loss_label.pack()
                restart_button = tk.Button(loss_window, text="Restart", command=self.restart_game)
                restart_button.pack()

                return
            
            # Check if the snake has collided with an obstacle
            if self.snake.check_obstacle(self.obstacle_list):
                # Open a new window with restart option
                loss_window = tk.Toplevel()
                loss_window.geometry("400x200")  # set width to 300 pixels and height to 200 pixels
                loss_label = tk.Label(loss_window, text="You lost!")
                loss_label.pack()
                restart_button = tk.Button(loss_window, text="Restart", command=self.restart_game)
                restart_button.pack()
                return


            # Check if the snake has eaten the food
            if self.snake.check_food(self.food):
                self.snake.grow()
                self.food.move()
                self.update_score()
            
            # Draw the snake, food, and obstacles
            self.canvas.delete("all")
            self.snake.draw()
            self.food.draw()
            for obstacle in self.obstacle_list:
                self.canvas.create_rectangle(obstacle[0], obstacle[1],
                                            obstacle[0]+CELL_SIZE, obstacle[1]+CELL_SIZE,
                                            fill="brown", outline="")
                # obstacle.draw()
            
        # Update the game speed and schedule the next loop iteration
        self.window.after(self.speed, self.game_loop)

    def restart_game(self):
        # Destroy current window
        self.window.destroy()

        # Create new instance of Game class
        new_game = Game()
        
        # Start the game loop
        new_game.game_loop()

game = Game()
game.game_loop()
game.window.mainloop()
