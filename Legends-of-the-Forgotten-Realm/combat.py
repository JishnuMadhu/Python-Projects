import random
import sys

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

from loot import generate_enemy_loot, generate_boss_loot, give_loot
from skills import use_skill


def player_attack(player, enemy):

    weapon_damage = 0

    if player.weapon:
        weapon_damage = player.weapon.damage

    damage = player.attack + weapon_damage - enemy.defense

    if damage < 0:
        damage = 0

    critical = random.randint(1, 100) <= player.critical_chance

    if critical:
        damage *= player.critical_damage
        print("\n💥 CRITICAL HIT!")

    enemy.hp = max(0, enemy.hp - damage)

    print(f"\nYou dealt {damage} damage!")
    print(f"{enemy.name} HP: {enemy.hp}/{enemy.max_hp}")


def enemy_attack(player, enemy):

    damage = enemy.attack - player.defense

    if damage < 0:
        damage = 0

    critical_chance = 10

    if getattr(enemy, "is_boss", False):
        critical_chance = 20

    critical = random.randint(1, 100) <= critical_chance

    if critical:
        damage *= 2
        print("\n💥 ENEMY CRITICAL HIT!")

    if player.is_defending:
        damage //= 2
        print("\nYour defense reduced the damage!")

    player.hp = max(0, player.hp - damage)

    print(f"{enemy.name} dealt {damage} damage!")
    print(f"Your HP: {player.hp}/{player.max_hp}")

    player.is_defending = False


def player_defend(player):

    player.is_defending = True

    print("\nYou are defending!")
    print("Incoming damage will be reduced by 50%.")


def heal(player):

    if player.hp >= player.max_hp:

        print("\nYour HP is already full!")

        return False

    heal_amount = 50

    old_hp = player.hp

    player.hp = min(
        player.max_hp,
        player.hp + heal_amount
    )

    print(f"\nYou healed for {player.hp - old_hp} HP!")
    print(f"HP: {player.hp}/{player.max_hp}")

    return True


def boss_special_attack(player, boss):

    print("\n" + "=" * 40)
    print(f"⚠️ {boss.name} uses a SPECIAL ATTACK!")
    print("=" * 40)

    special_damage = boss.attack + 20 - player.defense

    if special_damage < 0:
        special_damage = 0

    if player.is_defending:
        special_damage //= 2
        print("Your defense reduced the special attack!")

    player.hp = max(0, player.hp - special_damage)

    print(
        f"{boss.name} dealt "
        f"{special_damage} special damage!"
    )

    print(
        f"Your HP: "
        f"{player.hp}/{player.max_hp}"
    )

    player.is_defending = False


def boss_heal(boss):

    heal_amount = int(boss.max_hp * 0.10)

    old_hp = boss.hp

    boss.hp = min(
        boss.max_hp,
        boss.hp + heal_amount
    )

    print(
        f"\n{boss.name} healed "
        f"{boss.hp - old_hp} HP!"
    )

    print(
        f"Boss HP: "
        f"{boss.hp}/{boss.max_hp}"
    )


def show_inventory(player):

    print("\n========== INVENTORY ==========")

    player.show_weapons()
    player.show_armors()
    player.show_potions()

    print("===============================")


def battle(player, enemy):

    is_boss = getattr(enemy, "is_boss", False)

    boss_turn_count = 0

    print("\n" + "=" * 45)

    if is_boss:
        print(f"👑 BOSS BATTLE: {enemy.name}!")
    else:
        print(f"⚔️ A wild {enemy.name} appeared!")

    print("=" * 45)

    while player.hp > 0 and enemy.hp > 0:

        print("\n-----------------------------")

        print(
            f"{player.name}: "
            f"{player.hp}/{player.max_hp} HP | "
            f"{player.mana}/{player.max_mana} Mana"
        )

        print(
            f"{enemy.name}: "
            f"{enemy.hp}/{enemy.max_hp} HP"
        )

        print("\n1. Attack")
        print("2. Skills")
        print("3. Heal")
        print("4. Use Potion")
        print("5. Defend")
        print("6. Inventory")
        print("7. View Stats")
        print("8. Run")

        try:
            choice = int(input("Choose an action: "))

            # -------------------------
            # ATTACK
            # -------------------------

            if choice == 1:

                player_attack(player, enemy)

                if enemy.hp <= 0:
                    break

                if not is_boss:
                    enemy_attack(player, enemy)

            # -------------------------
            # SKILLS
            # -------------------------

            elif choice == 2:

                skill_used = use_skill(player, enemy)

                if not skill_used:
                    continue

                if enemy.hp <= 0:
                    break

                if not is_boss:
                    enemy_attack(player, enemy)

            # -------------------------
            # HEAL
            # -------------------------

            elif choice == 3:

                if heal(player):

                    if enemy.hp > 0:
                        if not is_boss:
                            enemy_attack(player, enemy)

            # -------------------------
            # POTION
            # -------------------------

            elif choice == 4:

                before_potions = len(player.potions)

                player.use_potion_from_inventory()

                after_potions = len(player.potions)

                if after_potions < before_potions:

                    if enemy.hp > 0:
                        if not is_boss:
                            enemy_attack(player, enemy)

            # -------------------------
            # DEFEND
            # -------------------------

            elif choice == 5:

                player_defend(player)

                if not is_boss:
                    enemy_attack(player, enemy)

            # -------------------------
            # INVENTORY
            # -------------------------

            elif choice == 6:

                show_inventory(player)

                continue

            # -------------------------
            # STATS
            # -------------------------

            elif choice == 7:

                player.display_stats()

                continue

            # -------------------------
            # RUN
            # -------------------------

            elif choice == 8:

                if is_boss:

                    print("\nYou cannot run from a boss!")

                    continue

                print("\nYou escaped from the battle!")

                return False

            else:

                print("Invalid choice!")

                continue

        except ValueError:

            print("Please enter a number!")

            continue

        # ==================================
        # BOSS TURN PROCESSING
        # ==================================

        if enemy.hp > 0 and is_boss:

            boss_turn_count += 1

            if boss_turn_count % 3 == 0:

                boss_special_attack(player, enemy)

                if player.hp <= 0:
                    break

                boss_heal(enemy)

            else:

                enemy_attack(player, enemy)

        # ==================================
        # PLAYER DEFEATED
        # ==================================

        if player.hp <= 0:

            print("\n" + "=" * 40)
            print("💀 YOU HAVE BEEN DEFEATED!")
            print("=" * 40)

            return False

    # ==================================
    # ENEMY DEFEATED
    # ==================================

    if enemy.hp <= 0:

        print("\n" + "=" * 40)

        if is_boss:
            print(f"👑 {enemy.name} DEFEATED!")
        else:
            print(f"⚔️ {enemy.name} DEFEATED!")

        print("=" * 40)

        xp = getattr(enemy, "experience", getattr(enemy, "experience_reward", 0))
        gold = getattr(enemy, "gold", getattr(enemy, "gold_reward", 0))

        player.experience += xp
        player.gold += gold

        print(f"\nYou gained {xp} XP!")
        print(f"You received {gold} gold!")

        player.check_level_up()

        # -------------------------
        # LOOT
        # -------------------------

        if is_boss:

            print("\n🎁 BOSS LOOT!")

            loot = generate_boss_loot()

        else:

            print("\n🎁 ENEMY LOOT!")

            loot = generate_enemy_loot()

        give_loot(player, loot)

        return True

    return False
