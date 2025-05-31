# 🪐 Asteroids

A classic-style 2D Asteroids game built with Python and [pygame](https://www.pygame.org/).

You control a triangular spaceship that can rotate, move, and shoot bullets. Destroy large asteroids to split them into smaller, faster ones — and survive as long as you can!

---

## 🎮 Features

- Smooth player movement (WASD)
- Rotational shooting with spacebar
- Bullet cooldown system
- Circle-based collision detection
- Asteroids split into smaller ones when hit
- Clean object-oriented design using `pygame.sprite.Group`

---

## 📸 Screenshots

![Gameplay Screenshot](/screenshot.png)

---

## 🚀 How to Run

### Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies:

```bash
pip install -r requirements.txt
```

### Run the game:

```bash
python3 main.py
```

---

## 🧠 Built With

- Python 3
- [pygame](https://www.pygame.org/)
- OOP + `pygame.sprite.Group` for game logic
- Vim, VS Code, and good old terminal

---

## 📁 Project Structure

```
Asteroids/
├── asteroid.py
├── asteroidfield.py
├── circleshape.py
├── constants.py
├── main.py
├── player.py
├── shot.py
└── README.md
```

---

## 💡 Future Ideas

- Add scoring system
- Add player lives and respawn
- Screen wrapping
- Sound effects and music
- UI overlays

---

## 📜 License

MIT (or any license you choose)

---

## 🙌 Author

**Chester Cai**  
[GitHub](https://github.com/ChesterCaii)
