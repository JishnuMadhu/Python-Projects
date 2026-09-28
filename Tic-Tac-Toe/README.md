# Tic-Tac-Toe (2-Player Console Game)

A classic 2-player turn-based Tic-Tac-Toe console game implemented in Python.

---

## 🎮 Features
- **Interactive 3x3 Board**: Clear grid display with numeric cell indexing (1–9).
- **Symbol Selection**: Player 1 can select their preferred symbol (`X` or `O`), automatically assigning the opposite symbol to Player 2.
- **Turn Alternation**: Clean turn-by-turn prompts announcing the active player and their symbol.
- **Input Validation**: Robust validation preventing crashes from non-numeric input, out-of-range choices (< 1 or > 9), and moves on already occupied cells.
- **Win & Draw Detection**: Instant detection for horizontal, vertical, and diagonal lines, as well as full-board tie games.
- **Rematch Loop**: Prompt to play again without needing to restart the script.
- **Friendly Exit**: Graceful closing message upon exiting.

---

## 🚀 How to Run

### Prerequisites
- Python 3.7 or higher installed on your system.

### Running the Game
Open your terminal or command prompt, navigate to the `projects` directory, and run:

```bash
python tictactoe.py
```

---

## 🕹️ Controls & Gameplay
1. **Choose Symbol**: Player 1 enters `X` or `O`.
2. **Make a Move**: Players take turns choosing a cell number from `1` to `9`:

```text
 1 | 2 | 3 
---+---+---
 4 | 5 | 6 
---+---+---
 7 | 8 | 9 
```

3. **Win / Draw**: The game announces the winner or declares a draw when all 9 cells are filled.
4. **Rematch**: Enter `y` to play another round, or `n` to exit.
