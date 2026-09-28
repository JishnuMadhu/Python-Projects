import random

from weapons import WEAPON_DATA, Weapon
from armor import ARMOR_DATA, Armor
from potions import POTION_DATA, Potion


LOOT_RARITY_CHANCES = {
    "Common": 50,
    "Uncommon": 25,
    "Rare": 15,
    "Super Rare": 6,
    "Epic": 3,
    "Mythical": 0.9,
    "Legendary": 0.1
}


BOSS_RARITIES = [
    "Rare",
    "Super Rare",
    "Epic",
    "Mythical",
    "Legendary"
]


def get_random_rarity():

    roll = random.uniform(0, 100)

    cumulative = 0

    for rarity, chance in LOOT_RARITY_CHANCES.items():

        cumulative += chance

        if roll <= cumulative:
            return rarity

    return "Common"


def get_boss_rarity():

    return random.choice(BOSS_RARITIES)


def get_weapon_by_rarity(rarity):

    weapons = []

    for weapon_name, data in WEAPON_DATA.items():

        if data["rarity"] == rarity:
            weapons.append(weapon_name)

    if not weapons:
        return None

    weapon_name = random.choice(weapons)

    return Weapon(weapon_name)


def get_armor_by_rarity(rarity):

    armors = []

    for armor_name, data in ARMOR_DATA.items():

        if data["rarity"] == rarity:
            armors.append(armor_name)

    if not armors:
        return None

    armor_name = random.choice(armors)

    return Armor(armor_name)


def get_random_potion():

    potion_name = random.choice(list(POTION_DATA.keys()))

    return Potion(potion_name)


def generate_enemy_loot():

    rarity = get_random_rarity()

    item_type = random.choice([
        "weapon",
        "armor",
        "potion"
    ])

    if item_type == "weapon":

        item = get_weapon_by_rarity(rarity)

        if item:
            return item

    elif item_type == "armor":

        item = get_armor_by_rarity(rarity)

        if item:
            return item

    else:

        return get_random_potion()

    return None


def generate_boss_loot():

    rarity = get_boss_rarity()

    item_type = random.choice([
        "weapon",
        "armor"
    ])

    if item_type == "weapon":

        return get_weapon_by_rarity(rarity)

    return get_armor_by_rarity(rarity)


def give_loot(player, item):

    if item is None:
        print("No loot found.")
        return

    if isinstance(item, Weapon):

        player.add_weapon(item)

        print(
            f"Loot received: {item.weapon_name} "
            f"[{item.rarity}]"
        )

    elif isinstance(item, Armor):

        player.add_armor(item)

        print(
            f"Loot received: {item.armor_name} "
            f"[{item.rarity}]"
        )

    elif isinstance(item, Potion):

        player.add_potion(item)

        print(
            f"Loot received: {item.potion_name}"
        )
