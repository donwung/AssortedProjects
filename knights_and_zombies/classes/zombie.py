from classes.human import Human
import random

class Zombie(Human):
    def __init__ (self):
        super().__init__()
        self.name = "Zombie"
        self.strength = 0
        self.health = 30

    def show_stats(self):
        print(self.name)

    def attack(self, target):
        print(f"{self.name} swipes at {target.name}")
        dmg = self.strength + random.randint(3,6)
        target.health -= dmg
        print(f"{target.name} took {dmg} damage")
        print(f"{target.name} health is at {target.health}")
