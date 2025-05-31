# 🐍 Snake Game using Python and Tkinter

A classic Snake game implemented in Python using the Tkinter GUI library. This interactive game challenges players to control a snake to eat food, grow longer, and avoid colliding with walls or itself.

---

## 🎮 Features

- Simple and intuitive controls (arrow keys)
- Real-time snake movement
- Randomly generated food positions
- Score tracking
- Game Over detection (collision with walls or self)
- Clean GUI using Tkinter Canvas

---

## 📸 Preview

```
![Snake_game_pic](https://github.com/user-attachments/assets/09a88eca-28a2-47be-ae36-99132a35b825)
![Snake_game_over_pic](https://github.com/user-attachments/assets/e7d2c692-c7b8-4efe-a212-58acab26daee)

Use arrow keys to control the snake.
```

---

### How it works:

- The snake is represented as a list of coordinate tuples.
- Food is randomly placed, ensuring it doesn't overlap the snake.
- Each update, the snake's head moves in the current direction.
- Eating food causes the snake to grow by adding a segment.
- The game uses the Tkinter canvas widget for rendering.
- The update loop runs on a timed interval with `root.after()`.

---

## 📚 Learning Objectives

- Working with Tkinter for GUI development in Python.
- Handling keyboard events.
- Using lists and tuples for game state.
- Implementing game logic (collision detection, score keeping).
- Understanding the game loop and timing.
- Basic object movement and growth mechanics.

---

## 📌 Requirements

- Python 3.x
- Tkinter (usually included with Python standard library)

---

## ▶️ How to Run

1. **Clone the repository:**

```bash
git clone https://github.com/Chennakesava9007/snake-game-python.git
cd snake-game-python
```

2. **Run the game:**

```bash
python snake_game.py
```

---

## 🛠 Possible Enhancements

- Add levels or increasing speed over time.
- Add sound effects.
- Implement pause and resume functionality.
- Display high scores with persistent storage.
- Improve graphics and animations.
- Add a start menu and game over screen.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 👨‍💻 Author

- [Kesava](https://github.com/Chennakesava9007)

---

## 💡 Tip

Try modifying the game's speed or the snake's color to personalize your game. This project is great for learning GUI programming fundamentals!
