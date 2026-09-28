# Legends of the Forgotten Realm ⚔️

An epic, modular, text-based RPG developed in Python. Explore dangerous lands, battle ferocious enemies, conquer legendary bosses, upgrade equipment across 7 rarity tiers, and save your journey with JSON persistence.

---

## 🌟 Game Features

- **4 Unique Player Classes:** Warrior, Mage, Archer, and Assassin, each with tailored base statistics (HP, Mana, Attack, Defense, Critical Chance).
- **16 Class Skills:** 4 distinct abilities per class featuring custom mana costs, damage calculations, and visual combat feedback.
- **21 Weapons & 13 Armors:** Fully integrated across **7 Rarity Tiers** (*Common, Uncommon, Rare, Super Rare, Epic, Mythical, Legendary*) with progressive stat multipliers and level requirements.
- **15 Potions:** Health restoration, Mana restoration, Full Recovery, and combat stat boosters (Attack, Defense, Critical Chance).
- **25 Scaled Enemies:** Ranging from Goblins and Wolves to Fire Demons and Sky Harpies, dynamically scaling health, damage, and rewards by player level.
- **10 Milestone Bosses:** From the Goblin King (Lv. 10) to the Ancient Demon King (Lv. 100) featuring 3-turn special attack rotations and healing.
- **10 World Regions:** Progressive world exploration from the quiet Village to the treacherous Demon Realm.
- **Comprehensive Shop System:** Buy weapons, armors, and potions, or sell unwanted inventory items for 50% gold value.
- **Weighted Loot System:** Rarity-based loot drops upon defeating enemies, with bosses guaranteeing **Rare or better** drops.
- **JSON Persistence:** Seamless `Save Game` and `Continue` system serializing complete player state, equipment, inventories, and progression.
- **Game Over & Victory System:** Revive, reload, or return to menu upon defeat, and conquer the Ancient Demon King for the ultimate victory screen.

---

## 📁 System Architecture

| File | Purpose |
| :--- | :--- |
| `main.py` | Main game loop, character creation, exploration, game menu, and victory handling |
| `player.py` | `Player` class, stats, level-up calculations, equipment handling, and inventory menu |
| `combat.py` | Turn-based combat engine, 8 battle actions, boss special attacks, and rewards |
| `skills.py` | Skill database (16 skills) and `use_skill` execution logic |
| `weapons.py` | 21 weapons, rarity multipliers, and `Weapon` class |
| `armor.py` | 13 armors, rarity multipliers, stat bonuses, and `Armor` class |
| `potions.py` | 15 potion types, values, prices, and `Potion` class |
| `enemy.py` | 25 enemies, level range mappings, dynamic level scaling, and `Enemy` class |
| `bosses.py` | 10 milestone bosses, stats, and `Boss` class |
| `world.py` | 10 regions, level ranges, boss prerequisites, and world display |
| `shop.py` | Buying and selling weapons, armors, and potions |
| `loot.py` | Weighted drop chances, enemy loot generation, and boss Rare+ loot |
| `save_load.py` | JSON serialization (`save_game`) and deserialization (`load_game`) |

---

## 🗺️ World & Boss Milestones

| Region | Level Range | Unlock Prerequisite | Boss Encounter |
| :--- | :---: | :--- | :--- |
| **Village** | 1 – 9 | None (Starting Area) | — |
| **Forest** | 1 – 10 | None | Goblin King (Lv. 10) |
| **Cave** | 11 – 20 | Defeat Goblin King | Forest Guardian (Lv. 20) |
| **Desert** | 21 – 30 | Defeat Forest Guardian | Ancient Golem (Lv. 30) |
| **Ruins** | 31 – 40 | Defeat Ancient Golem | Vampire Lord (Lv. 40) |
| **Castle** | 41 – 50 | Defeat Vampire Lord | Dragon Rider (Lv. 50) |
| **Volcano** | 51 – 60 | Defeat Dragon Rider | Demon General (Lv. 60) |
| **Frozen Mountain** | 61 – 70 | Defeat Demon General | Ice Titan (Lv. 70) |
| **Sky Temple** | 71 – 80 | Defeat Ice Titan | Shadow Emperor (Lv. 80) |
| **Demon Realm** | 81 – 100 | Defeat Shadow Emperor | Celestial Dragon (Lv. 90) & Ancient Demon King (Lv. 100) |

---

## ⚔️ Player Classes & Starting Attributes

| Class | HP | Mana | Attack | Defense | Crit Chance |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Warrior** | 150 | 50 | 30 | 25 | 10% |
| **Mage** | 90 | 180 | 45 | 10 | 15% |
| **Archer** | 110 | 80 | 40 | 15 | 25% |
| **Assassin** | 80 | 100 | 35 | 8 | 35% |

---

## 💎 Rarity Tiers & Multipliers

| Rarity | Drop Chance | Damage Multiplier | Defense Multiplier |
| :--- | :---: | :---: | :---: |
| **Common** | 50.0% | 1.0x | 1.0x |
| **Uncommon** | 25.0% | 1.2x | 1.2x |
| **Rare** | 15.0% | 1.5x | 1.5x |
| **Super Rare** | 6.0% | 1.8x | 1.8x |
| **Epic** | 3.0% | 2.2x | 2.2x |
| **Mythical** | 0.9% | 2.5x | 2.5x |
| **Legendary** | 0.1% | 2.8x | 2.8x |

*Bosses exclusively drop **Rare**, **Super Rare**, **Epic**, **Mythical**, or **Legendary** equipment.*

---

## 🚀 How to Run

### Requirements
- Python 3.10+ (tested on Python 3.14)
- Standard library modules only (`json`, `random`, `sys`, `os`)

### Launch the Game
Open a terminal in the project directory:

```bash
python main.py
```

### Controls & Navigation
- Input the corresponding number (e.g., `1`, `2`, `3`) at any prompt.
- Save your progress anytime from the Game Menu (`6. Save Game`).
- Resume your adventure from the Main Menu (`2. Continue`).
