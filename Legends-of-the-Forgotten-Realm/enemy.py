import random


ENEMY_DATA = {

    #  Level 1–10
    "Goblin": {
        "hp": 40,
        "attack": 10,
        "defense": 5,
        "experience": 20,
        "gold": 10
    },

    "Wolf": {
        "hp": 35,
        "attack": 15,
        "defense": 3,
        "experience": 25,
        "gold": 12
    },

    "Slime": {
        "hp": 50,
        "attack": 8,
        "defense": 8,
        "experience": 20,
        "gold": 8
    },

    "Zombie": {
        "hp": 60,
        "attack": 12,
        "defense": 10,
        "experience": 30,
        "gold": 15
    },

    "Skeleton": {
        "hp": 45,
        "attack": 14,
        "defense": 7,
        "experience": 28,
        "gold": 13
    },


    # Level 11–20

    "Orc": {
        "hp": 90,
        "attack": 22,
        "defense": 15,
        "experience": 50,
        "gold": 25
    },

    "Bandit": {
        "hp": 75,
        "attack": 25,
        "defense": 10,
        "experience": 45,
        "gold": 30
    },

    "Troll": {
        "hp": 120,
        "attack": 20,
        "defense": 20,
        "experience": 60,
        "gold": 28
    },

    "Dark Archer": {
        "hp": 70,
        "attack": 28,
        "defense": 8,
        "experience": 55,
        "gold": 32
    },

    "Giant Spider": {
        "hp": 85,
        "attack": 24,
        "defense": 12,
        "experience": 52,
        "gold": 27
    },


    # Level 21–30 

    "Vampire": {
        "hp": 150,
        "attack": 32,
        "defense": 18,
        "experience": 80,
        "gold": 45
    },

    "Werewolf": {
        "hp": 140,
        "attack": 38,
        "defense": 15,
        "experience": 85,
        "gold": 50
    },

    "Necromancer": {
        "hp": 110,
        "attack": 40,
        "defense": 12,
        "experience": 90,
        "gold": 55
    },

    "Ice Golem": {
        "hp": 200,
        "attack": 30,
        "defense": 30,
        "experience": 100,
        "gold": 60
    },

    "Fire Demon": {
        "hp": 170,
        "attack": 42,
        "defense": 20,
        "experience": 110,
        "gold": 65
    },

    # Level 31–40
    "Sand Wraith": {
        "hp": 180,
        "attack": 45,
        "defense": 22,
        "experience": 120,
        "gold": 70
    },
    "Scorpion": {
        "hp": 160,
        "attack": 48,
        "defense": 18,
        "experience": 115,
        "gold": 68
    },
    "Mummy": {
        "hp": 200,
        "attack": 40,
        "defense": 28,
        "experience": 125,
        "gold": 75
    },
    "Stone Guardian": {
        "hp": 250,
        "attack": 38,
        "defense": 40,
        "experience": 140,
        "gold": 80
    },
    "Dark Knight": {
        "hp": 220,
        "attack": 50,
        "defense": 35,
        "experience": 150,
        "gold": 85
    },

    # Level 41–50
    "Lava Beast": {
        "hp": 280,
        "attack": 55,
        "defense": 30,
        "experience": 160,
        "gold": 90
    },
    "Flame Serpent": {
        "hp": 240,
        "attack": 60,
        "defense": 25,
        "experience": 155,
        "gold": 95
    },
    "Frost Wolf": {
        "hp": 260,
        "attack": 52,
        "defense": 32,
        "experience": 165,
        "gold": 100
    },
    "Ice Witch": {
        "hp": 230,
        "attack": 65,
        "defense": 28,
        "experience": 170,
        "gold": 105
    },
    "Sky Harpy": {
        "hp": 210,
        "attack": 68,
        "defense": 24,
        "experience": 175,
        "gold": 110
    }
}

ENEMY_RANGES = {
    (1, 10): [
        "Goblin",
        "Wolf",
        "Slime",
        "Zombie",
        "Skeleton"
    ],

    (11, 20): [
        "Orc",
        "Bandit",
        "Troll",
        "Dark Archer",
        "Giant Spider"
    ],

    (21, 30): [
        "Vampire",
        "Werewolf",
        "Necromancer",
        "Ice Golem",
        "Fire Demon"
    ],

    (31, 40): [
        "Sand Wraith",
        "Scorpion",
        "Mummy",
        "Stone Guardian",
        "Dark Knight"
    ],

    (41, 50): [
        "Lava Beast",
        "Flame Serpent",
        "Frost Wolf",
        "Ice Witch",
        "Sky Harpy"
    ],

    (51, 60): [
        "Lava Beast",
        "Flame Serpent",
        "Fire Demon",
        "Troll",
        "Orc"
    ],

    (61, 70): [
        "Frost Wolf",
        "Ice Witch",
        "Ice Golem",
        "Dark Knight",
        "Werewolf"
    ],

    (71, 80): [
        "Sky Harpy",
        "Dark Archer",
        "Stone Guardian",
        "Sand Wraith",
        "Dark Knight"
    ],

    (81, 100): [
        "Vampire",
        "Necromancer",
        "Fire Demon",
        "Ice Golem",
        "Dark Knight"
    ]
}


def get_random_enemy(player_level):

    for level_range, enemies in ENEMY_RANGES.items():
        min_level, max_level = level_range

        if min_level <= player_level <= max_level:
            enemy_name = random.choice(enemies)
            return Enemy(enemy_name, player_level)

    # Fallback for levels beyond 100 or edge cases:
    highest_tier_enemies = ENEMY_RANGES.get((81, 100), list(ENEMY_DATA.keys()))
    enemy_name = random.choice(highest_tier_enemies)
    return Enemy(enemy_name, player_level)



class Enemy:

    def __init__(self, name, level):

        self.name = name
        self.level = level

        self.enemy_stats = ENEMY_DATA[name]

        self.level_scaling = 1 + (level - 1) * 0.10  #factor with which enemy stats increases by level by 10%


        self.hp = int(self.enemy_stats["hp"] * self.level_scaling)
        self.max_hp = self.hp

        self.attack = int(self.enemy_stats["attack"] * self.level_scaling)
        self.defense = int(self.enemy_stats["defense"] * self.level_scaling)

        reward_scaling = 1 + (level - 1) * 0.05  #factor with which enemy rewards increases by level by 5%

        self.experience_reward = int(self.enemy_stats['experience'] * reward_scaling)
        self.gold_reward = int(self.enemy_stats['gold'] * reward_scaling)
        self.experience = self.experience_reward
        self.gold = self.gold_reward


#test
# enemy = Enemy("Goblin", 99)

# print(enemy.name)
# print(enemy.level)
# print(enemy.hp)
# print(enemy.max_hp)
# print(enemy.attack)
# print(enemy.defense)
# print(enemy.experience_reward)
# print(enemy.gold_reward)

# print(ENEMY_DATA['Orc'])
# print()
# print(ENEMY_RANGES[(21,30)])


#test 
# print(get_random_enemy(9))