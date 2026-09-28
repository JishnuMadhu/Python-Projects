from bosses import get_boss, is_boss_level

REGIONS = {
    "Village": {
        "min_level": 1,
        "max_level": 9,
        "boss_level": None
    },

    "Forest": {
        "min_level": 1,
        "max_level": 10,
        "boss_level": 10
    },

    "Cave": {
        "min_level": 11,
        "max_level": 20,
        "boss_level": 20
    },

    "Desert": {
        "min_level": 21,
        "max_level": 30,
        "boss_level": 30
    },

    "Ruins": {
        "min_level": 31,
        "max_level": 40,
        "boss_level": 40
    },

    "Castle": {
        "min_level": 41,
        "max_level": 50,
        "boss_level": 50
    },

    "Volcano": {
        "min_level": 51,
        "max_level": 60,
        "boss_level": 60
    },

    "Frozen Mountain": {
        "min_level": 61,
        "max_level": 70,
        "boss_level": 70
    },

    "Sky Temple": {
        "min_level": 71,
        "max_level": 80,
        "boss_level": 80
    },

    "Demon Realm": {
        "min_level": 81,
        "max_level": 100,
        "boss_level": 100
    }
}


def get_region(player_level):

    for region, data in REGIONS.items():

        if data["min_level"] <= player_level <= data["max_level"]:
            return region

    return None


REGION_PREREQUISITES = {
    "Village": None,
    "Forest": None,
    "Cave": "Goblin King",
    "Desert": "Forest Guardian",
    "Ruins": "Ancient Golem",
    "Castle": "Vampire Lord",
    "Volcano": "Dragon Rider",
    "Frozen Mountain": "Demon General",
    "Sky Temple": "Ice Titan",
    "Demon Realm": "Shadow Emperor"
}


def is_region_unlocked(player_or_level, region):

    if region not in REGIONS:
        return False

    prereq_boss = REGION_PREREQUISITES.get(region)

    if hasattr(player_or_level, "bosses_defeated"):
        if prereq_boss is None:
            return True
        return prereq_boss in player_or_level.bosses_defeated

    return player_or_level >= REGIONS[region]["min_level"]


def get_region_boss_level(region):

    if region not in REGIONS:
        return None

    return REGIONS[region]["boss_level"]


def display_world(player_or_level):

    print("\n========== WORLD ==========")

    for region, data in REGIONS.items():

        if is_region_unlocked(player_or_level, region):
            status = "Unlocked"
        else:
            status = "Locked"

        print(
            f"{region:<18} "
            f"Level {data['min_level']:<3} "
            f"- {data['max_level']:<3} "
            f"[{status}]"
        )

    print("===========================")


def get_current_region_boss(player_level):

    if is_boss_level(player_level):
        return get_boss(player_level)

    return None
