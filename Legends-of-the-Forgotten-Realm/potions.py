
POTION_DATA = {

    # Health
    "Small Health Potion": {
        "type": "health",
        "value": 50,
        "price": 20
    },
    "Medium Health Potion": {
        "type": "health",
        "value": 100,
        "price": 40
    },
    "Large Health Potion": {
        "type": "health",
        "value": 250,
        "price": 80
    },
    "Giant Health Potion": {
        "type": "health",
        "value": 500,
        "price": 150
    },
    "Ultimate Health Potion": {
        "type": "health",
        "value": "full",
        "price": 250
    },

    # Mana
    "Small Mana Potion": {
        "type": "mana",
        "value": 30,
        "price": 20
    },
    "Medium Mana Potion": {
        "type": "mana",
        "value": 75,
        "price": 40
    },
    "Large Mana Potion": {
        "type": "mana",
        "value": 150,
        "price": 80
    },
    "Giant Mana Potion": {
        "type": "mana",
        "value": 300,
        "price": 150
    },
    "Ultimate Mana Potion": {
        "type": "mana",
        "value": "full",
        "price": 250
    },

    # Mixed
    "Recovery Potion": {
        "type": "mixed",
        "value": 100,
        "price": 100
    },
    "Full Recovery Potion": {
        "type": "mixed",
        "value": "full",
        "price": 300
    },

    # Buffs
    "Attack Boost Potion": {
        "type": "attack_buff",
        "value": 10,
        "duration": 3,
        "price": 100
    },
    "Defense Boost Potion": {
        "type": "defense_buff",
        "value": 10,
        "duration": 3,
        "price": 100
    },
    "Critical Boost Potion": {
        "type": "crit_buff",
        "value": 10,
        "duration": 3,
        "price": 120
    }
}

class Potion:

    def __init__(self, potion_name):

        self.potion_name = potion_name

        data = POTION_DATA[potion_name]

        self.type = data["type"]
        self.value = data["value"]
        self.price = data["price"]

        self.duration = data.get("duration", None)