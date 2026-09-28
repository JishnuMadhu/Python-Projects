RARITY_DATA = {
    "Common": {
        "defense_multiplier": 1.0,
        "hp_bonus": 10,
        "mana_bonus": 5,
        "crit_resistance": 2
    },
    "Uncommon": {
        "defense_multiplier": 1.1,
        "hp_bonus": 20,
        "mana_bonus": 10,
        "crit_resistance": 4
    },
    "Rare": {
        "defense_multiplier": 1.3,
        "hp_bonus": 35,
        "mana_bonus": 15,
        "crit_resistance": 6
    },
    "Super Rare": {
        "defense_multiplier": 1.5,
        "hp_bonus": 50,
        "mana_bonus": 20,
        "crit_resistance": 8
    },
    "Epic": {
        "defense_multiplier": 1.8,
        "hp_bonus": 70,
        "mana_bonus": 30,
        "crit_resistance": 12
    },
    "Mythical": {
        "defense_multiplier": 2.2,
        "hp_bonus": 100,
        "mana_bonus": 40,
        "crit_resistance": 18
    },
    "Legendary": {
        "defense_multiplier": 2.8,
        "hp_bonus": 150,
        "mana_bonus": 60,
        "crit_resistance": 25
    }
}


ARMOR_DATA = {

    # Common
    "Leather Armor": {
        "rarity": "Common",
        "defense": 5,
        "price": 20,
        "required_level": 1
    },
    "Cloth Robe": {
        "rarity": "Common",
        "defense": 4,
        "price": 20,
        "required_level": 1
    },

    # Uncommon
    "Iron Armor": {
        "rarity": "Uncommon",
        "defense": 10,
        "price": 50,
        "required_level": 2
    },
    "Hunter Armor": {
        "rarity": "Uncommon",
        "defense": 9,
        "price": 55,
        "required_level": 3
    },

    # Rare
    "Steel Armor": {
        "rarity": "Rare",
        "defense": 15,
        "price": 100,
        "required_level": 5
    },
    "Knight Armor": {
        "rarity": "Rare",
        "defense": 17,
        "price": 120,
        "required_level": 5
    },

    # Super Rare
    "Shadow Armor": {
        "rarity": "Super Rare",
        "defense": 20,
        "price": 160,
        "required_level": 8
    },
    "Guardian Armor": {
        "rarity": "Super Rare",
        "defense": 22,
        "price": 180,
        "required_level": 8
    },

    # Epic
    "Flame Armor": {
        "rarity": "Epic",
        "defense": 25,
        "price": 250,
        "required_level": 10
    },
    "Dragon Armor": {
        "rarity": "Epic",
        "defense": 28,
        "price": 300,
        "required_level": 12
    },

    # Mythical
    "Demon Armor": {
        "rarity": "Mythical",
        "defense": 35,
        "price": 400,
        "required_level": 15
    },

    # Legendary
    "Celestial Armor": {
        "rarity": "Legendary",
        "defense": 40,
        "price": 550,
        "required_level": 20
    },
    "Ancient Armor": {
        "rarity": "Legendary",
        "defense": 45,
        "price": 700,
        "required_level": 25
    }
}


class Armor:

    def __init__(self, armor_name):

        self.armor_name = armor_name

        data = ARMOR_DATA[armor_name]

        self.rarity = data["rarity"]
        self.base_defense = data["defense"]
        self.price = data["price"]
        self.required_level = data["required_level"]

        rarity_data = RARITY_DATA[self.rarity]

        self.defense_multiplier = rarity_data["defense_multiplier"]
        self.hp_bonus = rarity_data["hp_bonus"]
        self.mana_bonus = rarity_data["mana_bonus"]
        self.crit_resistance = rarity_data["crit_resistance"]

        self.defense = int(self.base_defense * self.defense_multiplier)