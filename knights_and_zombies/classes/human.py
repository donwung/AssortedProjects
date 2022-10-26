class Human:
    def __init__(self):
        self.name = "human";
        self.strength = 10
        self.health = 100
    
    def show_name(self):
        print(self.name)

    def attack(self, target):
        print(f"{self.name} attacking {target.name}")
        target.health -= self.strength
        print(f"{target.name} took {self.strength} damage")
        print(f"{target.name} health is at {target.health}")

    # TODO
    # basic attack kinda sucks
    #   remove and add functionality elsewhere
    # plus prints aren't pretty
    # if zombies get more variety, human class is only inherited by the knight

