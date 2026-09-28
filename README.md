# Python Projects Portfolio

A collection of three Python projects showcasing fundamental programming concepts, database management with SQLite, and turn-based game development.

---

## 📁 Repository Structure

```text
Python-Projects/
├── Tic-Tac-Toe/
│   ├── tictactoe.py
│   └── README.md
│
├── Shopping-DBMS/
│   ├── main.py
│   ├── admin.py
│   ├── customer.py
│   ├── shopping.db
│   └── README.md
│
└── Legends-of-the-Forgotten-Realm/
    ├── main.py
    ├── player.py
    ├── combat.py
    ├── enemy.py
    ├── bosses.py
    ├── weapons.py
    ├── armor.py
    ├── potions.py
    ├── skills.py
    ├── shop.py
    ├── world.py
    ├── loot.py
    ├── save_load.py
    ├── README.md
    └── .gitignore
```

---

## 🎮 1. Tic-Tac-Toe (`Tic-Tac-Toe/`)
A classic 2-player turn-based console game.
- **Key Features**: Symbol selection (X/O), 3x3 interactive board, move validation, win & draw detection, rematch option, friendly exit message.
- **How to run**:
  ```bash
  cd Tic-Tac-Toe
  python tictactoe.py
  ```

---

## 🛒 2. Shopping System DBMS (`Shopping-DBMS/`)
A command-line e-commerce store backed by a SQLite database.
- **Key Features**: User authentication, separate Admin & Customer roles, complete CRUD operations for products, category management, order placement, order status updates, and enforced foreign key constraints.
- **How to run**:
  ```bash
  cd Shopping-DBMS
  python main.py
  ```

---

## ⚔️ 3. Legends of the Forgotten Realm (`Legends-of-the-Forgotten-Realm/`)
A full-featured turn-based fantasy RPG console game.
- **Key Features**: 
  - 4 character classes (Warrior, Mage, Archer, Assassin)
  - Level progression from Level 1 to 100 with milestone boss level caps
  - 25+ regular enemies and 10 milestone bosses
  - Weapon & Armor equipment system with 7 rarity tiers
  - 15 potions (Health, Mana, Mixed, and temporary Buffs)
  - Skill unlock progression & passive stat bonuses every 5 levels
  - Full inventory management (Equip, Unequip, Use, Drop)
  - Town shop to buy and sell gear
  - 10 unlockable regions with boss prerequisites
  - JSON game save and load persistence
  - Victory and Game Over screens with final score and play time tracking
- **How to run**:
  ```bash
  cd Legends-of-the-Forgotten-Realm
  python main.py
  ```
