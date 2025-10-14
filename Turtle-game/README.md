Turtle Crossing Game

This is a Python-based crossing game built using the `turtle` graphics module. The player controls a turtle that must cross a busy road filled with moving cars. The goal is to reach the other side without getting hit.

## How to Play

- Use the **Up Arrow** key to move the turtle forward.
- Each time you reach the top of the screen, you advance to the next level.
- With each new level, the speed of the cars increases.
- The game ends if your turtle collides with a car.

## Features

- Object-oriented structure using multiple classes:
  - `Player`: Controls the turtle and its movement
  - `CarManager`: Generates and moves cars
  - `Scoreboard`: Tracks the level and displays a game-over message
- Collision detection between player and cars
- Dynamic difficulty: car speed increases with each level

## Requirements

- Python 3.x
- No external libraries (uses the built-in `turtle` module and `random`)

## How to Run

1. Clone or download the repository.
2. Run the main file (typically named `main.py` or `crossing_game.py`) using:

```bash
python main.py
