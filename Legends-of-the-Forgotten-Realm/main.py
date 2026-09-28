import sys

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

from player import Player
from enemy import get_random_enemy
from bosses import get_boss
from world import get_region, get_current_region_boss, display_world
from combat import battle
from shop import shop_menu
from save_load import save_game, load_game


def create_player():
    classes = {
        1: "Warrior",
        2: "Mage",
        3: "Archer",
        4: "Assassin"
    }
    while True:
        name = input("Enter name:-")

        if name.strip():
            break

        print("Name cannot be empty!")

    while True:
        try:
            ch = int(input(f'Choose your class\n1. Warrior\n2. Mage\n3. Archer\n4. Assassin:-'))

            if ch in classes:
                player_class = classes[ch]
                break
            else:
                print('Invalid choice')

        except ValueError:
            print('Plese enter a number!!!')

    player = Player(name, player_class)
    print('===== PLAYER CREATED =====')

    return player


def display_victory(player):

    total_secs = player.get_total_play_time_seconds() if hasattr(player, "get_total_play_time_seconds") else 0
    mins = total_secs // 60
    secs = total_secs % 60

    score = (
        (player.level * 100)
        + (player.enemies_defeated * 50)
        + (len(player.bosses_defeated) * 500)
        + (player.gold * 2)
        + (getattr(player, "weapons_collected", len(player.weapons)) * 75)
        + (getattr(player, "rare_items_found", 0) * 200)
    )

    print("\n" + "=" * 45)
    print("                 VICTORY!")
    print("=" * 45)
    print(f"\nCongratulations, {player.name}!\n")
    print(f"Final Level      : {player.level}")
    print(f"Enemies Defeated : {player.enemies_defeated}")
    print(f"Bosses Defeated  : {len(player.bosses_defeated)}")
    print(f"Total Gold       : {player.gold}")
    print(f"Weapons Collected: {getattr(player, 'weapons_collected', len(player.weapons))}")
    print(f"Rare Items Found : {getattr(player, 'rare_items_found', 0)}")
    print(f"Total Play Time  : {mins}m {secs}s")
    print(f"Final Score      : {score}")
    print("\nYou have conquered the Forgotten Realm!")
    print("=" * 45)


def game_over_menu(player):

    print("\n" + "=" * 40)
    print("              GAME OVER")
    print("=" * 40)
    print("1. Retry")
    print("2. Load Save")
    print("3. Exit")

    while True:
        try:
            choice = int(input("\nChoose an option: "))

            if choice == 1:
                return "retry"

            elif choice == 2:
                saved_player = load_game()
                if saved_player:
                    return saved_player
                else:
                    print("Could not load save. Try another option.")

            elif choice == 3:
                print("\nReturning to main menu...")
                return "exit"

            else:
                print("Invalid choice!")

        except ValueError:
            print("Please enter a number!")


def explore(player):

    region = get_region(player.level)

    print("\n" + "=" * 40)
    print(f"You are exploring the {region}.")
    print("=" * 40)

    boss = get_current_region_boss(player.level)

    if boss and boss.name not in player.bosses_defeated:

        print(f"\n⚠️ You encountered {boss.name}!")

        result = battle(player, boss)

        if result:

            player.bosses_defeated.append(boss.name)

            if boss.name == "Ancient Demon King":
                display_victory(player)

        return

    enemy = get_random_enemy(player.level)

    result = battle(player, enemy)

    if result:

        player.enemies_defeated += 1


def game_menu(player):

    while True:

        if player.hp <= 0:
            action = game_over_menu(player)
            if action == "retry":
                player.hp = player.max_hp
                player.mana = player.max_mana
                print("\nYou have been revived! Prepare for battle once more.")
                continue
            elif action == "exit":
                break
            elif isinstance(action, Player):
                player = action
                continue

        print("\n")
        print("=" * 40)
        print("       LEGENDS OF THE FORGOTTEN REALM")
        print("=" * 40)

        print(f"Name: {player.name}")
        print(f"Level: {player.level}")
        print(f"HP: {player.hp}/{player.max_hp}")
        print(f"Gold: {player.gold}")

        print("\n1. Explore")
        print("2. Shop")
        print("3. World")
        print("4. Inventory")
        print("5. View Stats")
        print("6. Save Game")
        print("7. Exit Game")

        try:

            choice = int(input("\nChoose an option: "))

            if choice == 1:

                explore(player)

            elif choice == 2:

                shop_menu(player)

            elif choice == 3:

                display_world(player)

            elif choice == 4:

                player.inventory_menu()

            elif choice == 5:

                player.display_stats()

            elif choice == 6:

                save_game(player)

            elif choice == 7:

                print("\nLeaving the realm...")
                break

            else:

                print("Invalid choice!")

        except ValueError:

            print("Please enter a number!")


def instructions():

    print("\n========== INSTRUCTIONS ==========")

    print("""
Welcome to Legends of the Forgotten Realm!

Explore different regions.
Fight enemies to gain XP and Gold.
Use weapons, armor, potions and skills.
Defeat bosses to unlock your journey.
Collect better equipment through loot.
Level up your character and become stronger.

Battle options:
1. Attack
2. Skills
3. Heal
4. Use Potion
5. Defend
6. Inventory
7. View Stats
8. Run

Bosses cannot be escaped.
Bosses become stronger as you progress.
""")


def main():

    while True:

        print("\n")
        print("=" * 50)
        print("      LEGENDS OF THE FORGOTTEN REALM")
        print("=" * 50)

        print("1. New Game")
        print("2. Continue")
        print("3. Instructions")
        print("4. Exit")

        try:

            choice = int(input("\nChoose an option: "))

            if choice == 1:

                player = create_player()

                print("\nCharacter created successfully!")

                game_menu(player)

            elif choice == 2:

                player = load_game()
                if player:
                    game_menu(player)

            elif choice == 3:

                instructions()

            elif choice == 4:

                print("\nThank you for playing!")
                break

            else:

                print("Invalid choice!")

        except ValueError:

            print("Please enter a number!")


if __name__ == "__main__":
    main()