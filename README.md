# Snake Game 🐍

A modern take on the classic arcade game built using **Python** and the **Turtle** graphics library. This project utilizes object-oriented programming (OOP) to manage the snake's behavior, food generation, and real-time score tracking.

## 🎮 Features

* **Snake Growth:** Every time the snake eats food, it grows longer and the score increases.
* **Collision Detection:** The game detects when the snake hits the wall or its own tail.
* **Randomized Food:** Food spawns at random locations across the screen.
* **Scoreboard & High Score:** Tracks your current score and displays a "Game Over" message upon collision.
* **Smooth Animation:** Uses screen updates and time delays for fluid movement.

## 🛠️ Built With

* [Python 3](https://www.python.org/)
* `turtle` module (built-in Python graphics)

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3.x installed. You can verify this by running:

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

Guide the snake to eat the food and grow as long as possible without hitting the boundaries or yourself.

### Controls

Use the **Arrow Keys** on your keyboard to navigate:

* **Up Arrow:** Move North
* **Down Arrow:** Move South
* **Left Arrow:** Move West
* **Right Arrow:** Move East

## 📂 File Structure

* `main.py`: The core game engine. It manages the screen setup, game loop, and collision logic.
* `snake.py`: Handles the creation of the snake segments, movement logic, and directional constraints.
* `food.py`: A subclass of the Turtle class that manages the food's appearance and random repositioning.
* `scoreboard.py`: Manages the UI, tracks the current score, and handles the "Game Over" state.

## 📜 License

This project is open-source and available under the [MIT License](https://www.google.com/search?q=LICENSE).

## 🤝 Contributing

Feel free to fork this project and submit a pull request! Potential improvements could include adding a "High Score" persistence file (`data.txt`) or different difficulty levels.

---

*Created by [abatima*](https://github.com/abatima)
