import random

SKILLS = {
    "Warrior": {
        "Slash": {
            "mana_cost": 0,
            "damage": 20,
            "required_level": 1
        },
        "Shield Bash": {
            "mana_cost": 10,
            "damage": 15,
            "required_level": 5
        },
        "Rage": {
            "mana_cost": 15,
            "damage": 25,
            "required_level": 10
        },
        "Earthquake": {
            "mana_cost": 30,
            "damage": 40,
            "required_level": 15
        }
    },

    "Mage": {
        "Fireball": {
            "mana_cost": 10,
            "damage": 25,
            "required_level": 1
        },
        "Ice Blast": {
            "mana_cost": 15,
            "damage": 30,
            "required_level": 5
        },
        "Thunder Strike": {
            "mana_cost": 25,
            "damage": 45,
            "required_level": 10
        },
        "Meteor": {
            "mana_cost": 40,
            "damage": 60,
            "required_level": 15
        }
    },

    "Archer": {
        "Multi Shot": {
            "mana_cost": 10,
            "damage": 25,
            "required_level": 1
        },
        "Poison Arrow": {
            "mana_cost": 15,
            "damage": 30,
            "required_level": 5
        },
        "Explosive Arrow": {
            "mana_cost": 25,
            "damage": 45,
            "required_level": 10
        },
        "Sniper Shot": {
            "mana_cost": 35,
            "damage": 60,
            "required_level": 15
        }
    },

    "Assassin": {
        "Backstab": {
            "mana_cost": 10,
            "damage": 30,
            "required_level": 1
        },
        "Smoke Bomb": {
            "mana_cost": 15,
            "damage": 20,
            "required_level": 5
        },
        "Shadow Strike": {
            "mana_cost": 25,
            "damage": 45,
            "required_level": 10
        },
        "Instant Kill": {
            "mana_cost": 50,
            "damage": 80,
            "required_level": 15,
            "instant_kill_chance": 0.08
        }
    }
}


def get_unlocked_skills(player):
    class_skills = SKILLS[player.character_class]
    unlocked = {}
    for skill_name, data in class_skills.items():
        if player.level >= data["required_level"]:
            unlocked[skill_name] = data
    return unlocked


def use_skill(player, enemy):

    class_skills = SKILLS[player.character_class]

    print("\n===== SKILLS =====")

    skill_names = list(class_skills.keys())

    for i, skill_name in enumerate(skill_names, start=1):
        skill = class_skills[skill_name]
        status = "[Unlocked]" if player.level >= skill["required_level"] else f"[Locked - Level {skill['required_level']}]"
        print(f"{i}. {skill_name:<16} | Mana: {skill['mana_cost']:<2} | Damage: {skill['damage']:<2} {status}")

    try:
        choice = int(input("\nChoose a skill: "))

        if choice < 1 or choice > len(skill_names):
            print("Invalid choice!")
            return False

        skill_name = skill_names[choice - 1]
        skill = class_skills[skill_name]

        if player.level < skill["required_level"]:
            print(f"\n{skill_name} is locked! Requires Level {skill['required_level']}.")
            return False

        if player.mana < skill["mana_cost"]:
            print("\nNot enough mana!")
            return False

        player.mana -= skill["mana_cost"]

        # Check for Assassin Instant Kill chance
        is_instant_kill = False
        if skill_name == "Instant Kill":
            # 8% chance against normal enemies, 4% against bosses
            chance = 0.04 if getattr(enemy, "is_boss", False) else skill.get("instant_kill_chance", 0.08)
            if random.random() < chance:
                is_instant_kill = True
                damage = enemy.hp
                print("\n☠️ CRITICAL EXECUTION! Instant Kill triggered!")

        if not is_instant_kill:
            damage = player.attack + skill["damage"] - enemy.defense
            if damage < 0:
                damage = 0

        enemy.hp -= damage

        if enemy.hp < 0:
            enemy.hp = 0

        print(f"\nUsed {skill_name}!")
        print(f"Damage dealt: {damage}")
        print(f"Enemy HP: {enemy.hp}/{enemy.max_hp}")
        print(f"Mana remaining: {player.mana}/{player.max_mana}")
        return True

    except ValueError:
        print("Please enter a number!")
        return False
