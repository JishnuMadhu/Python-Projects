from weapons import WEAPON_DATA, Weapon
from armor import ARMOR_DATA, Armor
from potions import POTION_DATA, Potion


def buy_weapon(player):

    print("\n===== WEAPON SHOP =====")

    weapon_names = list(WEAPON_DATA.keys())

    for i, weapon_name in enumerate(weapon_names, start=1):
        data = WEAPON_DATA[weapon_name]

        print(
            f"{i}. {weapon_name} | "
            f"{data['rarity']} | "
            f"Price: {data['price']} Gold | "
            f"Required Level: {data['required_level']}"
        )

    print("0. Back")

    try:
        choice = int(input("Choose a weapon: "))

        if choice == 0:
            return

        if choice < 1 or choice > len(weapon_names):
            print("Invalid choice!")
            return

        weapon_name = weapon_names[choice - 1]
        data = WEAPON_DATA[weapon_name]

        if player.level < data["required_level"]:
            print(
                f"You need to be level {data['required_level']} "
                f"to buy {weapon_name}!"
            )
            return

        if player.gold < data["price"]:
            print("Not enough gold!")
            return

        weapon = Weapon(weapon_name)

        player.gold -= data["price"]
        player.add_weapon(weapon)

        print(f"Purchased {weapon_name}!")
        print(f"Gold remaining: {player.gold}")

    except ValueError:
        print("Please enter a number!")


def buy_armor(player):

    print("\n===== ARMOR SHOP =====")

    armor_names = list(ARMOR_DATA.keys())

    for i, armor_name in enumerate(armor_names, start=1):
        data = ARMOR_DATA[armor_name]

        print(
            f"{i}. {armor_name} | "
            f"{data['rarity']} | "
            f"Price: {data['price']} Gold | "
            f"Required Level: {data['required_level']}"
        )

    print("0. Back")

    try:
        choice = int(input("Choose armor: "))

        if choice == 0:
            return

        if choice < 1 or choice > len(armor_names):
            print("Invalid choice!")
            return

        armor_name = armor_names[choice - 1]
        data = ARMOR_DATA[armor_name]

        if player.level < data["required_level"]:
            print(
                f"You need to be level {data['required_level']} "
                f"to buy {armor_name}!"
            )
            return

        if player.gold < data["price"]:
            print("Not enough gold!")
            return

        armor = Armor(armor_name)

        player.gold -= data["price"]
        player.add_armor(armor)

        print(f"Purchased {armor_name}!")
        print(f"Gold remaining: {player.gold}")

    except ValueError:
        print("Please enter a number!")


def buy_potion(player):

    print("\n===== POTION SHOP =====")

    potion_names = list(POTION_DATA.keys())

    for i, potion_name in enumerate(potion_names, start=1):
        data = POTION_DATA[potion_name]

        print(
            f"{i}. {potion_name} | "
            f"Price: {data['price']} Gold"
        )

    print("0. Back")

    try:
        choice = int(input("Choose a potion: "))

        if choice == 0:
            return

        if choice < 1 or choice > len(potion_names):
            print("Invalid choice!")
            return

        potion_name = potion_names[choice - 1]
        data = POTION_DATA[potion_name]

        if player.gold < data["price"]:
            print("Not enough gold!")
            return

        potion = Potion(potion_name)

        player.gold -= data["price"]
        player.add_potion(potion)

        print(f"Purchased {potion_name}!")
        print(f"Gold remaining: {player.gold}")

    except ValueError:
        print("Please enter a number!")


def sell_weapon(player):

    if not player.weapons:
        print("You have no weapons to sell.")
        return

    player.show_weapons()

    try:
        choice = int(input("Choose a weapon to sell: "))

        if choice < 1 or choice > len(player.weapons):
            print("Invalid choice!")
            return

        weapon = player.weapons[choice - 1]

        sell_price = weapon.price // 2

        player.weapons.remove(weapon)
        player.gold += sell_price

        print(f"Sold {weapon.weapon_name} for {sell_price} Gold!")
        print(f"Gold: {player.gold}")

    except ValueError:
        print("Please enter a number!")


def sell_armor(player):

    if not player.armors:
        print("You have no armor to sell.")
        return

    player.show_armors()

    try:
        choice = int(input("Choose armor to sell: "))

        if choice < 1 or choice > len(player.armors):
            print("Invalid choice!")
            return

        armor = player.armors[choice - 1]

        sell_price = armor.price // 2

        player.armors.remove(armor)
        player.gold += sell_price

        print(f"Sold {armor.armor_name} for {sell_price} Gold!")
        print(f"Gold: {player.gold}")

    except ValueError:
        print("Please enter a number!")


def sell_potion(player):

    if not player.potions:
        print("You have no potions to sell.")
        return

    player.show_potions()

    try:
        choice = int(input("Choose a potion to sell: "))

        if choice < 1 or choice > len(player.potions):
            print("Invalid choice!")
            return

        potion = player.potions[choice - 1]

        sell_price = potion.price // 2

        player.potions.remove(potion)
        player.gold += sell_price

        print(f"Sold {potion.potion_name} for {sell_price} Gold!")
        print(f"Gold: {player.gold}")

    except ValueError:
        print("Please enter a number!")


def shop_menu(player):

    while True:

        print("\n========== SHOP ==========")
        print(f"Gold: {player.gold}")
        print("1. Buy Weapon")
        print("2. Buy Armor")
        print("3. Buy Potion")
        print("4. Sell Weapon")
        print("5. Sell Armor")
        print("6. Sell Potion")
        print("7. Exit")

        try:
            choice = int(input("Choose an option: "))

            if choice == 1:
                buy_weapon(player)

            elif choice == 2:
                buy_armor(player)

            elif choice == 3:
                buy_potion(player)

            elif choice == 4:
                sell_weapon(player)

            elif choice == 5:
                sell_armor(player)

            elif choice == 6:
                sell_potion(player)

            elif choice == 7:
                print("Leaving shop...")
                break

            else:
                print("Invalid choice!")

        except ValueError:
            print("Please enter a number!")
