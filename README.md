<h1 align="center"> Snake Game 🐍 🎮 </h1>

| <img src="https://user-images.githubusercontent.com/77020164/228026834-cd93f2d2-d3cb-45cc-97c3-bc10c881fbfb.png" width="500" height="400"/> | ![Screenshot from 2023-03-27 19-48-30](https://user-images.githubusercontent.com/77020164/228026890-fcde6a84-0528-4260-a744-ca906087e5ce.png)
|-|-|




## About:

This is a Python program that implements the classic Snake game using the tkinter library for creating the graphical user interface. It uses the Canvas widget to draw the game board, snake, food, and obstacles.

The `Snake class` holds information about the snake such as its position, body segments, direction, and color. It also has methods for moving the snake, changing its direction, drawing it on the canvas, checking if it has collided with an obstacle or eaten the food, and growing by one segment.

The `Food class` holds information about the food such as its position, color, and methods for moving it to a new location, and drawing it on the canvas.

The `Obstacle class` holds information about the obstacles in the game. Similar to the food, the obstacle has methods for moving it to a new location and drawing it on the canvas.

The `Game class` is the main controller class that initializes the canvas, the snake, the food, the obstacles and updates the score, and the level of the game dynamically throughout the game play. The Game class also contains the game loop which updates the game screen at a certain interval of time using the tkinter after() method. It also has a method for restarting the game.

The code only runs when executed directly, it creates an instance of the Game class and calls its game_loop() method.

## Requirements
* Python 3.x
* Tkinter library (which is usually included with Python)


## Getting Started
1. Clone this repository to your local machine.
2. Open a terminal window and navigate to the cloned repository.
3. Run the following command to start the program: `python game.py`


## Code Structure

The code is organized into the following functions:
1. Snake class:

* `__init__(self, canvas)`
* `move(self)`
* `change_direction(self, event)`
* `draw(self)`
* `check_food(self, food)`
* `grow(self)`
* `check_obstacle(self, obstacle_list)`


2. Food class:

* `__init__(self, canvas)`
* `move(self)`
* `draw(self)`

3.Obstacle class:

* `__init__(self, canvas)`
* `move(self)`
* `draw(self)`

4. Game class:

* `__init__`
* `toggle_pause(self, event)`
* `setup_obstacles(self)`
* `update_score`
* `game_loop`
* `restart_game`

 


<div align="center">
  
## Made with ❤️ , Python, and Tkinter. Enjoy!
  
</div>

