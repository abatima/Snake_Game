# Snake Game 🐍

## <img width="601" height="632" alt="image" src="https://github.com/user-attachments/assets/162f66dc-d982-4640-ac52-d0f21976eafd" />


A polished, object-oriented implementation of the classic Snake arcade game using Python and Turtle. Featuring high-score persistence, improved collision physics, and a modular architecture that separates snake behavior, food mechanics, and UI management.

## 🎮 Features

* **Persistent High Scores:** Your best score is now saved to a local data file, allowing you to track progress over time.
* **Modular OOP Design:** Separate classes for the snake, food, and scoreboard ensure clean, maintainable code.
* **Dynamic Snake Growth:** The snake body expands and speeds up as you consume food.
* **Boundary & Tail Detection:** Enhanced collision logic detects both wall hits and self-collisions to trigger game-over states.
* **Smooth Refresh Rates:** Optimized using `screen.tracer(0)` and `screen.update()` for flicker-free gameplay.

## 🛠️ Built With

* [Python 3](https://www.python.org/)
* `turtle` module (built-in Python graphics)

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3.x installed. You can check your version by running:

```bash
python --version

```

### Installation

1. Clone the repository:
```bash
git clone https://github.com/abatima/Snake_Game.git

```


2. Navigate to the project directory:
```bash
cd Snake_Game

```



### Running the Game

Launch the game by running the main script:

```bash
python main.py

```

## 🕹️ How to Play

Navigate the snake to eat the food and grow as long as possible. The game ends if you hit the wall or your own tail.

### Controls

Use the **Arrow Keys** to navigate:

* **Up Arrow:** North
* **Down Arrow:** South
* **Left Arrow:** West
* **Right Arrow:** East

## 📂 File Structure

* `main.py`: The entry point that initializes the game loop and manages screen refreshes.
* `snake.py`: Manages the snake's segments, movement directions, and body extension logic.
* `food.py`: Handles the randomized spawning of food items on the grid.
* `scoreboard.py`: Manages the UI, current score tracking, and data persistence for high scores.
* `data.txt`: A local file used to store and retrieve your all-time high score.

## 📜 License

This project is open-source and available under the [MIT License](https://en.wikipedia.org/wiki/MIT_License).

---

*Created by [abatima*](https://github.com/abatima)
