import random






#                                                Character Section

class Character:
    def __init__(self, name, health_points, attack_power, defense):
        self.name = name
        self.health_points = health_points
        self.attack_power = attack_power
        self.defense = defense

    def attack(self, target):
        damage = max(0, self.attack_power - target.defense)
        target.health_points -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage.")

    def use_ability(self, target):
        abilities = ["Fireball", "Healing Wave", "Thunder Strike"] 
        random_ability = random.choice(abilities)

        if random_ability == "Fireball":
            damage = max(0, 2 * self.attack_power - target.defense)
            target.health_points -= damage
            print(f"{self.name} casts Fireball on {target.name} for {damage} damage.")
        if random_ability == "Healing Wave":
            heal_amount = 20  
            self.health_points += heal_amount
            print(f"{self.name} casts Healing Wave and restores {heal_amount} HP.")
        if random_ability == "Thunder Strike":
            damage = max(0, 1.5 * self.attack_power - target.defense)
            target.health_points -= damage
            print(f"{self.name} casts Thunder Strike on {target.name} for {damage} damage.")

    def defend(self):
        defense_options = ["Dodge", "Block"] 
        random_defense = random.choice(defense_options)

        if random_defense == "Dodge":
            print(f"{self.name} dodges the next attack.")
        elif random_defense == "Block":
            self.defense += 5 
            print(f"{self.name} blocks the next attack.")

    def display_status(self):
        print(f"{self.name}'s HP: {self.health_points}")






###################################################################################################################
        
#                                                Enemy Section
class Enemy(Character):
    def __init__(self, name, health_points, attack_power, defense):
        super().__init__(name, health_points, attack_power, defense)

    def enemy_attack(self, target):
        damage = max(0, self.attack_power - target.defense)
        target.health_points -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage.")
