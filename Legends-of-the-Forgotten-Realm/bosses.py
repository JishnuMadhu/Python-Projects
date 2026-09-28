BOSS_DATA = {

    10: {
        "name": "Goblin King",
        "hp": 400,
        "attack": 45,
        "defense": 25,
        "experience": 300,
        "gold": 200
    },

    20: {
        "name": "Forest Guardian",
        "hp": 600,
        "attack": 60,
        "defense": 40,
        "experience": 500,
        "gold": 350
    },

    30: {
        "name": "Ancient Golem",
        "hp": 850,
        "attack": 75,
        "defense": 55,
        "experience": 700,
        "gold": 500
    },

    40: {
        "name": "Vampire Lord",
        "hp": 1100,
        "attack": 90,
        "defense": 65,
        "experience": 900,
        "gold": 650
    },

    50: {
        "name": "Dragon Rider",
        "hp": 1400,
        "attack": 110,
        "defense": 80,
        "experience": 1100,
        "gold": 800
    },

    60: {
        "name": "Demon General",
        "hp": 1700,
        "attack": 130,
        "defense": 95,
        "experience": 1300,
        "gold": 950
    },

    70: {
        "name": "Ice Titan",
        "hp": 2000,
        "attack": 150,
        "defense": 110,
        "experience": 1500,
        "gold": 1100
    },

    80: {
        "name": "Shadow Emperor",
        "hp": 2300,
        "attack": 170,
        "defense": 125,
        "experience": 1700,
        "gold": 1250
    },

    90: {
        "name": "Celestial Dragon",
        "hp": 2600,
        "attack": 190,
        "defense": 140,
        "experience": 1900,
        "gold": 1400
    },

    100: {
        "name": "Ancient Demon King",
        "hp": 3000,
        "attack": 220,
        "defense": 160,
        "experience": 2500,
        "gold": 2000
    }
}


class Boss:

    def __init__(self, level):

        if level not in BOSS_DATA:
            raise ValueError("No boss exists at this level!")

        data = BOSS_DATA[level]

        self.name = data["name"]
        self.level = level

        self.max_hp = data["hp"]
        self.hp = self.max_hp

        self.attack = data["attack"]
        self.defense = data["defense"]

        self.experience = data["experience"]
        self.gold = data["gold"]

        self.is_boss = True

    def display_stats(self):

        print("\n========== BOSS ==========")
        print(f"Name: {self.name}")
        print(f"Level: {self.level}")
        print(f"HP: {self.hp}/{self.max_hp}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")
        print(f"Experience: {self.experience}")
        print(f"Gold: {self.gold}")
        print("==========================")


def is_boss_level(level):
    return level in BOSS_DATA


def get_boss(level):

    if not is_boss_level(level):
        return None

    return Boss(level)
