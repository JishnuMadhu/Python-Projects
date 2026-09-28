# Player Class
import time
from weapons import Weapon

CLASS_STATS = {
    "Warrior": {
        "max_hp": 150,
        "max_mana": 50,
        "attack": 30,
        "defense": 25,
        "critical_chance": 10
    },

    "Mage": {
        "max_hp": 100,
        "max_mana": 150,
        "attack": 35,
        "defense": 10,
        "critical_chance": 15
    },

    "Archer": {
        "max_hp": 110,
        "max_mana": 100,
        "attack": 25,
        "defense": 15,
        "critical_chance": 25
    },

    "Assassin": {
        "max_hp": 80,
        "max_mana": 100,
        "attack": 35,
        "defense": 8,
        "critical_chance": 35
    }
}


class Player:

    def __init__(self, name, player_class):
        self.name = name
        self.player_class = player_class
        self.character_class = player_class
        self.level = 1
        self.experience = 0

        self.stats = CLASS_STATS[player_class]

        self.hp = self.stats["max_hp"]
        self.max_hp = self.stats["max_hp"]

        self.mana = self.stats["max_mana"]
        self.max_mana = self.stats["max_mana"]

        self.attack = self.stats["attack"]
        self.defense = self.stats["defense"]

        self.is_defending = False

        self.gold = 0
        self.weapon = None

        self.base_critical_chance = self.stats["critical_chance"]
        self.critical_chance = self.base_critical_chance

        self.critical_damage = 2

        self.armor = None

        self.critical_resistance = 0

        self.weapons = []
        self.armors = []
        self.potions = []

        self.bosses_defeated = []
        self.enemies_defeated = 0

        # Stats for victory and progression tracking
        self.weapons_collected = 0
        self.rare_items_found = 0
        self.play_time_seconds = 0
        self.start_time = time.time()

    def get_total_play_time_seconds(self):
        return int(self.play_time_seconds + (time.time() - self.start_time))

    def display_stats(self):
        print("========================")
        print("     PLAYER STATS     ")
        print("========================")
        print(f"Name       : {self.name}")
        print(f"Class      : {self.player_class}")
        print(f"Level      : {self.level}")
        print(f"Experience : {self.experience}")
        print(f"HP         : {self.hp} / {self.max_hp}")
        print(f"Mana       : {self.mana} / {self.max_mana}")
        print(f"Attack     : {self.attack}")
        print(f"Defense    : {self.defense}")
        print(f"Crit Chance: {self.critical_chance}%")
        print(f"Gold       : {self.gold}")

    def check_level_up(self):
        boss_milestones = {
            10: "Goblin King",
            20: "Forest Guardian",
            30: "Ancient Golem",
            40: "Vampire Lord",
            50: "Dragon Rider",
            60: "Demon General",
            70: "Ice Titan",
            80: "Shadow Emperor",
            90: "Celestial Dragon"
        }

        while self.level < 100 and self.experience >= self.level * 100:
            # Check milestone boss requirement
            if self.level in boss_milestones:
                required_boss = boss_milestones[self.level]
                if required_boss not in self.bosses_defeated:
                    print(f"\n⚠️ LEVEL CAP REACHED at Level {self.level}!")
                    print(f"You cannot advance beyond Level {self.level} until you defeat: {required_boss}!")
                    # Cap experience just below level threshold to avoid infinite loop
                    self.experience = min(self.experience, (self.level * 100) - 1)
                    break

            required_xp = self.level * 100
            self.experience -= required_xp
            self.level += 1

            self.max_hp += 10
            self.max_mana += 10
            self.attack += 5
            self.defense += 5
            self.critical_chance += 2

            self.hp = self.max_hp
            self.mana = self.max_mana

            print(f"\n🌟 You leveled up to Level {self.level}!")
            print("Your HP and Mana have been fully restored!")

            # Skill tier unlocks
            if self.level == 5:
                print("✨ New Skill Unlocked: Tier 2 Skill is now available!")
            elif self.level == 10:
                print("✨ New Skill Unlocked: Tier 3 Skill is now available!")
            elif self.level == 15:
                print("✨ New Skill Unlocked: Tier 4 Ultimate Skill is now available!")

            # Passive bonus every 5 levels
            if self.level % 5 == 0:
                bonus_hp = 15
                bonus_mana = 10
                bonus_atk = 5
                bonus_def = 5
                self.max_hp += bonus_hp
                self.max_mana += bonus_mana
                self.attack += bonus_atk
                self.defense += bonus_def
                self.hp = self.max_hp
                self.mana = self.max_mana
                print(f"🎉 PASSIVE MILESTONE REACHED (Level {self.level})!")
                print(f"Bonus: +{bonus_atk} ATK, +{bonus_def} DEF, +{bonus_hp} Max HP, +{bonus_mana} Max Mana!")

        if self.level >= 100:
            self.level = 100
            self.experience = 0

    def equip_weapon(self, weapon):
        if self.level < weapon.required_level:
            print(
                f"You need to be level {weapon.required_level} "
                f"to equip {weapon.weapon_name}!"
            )
            return False

        self.weapon = weapon
        self.critical_chance = self.base_critical_chance + weapon.crit_bonus

        print(f"\n{weapon.weapon_name} equipped!")
        print(f"Damage: {weapon.damage}")
        print(f"Critical Chance: {self.critical_chance}%")

        return True

    def unequip_weapon(self):
        if self.weapon is None:
            print("\nNo weapon is currently equipped!")
            return False
        print(f"\nUnequipped {self.weapon.weapon_name}!")
        self.weapon = None
        self.critical_chance = self.base_critical_chance
        return True

    def equip_armor(self, armor):
        if self.level < armor.required_level:
            print(
                f"You need to be level {armor.required_level} "
                f"to equip {armor.armor_name}!"
            )
            return False

        if self.armor is not None:
            self.defense -= self.armor.defense
            self.max_hp -= self.armor.hp_bonus
            self.max_mana -= self.armor.mana_bonus
            self.critical_resistance -= self.armor.crit_resistance

        self.armor = armor

        self.defense += armor.defense
        self.max_hp += armor.hp_bonus
        self.max_mana += armor.mana_bonus
        self.critical_resistance += armor.crit_resistance

        self.hp = min(self.hp, self.max_hp)
        self.mana = min(self.mana, self.max_mana)

        print(f"\n{armor.armor_name} equipped!")
        print(f"Defense: {self.defense}")
        print(f"Max HP: {self.max_hp}")
        print(f"Max Mana: {self.max_mana}")
        print(f"Critical Resistance: {self.critical_resistance}%")

        return True

    def unequip_armor(self):
        if self.armor is None:
            print("\nNo armor is currently equipped!")
            return False
        print(f"\nUnequipped {self.armor.armor_name}!")
        self.defense -= self.armor.defense
        self.max_hp -= self.armor.hp_bonus
        self.max_mana -= self.armor.mana_bonus
        self.critical_resistance -= self.armor.crit_resistance
        self.hp = min(self.hp, self.max_hp)
        self.mana = min(self.mana, self.max_mana)
        self.armor = None
        return True

    def use_potion(self, potion):
        if potion.type == "health":
            if potion.value == "full":
                self.hp = self.max_hp
            else:
                self.hp = min(self.max_hp, self.hp + potion.value)
            print(f"Used {potion.potion_name}!")
            print(f"HP: {self.hp}/{self.max_hp}")

        elif potion.type == "mana":
            if potion.value == "full":
                self.mana = self.max_mana
            else:
                self.mana = min(self.max_mana, self.mana + potion.value)
            print(f"Used {potion.potion_name}!")
            print(f"Mana: {self.mana}/{self.max_mana}")

        elif potion.type == "mixed":
            if potion.value == "full":
                self.hp = self.max_hp
                self.mana = self.max_mana
            else:
                self.hp = min(self.max_hp, self.hp + potion.value)
                self.mana = min(self.max_mana, self.mana + potion.value)
            print(f"Used {potion.potion_name}!")
            print(f"HP: {self.hp}/{self.max_hp}")
            print(f"Mana: {self.mana}/{self.max_mana}")

        elif potion.type == "attack_buff":
            self.attack += potion.value
            print(f"Attack increased by {potion.value}!")

        elif potion.type == "defense_buff":
            self.defense += potion.value
            print(f"Defense increased by {potion.value}!")

        elif potion.type == "crit_buff":
            self.critical_chance += potion.value
            print(f"Critical Chance increased by {potion.value}%!")

    def add_potion(self, potion):
        self.potions.append(potion)
        print(f"{potion.potion_name} added to inventory!")

    def show_potions(self):
        if not self.potions:
            print("No potions in inventory.")
            return

        print("\n===== POTIONS =====")
        for i, potion in enumerate(self.potions, start=1):
            print(f"{i}. {potion.potion_name}")

    def use_potion_from_inventory(self):
        if not self.potions:
            print("You have no potions!")
            return

        self.show_potions()
        try:
            choice = int(input("\nChoose a potion (0 to cancel): "))
            if choice == 0:
                return
            if choice < 1 or choice > len(self.potions):
                print("Invalid choice!")
                return

            potion = self.potions[choice - 1]
            self.use_potion(potion)
            self.potions.remove(potion)
        except ValueError:
            print("Please enter a number!")

    def drop_potion_from_inventory(self):
        if not self.potions:
            print("\nNo potions in inventory to drop.")
            return

        self.show_potions()
        try:
            choice = int(input("\nChoose a potion to drop (0 to cancel): "))
            if choice == 0:
                return
            if choice < 1 or choice > len(self.potions):
                print("Invalid choice!")
                return

            dropped = self.potions.pop(choice - 1)
            print(f"\nDropped {dropped.potion_name}!")
        except ValueError:
            print("Please enter a number!")

    def add_weapon(self, weapon):
        self.weapons.append(weapon)
        self.weapons_collected += 1
        if getattr(weapon, "rarity", "") in ["Rare", "Super Rare", "Epic", "Mythical", "Legendary"]:
            self.rare_items_found += 1
        print(f"{weapon.weapon_name} added to inventory!")

    def show_weapons(self):
        if not self.weapons:
            print("No weapons in inventory.")
            return

        print("\n===== WEAPONS =====")
        for i, weapon in enumerate(self.weapons, start=1):
            equipped_tag = " [Equipped]" if self.weapon == weapon else ""
            print(
                f"{i}. {weapon.weapon_name} | "
                f"{weapon.rarity} | "
                f"Damage: {weapon.damage}{equipped_tag}"
            )

    def equip_weapon_from_inventory(self):
        if not self.weapons:
            print("No weapons in inventory to equip.")
            return

        self.show_weapons()
        try:
            choice = int(input("\nChoose a weapon to equip (0 to cancel): "))
            if choice == 0:
                return
            if choice < 1 or choice > len(self.weapons):
                print("Invalid choice!")
                return

            chosen_weapon = self.weapons[choice - 1]
            self.equip_weapon(chosen_weapon)
        except ValueError:
            print("Please enter a number!")

    def drop_weapon_from_inventory(self):
        if not self.weapons:
            print("\nNo weapons in inventory to drop.")
            return

        self.show_weapons()
        try:
            choice = int(input("\nChoose a weapon to drop (0 to cancel): "))
            if choice == 0:
                return
            if choice < 1 or choice > len(self.weapons):
                print("Invalid choice!")
                return

            dropped = self.weapons.pop(choice - 1)
            if self.weapon == dropped:
                self.unequip_weapon()
            print(f"\nDropped {dropped.weapon_name}!")
        except ValueError:
            print("Please enter a number!")

    def add_armor(self, armor):
        self.armors.append(armor)
        if getattr(armor, "rarity", "") in ["Rare", "Super Rare", "Epic", "Mythical", "Legendary"]:
            self.rare_items_found += 1
        print(f"{armor.armor_name} added to inventory!")

    def show_armors(self):
        if not self.armors:
            print("No armor in inventory.")
            return

        print("\n===== ARMOR =====")
        for i, armor in enumerate(self.armors, start=1):
            equipped_tag = " [Equipped]" if self.armor == armor else ""
            print(
                f"{i}. {armor.armor_name} | "
                f"{armor.rarity} | "
                f"Defense: {armor.defense}{equipped_tag}"
            )

    def equip_armor_from_inventory(self):
        if not self.armors:
            print("No armor in inventory to equip.")
            return

        self.show_armors()
        try:
            choice = int(input("\nChoose armor to equip (0 to cancel): "))
            if choice == 0:
                return
            if choice < 1 or choice > len(self.armors):
                print("Invalid choice!")
                return

            chosen_armor = self.armors[choice - 1]
            self.equip_armor(chosen_armor)
        except ValueError:
            print("Please enter a number!")

    def drop_armor_from_inventory(self):
        if not self.armors:
            print("\nNo armor in inventory to drop.")
            return

        self.show_armors()
        try:
            choice = int(input("\nChoose armor to drop (0 to cancel): "))
            if choice == 0:
                return
            if choice < 1 or choice > len(self.armors):
                print("Invalid choice!")
                return

            dropped = self.armors.pop(choice - 1)
            if self.armor == dropped:
                self.unequip_armor()
            print(f"\nDropped {dropped.armor_name}!")
        except ValueError:
            print("Please enter a number!")

    def inventory_menu(self):
        while True:
            print("\n========== INVENTORY ==========")
            eq_weapon = self.weapon.weapon_name if self.weapon else "None"
            eq_armor = self.armor.armor_name if self.armor else "None"
            print(f"Equipped Weapon: {eq_weapon}")
            print(f"Equipped Armor : {eq_armor}")
            print("-------------------------------")
            print("1. View Weapons")
            print("2. Equip Weapon")
            print("3. Unequip Weapon")
            print("4. Drop Weapon")
            print("5. View Armor")
            print("6. Equip Armor")
            print("7. Unequip Armor")
            print("8. Drop Armor")
            print("9. View Potions")
            print("10. Use Potion")
            print("11. Drop Potion")
            print("12. Back")

            try:
                choice = int(input("\nChoose an option: "))
                if choice == 1:
                    self.show_weapons()
                elif choice == 2:
                    self.equip_weapon_from_inventory()
                elif choice == 3:
                    self.unequip_weapon()
                elif choice == 4:
                    self.drop_weapon_from_inventory()
                elif choice == 5:
                    self.show_armors()
                elif choice == 6:
                    self.equip_armor_from_inventory()
                elif choice == 7:
                    self.unequip_armor()
                elif choice == 8:
                    self.drop_armor_from_inventory()
                elif choice == 9:
                    self.show_potions()
                elif choice == 10:
                    self.use_potion_from_inventory()
                elif choice == 11:
                    self.drop_potion_from_inventory()
                elif choice == 12:
                    break
                else:
                    print("Invalid choice!")
            except ValueError:
                print("Please enter a number!")
