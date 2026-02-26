import random
from datetime import datetime

class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.health = 100
        self.max_health = 100
        self.experience = 0
        self.gold = 0
        self.location = "Village"
        self.inventory = []
    
    def take_damage(self, damage):
        self.health = max(0, self.health - damage)
    
    def heal(self, amount):
        self.health = min(self.max_health, self.health + amount)
    
    def gain_experience(self, amount):
        self.experience += amount
        if self.experience >= self.level * 100:
            self.level_up()
    
    def level_up(self):
        self.level += 1
        self.max_health += 10
        self.health = self.max_health
        print(f"\n{self.name} leveled up to {self.level}!")
    
    def status(self):
        return f"\n{'='*40}\n{self.name} | Level {self.level} | HP: {self.health}/{self.max_health}\nLocation: {self.location} | Gold: {self.gold} | XP: {self.experience}\n{'='*40}"

class Game:
    def __init__(self):
        self.player = None
        self.locations = ["Village", "Forest", "Dungeon", "Castle", "Cave", "Swamp", "Mountain"]

        self.enemies = [
            {"name": "Goblin", "health": 20, "damage": 5, "xp": 50, "gold": 10, "location": "Forest"},
            {"name": "Orc", "health": 40, "damage": 10, "xp": 100, "gold": 25, "location": "Mountain"},
            {"name": "Dragon", "health": 100, "damage": 20, "xp": 500, "gold": 100, "location": "Castle"},
            {"name": "Bandit", "health": 30, "damage": 7, "xp": 75, "gold": 15, "location": "Forest"},
            {"name": "Skeleton", "health": 25, "damage": 6, "xp": 60, "gold": 12, "location": "Dungeon"},
            {"name": "Troll", "health": 50, "damage": 12, "xp": 150, "gold": 30, "location": "Swamp"},
            {"name": "Vampire", "health": 60, "damage": 15, "xp": 200, "gold": 40, "location": "Castle"},
            {"name": "Chicken", "health": 5, "damage": 1, "xp": 10, "gold": 2, "location": "Village"},
            {"name": "Giant Spider", "health": 35, "damage": 8, "xp": 80, "gold": 20, "location": "Cave"},
            {"name": "Zombie", "health": 30, "damage": 6, "xp": 70, "gold": 18, "location": "Dungeon"},
            {"name": "Giant Snake", "health": 40, "damage": 10, "xp": 90, "gold": 22, "location": "Swamp"},
            {"name": "Dark Knight", "health": 80, "damage": 18, "xp": 300, "gold": 50, "location": "Castle"},
            {"name": "Giant Rat", "health": 15, "damage": 4, "xp": 30, "gold": 5, "location": "Cave"},
            {"name": "Bandit Leader", "health": 45, "damage": 10, "xp": 120, "gold": 35, "location": "Forest"},
            {"name": "Giant Worm", "health": 50, "damage": 12, "xp": 150, "gold": 30, "location": "Cave"},
            {"name": "Lich", "health": 70, "damage": 15, "xp": 250, "gold": 45, "location": "Dungeon"},
            {"name": "Chicken", "health": 5, "damage": 1, "xp": 10, "gold": 2, "location": "Village"},
            {"name": "Slime", "health": 20, "damage": 3, "xp": 40, "gold": 8, "location": "Swamp"},
        ]

    def start(self):
        print("Welcome to TextMMO!")
        name = input("Enter your character name: ")
        self.player = Player(name)
        self.main_loop()
    
    def main_loop(self):
        while self.player.health > 0:
            print(self.player.status())
            print("\nCommands: explore, fight, heal, rest, inventory, quit")
            command = input("What do you do? ").lower().strip()
            
            if command == "quit":
                print("Thanks for playing!")
                break
            elif command == "explore":
                self.explore()
            elif command == "fight":
                self.fight()
            elif command == "heal":
                self.heal()
            elif command == "rest":
                self.rest()
            elif command == "inventory":
                self.show_inventory()
            else:
                print("Unknown command!")
    
    def explore(self):
        location = random.choice(self.locations)
        self.player.location = location
        print(f"\nYou travel to {location}...")
    
    def fight(self):
        available_enemies = [e for e in self.enemies if e["location"] == self.player.location]

        if not available_enemies:
            print(f"No enemies found in {self.player.location}!")
            return
        enemy = random.choice(self.enemies).copy()
        print(f"\nA {enemy['name']} appears! ({enemy['health']} HP)")
        
        while enemy["health"] > 0 and self.player.health > 0:
            action = input("Attack (a) or Defend (d)? ").lower()
            
            if action == "a":
                damage = random.randint(5, 15)
                enemy["health"] -= damage
                print(f"You dealt {damage} damage!")
            elif action == "d":
                damage = max(1, enemy["damage"] - random.randint(2, 5))
                self.player.take_damage(damage)
                print(f"You defended! Only took {damage} damage.")
                continue
            
            if enemy["health"] > 0:
                damage = enemy["damage"]
                self.player.take_damage(damage)
                print(f"{enemy['name']} dealt {damage} damage!")
        
        if self.player.health > 0:
            print(f"\nVictory! You defeated {enemy['name']}!")
            self.player.gain_experience(enemy["xp"])
            self.player.gold += enemy["gold"]
    
    def heal(self):
        if self.player.gold >= 20:
            self.player.heal(50)
            self.player.gold -= 20
            print("You healed for 50 HP!")
        else:
            print("Not enough gold to heal!")
    
    def rest(self):
        self.player.heal(self.player.max_health)
        print("You rested and fully healed.")
    
    def show_inventory(self):
        print(f"\nInventory: {self.player.inventory if self.player.inventory else 'Empty'}")
    
    def game_over(self):
        print(f"\nGame Over! {self.player.name} reached level {self.player.level}.")

if __name__ == "__main__":
    game = Game()
    game.start()