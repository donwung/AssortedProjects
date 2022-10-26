from classes.knight import Knight
from classes.zombie import Zombie
#
# Pamela, Uchenna, Don, Corbin, Cieran, Beltus
#

knight_guy = Knight("phil")
zomb = Zombie()
kills = 0
level = 1

while(knight_guy.health > 0):
    response = ""
    while not response == "1":
        response = input("WHAT SHALL YOU DO: ")
        if (response == "1"):
            knight_guy.attack(zomb)
            zomb.attack(knight_guy)
            print("======")
        elif (response == "2"):
            knight_guy.heal_thyself()
            zomb.attack(knight_guy)
            print("======")
        elif (response == "8"):
            print(f"{knight_guy.name} has slain {kills} zombies on level {level}!")
        elif (response == "0"):
            knight_guy.health = -1;
            break
        
        if(zomb.health <= 0):
            kills+= 1;
            zomb.health = 30 + (kills * level)
        if(kills >= 3):
            kills = 0
            level += 1

print(f"{knight_guy.name} has died")



# knight_guy.name_str();
# zomb.show_name()



# knight_guy.attack(zomb)
# zomb.attack(knight_guy)2