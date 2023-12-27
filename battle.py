import random
from players import Character, Enemy
from dependencies import *



def battle(player, enemies):
    print("Battle Start!")

    while True:
        # Player's turn
        print("\nPlayer's Turn:")
        player.display_status()
        action = input("Choose your action (1. Attack, 2. Use Ability, 3. Defend): ")

        if action == "1":
            target = random.choice(enemies)
            player.attack(target)
        if action == "2":
            target = random.choice(enemies)
            player.use_ability(target)
        if action == "3":
            player.defend()

        # Check victory condition
        if all(enemy.health_points <= 0 for enemy in enemies):
            print("Congratulations! You defeated all enemies!")
            break

        # Enemies' turn
        print("\nEnemies' Turn:")
        for enemy in enemies:
            enemy.enemy_attack(player)
            player.display_status()

        # Check defeat condition
        if player.health_points <= 0:
            print("Game Over! You were defeated by the enemies.")
            break



battle(player, [enemy1, enemy2])
