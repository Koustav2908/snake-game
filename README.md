# 🐍 Snake Game

This is a modern implementation of the classic Snake Game using Python's turtle graphics module and Object-Oriented Programming (OOP). The snake moves across the screen, eats food to grow, and the score increases accordingly. The game resets when the snake hits the wall or its own body.

## 🎮 Features

-   Smooth gameplay using turtle and manual screen updates

-   Classic movement controls using arrow keys

-   Snake grows and score increases when it eats food

-   Game resets on collision with wall or self

-   Live score display with automatic reset handling

-   Score saving mode available too, so you wouldn't lose your high score even if you close the application.

## ⌨️ Controls

-   `↑` Up Arrow — Move Up

-   `↓` Down Arrow — Move Down

-   `←` Left Arrow — Move Left

-   `→` Right Arrow — Move Right

-   `Space` — End Game

## 📦 Project Structure

```bash
snake_game/
│
├── main.py               # Main game loop and setup
├── snake.py              # Snake class with movement and collision logic
├── food.py               # Food class that randomly generates food
├── scoreboard.py         # ScoreBoard class to track and show score
└── colors.py             # Configuration file for changing colors
```

## 🚀 How to Run

1. Clone the repository or download the files

2. Make sure Python 3 is installed

3. Install the turtle module if not already present (usually comes by default)

4. Run the game:

```bash
python main.py
```

## 🛠️ Technologies Used

-   Python 3

-   `turtle` module for graphics

-   Object-Oriented Programming (OOP)

## 🧠 Game Logic Overview

-   The snake is made up of segments that move forward each frame

-   When the snake collides with the food (within 15 pixels), it:

    -   Extends by one segment

    -   Refreshes the food in a random location

    -   Increments the score

-   If the snake touches the wall or its own body:

    -   The game resets by clearing the snake and resetting the score

Enjoy the game and happy coding!
