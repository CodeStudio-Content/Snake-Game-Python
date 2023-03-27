<h1 align="center"> Snake Game 🐍 </h1>

## About:

This is a Python program that implements the classic Snake game using the tkinter library for creating the graphical user interface. It uses the Canvas widget to draw the game board, snake, food, and obstacles.

The `Snake class` holds information about the snake such as its position, body segments, direction, and color. It also has methods for moving the snake, changing its direction, drawing it on the canvas, checking if it has collided with an obstacle or eaten the food, and growing by one segment.

The `Food class` holds information about the food such as its position, color, and methods for moving it to a new location, and drawing it on the canvas.

The `Obstacle class` holds information about the obstacles in the game. Similar to the food, the obstacle has methods for moving it to a new location and drawing it on the canvas.

The `Game class` is the main controller class that initializes the canvas, the snake, the food, the obstacles and updates the score, and the level of the game dynamically throughout the game play. The Game class also contains the game loop which updates the game screen at a certain interval of time using the tkinter after() method. It also has a method for restarting the game.

The code only runs when executed directly, it creates an instance of the Game class and calls its game_loop() method.

