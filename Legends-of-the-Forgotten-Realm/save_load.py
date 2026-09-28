import json
import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

from player import Player
from weapons import Weapon
from armor import Armor
from potions import Potion

SAVE_FILE = "savegame.json"


def save_game(player, filename=SAVE_FILE):

    data = {
        "name": player.name,
        "player_class": player.player_class,
        "level": player.level,
        "experience": player.experience,
        "hp": player.hp,
        "max_hp": player.max_hp,
        "mana": player.mana,
        "max_mana": player.max_mana,
        "attack": player.attack,
        "defense": player.defense,
        "gold": player.gold,
        "critical_chance": player.critical_chance,
        "critical_damage": player.critical_damage,
        "weapon": player.weapon.weapon_name if player.weapon else None,
        "armor": player.armor.armor_name if player.armor else None,
        "weapons": [w.weapon_name for w in player.weapons],
        "armors": [a.armor_name for a in player.armors],
        "potions": [p.potion_name for p in player.potions],
        "bosses_defeated": player.bosses_defeated,
        "enemies_defeated": player.enemies_defeated,
        "weapons_collected": getattr(player, "weapons_collected", len(player.weapons) + (1 if player.weapon else 0)),
        "rare_items_found": getattr(player, "rare_items_found", 0),
        "play_time_seconds": player.get_total_play_time_seconds() if hasattr(player, "get_total_play_time_seconds") else 0
    }

    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print("\nGame saved successfully!")
        return True
    except Exception as e:
        print(f"\nFailed to save game: {e}")
        return False


def load_game(filename=SAVE_FILE):

    if not os.path.exists(filename):
        print("\nNo save file found!")
        return None

    try:
        with open(filename, "r") as file:
            data = json.load(file)

        player = Player(data["name"], data["player_class"])
        player.level = data["level"]
        player.experience = data["experience"]
        player.max_hp = data["max_hp"]
        player.hp = data["hp"]
        player.max_mana = data["max_mana"]
        player.mana = data["mana"]
        player.attack = data["attack"]
        player.defense = data["defense"]
        player.gold = data["gold"]
        player.critical_chance = data.get("critical_chance", player.critical_chance)
        player.critical_damage = data.get("critical_damage", player.critical_damage)

        # Equipped items
        if data.get("weapon"):
            player.weapon = Weapon(data["weapon"])
        if data.get("armor"):
            player.armor = Armor(data["armor"])

        # Inventory
        player.weapons = [Weapon(w_name) for w_name in data.get("weapons", [])]
        player.armors = [Armor(a_name) for a_name in data.get("armors", [])]
        player.potions = [Potion(p_name) for p_name in data.get("potions", [])]

        # Progression
        player.bosses_defeated = data.get("bosses_defeated", [])
        player.enemies_defeated = data.get("enemies_defeated", 0)

        # Stats tracking
        player.weapons_collected = data.get("weapons_collected", len(player.weapons) + (1 if player.weapon else 0))
        player.rare_items_found = data.get("rare_items_found", 0)
        player.play_time_seconds = data.get("play_time_seconds", 0)

        print(f"\nWelcome back, {player.name}! Game loaded successfully.")
        return player

    except Exception as e:
        print(f"\nError loading save file: {e}")
        return None


def has_save_file(filename=SAVE_FILE):
    return os.path.exists(filename)
