



WEAPON_DATA = {

    # Common
    "Rusty Sword": {
        "rarity": "Common",
        "damage": 5,
        "price": 20,
        "required_level": 1
    },
    "Wooden Bow": {
        "rarity": "Common",
        "damage": 5,
        "price": 20,
        "required_level": 1
    },
    "Apprentice Staff": {
        "rarity": "Common",
        "damage": 6,
        "price": 25,
        "required_level": 1
    },

    # Uncommon
    "Iron Sword": {
        "rarity": "Uncommon",
        "damage": 10,
        "price": 50,
        "required_level": 2
    },
    "Hunter Bow": {
        "rarity": "Uncommon",
        "damage": 11,
        "price": 55,
        "required_level": 2
    },
    "Steel Dagger": {
        "rarity": "Uncommon",
        "damage": 10,
        "price": 55,
        "required_level": 3
    },

    # Rare
    "Steel Sword": {
        "rarity": "Rare",
        "damage": 15,
        "price": 100,
        "required_level": 5
    },
    "Battle Axe": {
        "rarity": "Rare",
        "damage": 17,
        "price": 120,
        "required_level": 5
    },
    "Longbow": {
        "rarity": "Rare",
        "damage": 16,
        "price": 110,
        "required_level": 5
    },

    # Super Rare
    "Knight Sword": {
        "rarity": "Super Rare",
        "damage": 20,
        "price": 160,
        "required_level": 8
    },
    "Shadow Dagger": {
        "rarity": "Super Rare",
        "damage": 21,
        "price": 170,
        "required_level": 8
    },
    "War Bow": {
        "rarity": "Super Rare",
        "damage": 20,
        "price": 165,
        "required_level": 8
    },

    # Epic
    "Flame Blade": {
        "rarity": "Epic",
        "damage": 25,
        "price": 250,
        "required_level": 10
    },
    "Thunder Hammer": {
        "rarity": "Epic",
        "damage": 28,
        "price": 280,
        "required_level": 12
    },
    "Arcane Staff": {
        "rarity": "Epic",
        "damage": 27,
        "price": 270,
        "required_level": 12
    },

    # Mythical
    "Dragon Fang": {
        "rarity": "Mythical",
        "damage": 32,
        "price": 350,
        "required_level": 15
    },
    "Demon Scythe": {
        "rarity": "Mythical",
        "damage": 35,
        "price": 380,
        "required_level": 15
    },
    "Celestial Bow": {
        "rarity": "Mythical",
        "damage": 34,
        "price": 370,
        "required_level": 18
    },

    # Legendary
    "Demon Slayer": {
        "rarity": "Legendary",
        "damage": 40,
        "price": 500,
        "required_level": 20
    },
    "Excalibur": {
        "rarity": "Legendary",
        "damage": 45,
        "price": 650,
        "required_level": 25
    },
    "Soul Reaper": {
        "rarity": "Legendary",
        "damage": 50,
        "price": 750,
        "required_level": 30
    }
}

RARITY_DATA = {
    "Common": {
        "damage_multiplier": 1.0,
        "crit_bonus": 0
    },
    "Uncommon": {
        "damage_multiplier": 1.1,
        "crit_bonus": 2
    },
    "Rare": {
        "damage_multiplier": 1.3,
        "crit_bonus": 5
    },
    "Super Rare": {
        "damage_multiplier": 1.5,
        "crit_bonus": 8
    },
    "Epic": {
        "damage_multiplier": 1.8,
        "crit_bonus": 12
    },
    "Mythical": {
        "damage_multiplier": 2.2,
        "crit_bonus": 18
    },
    "Legendary": {
        "damage_multiplier": 2.8,
        "crit_bonus": 25
    }
}



class Weapon:

    def __init__(self, weapon_name):

        self.weapon_name = weapon_name

        data = WEAPON_DATA[weapon_name]

        self.rarity = data["rarity"]
        self.base_damage = data["damage"]
        self.price = data["price"]
        self.required_level = data["required_level"]

        rarity_data = RARITY_DATA[self.rarity]

        self.damage_multiplier = rarity_data["damage_multiplier"]
        self.crit_bonus = rarity_data["crit_bonus"]

        self.damage = int(self.base_damage * self.damage_multiplier)

#test 
# weapon = Weapon("Rusty Sword")
# print(weapon.weapon_name)
# print(weapon.rarity)
# print(weapon.damage)
# print(weapon.crit_bonus)
# print(weapon.price)
# print(weapon.required_level)
# print(weapon.rarity)
