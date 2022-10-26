from classes.human import Human
import random

class Knight(Human):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.strength = 7
        
    def name_str(self):
        print(f"Name String: {self.name}")

    def heal_thyself(self):
        print(f"{self.name} is offering a prayer...")
        self.health += random.randint(2,7);

    def attack(self, target):
        print(f"{self.name} swangs {target.name}")
        target.health -= self.strength
        print(f"{target.name} took {self.strength} damage")
        print(f"{target.name} health is at {target.health}")
