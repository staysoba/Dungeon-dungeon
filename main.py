
from lib import fightable, menu, hero
from lib.mobs import mob
from lib.mobs.goblin import Goblin
from lib.mobs.tree import TreeBoss
from lib.Weapons.weapons import Weapon
from lib.consumables.consumable import Consumable
import random
def main():
    print("Welcome to my Dugeon game")

    mainMenu = menu.Menu()

    mainMenu.addMenuItem("Start Game", gameLoop)
    mainMenu.addMenuItem("Scores", print, "print this stuff also")
    mainMenu.addMenuItem("Quit", exit)

    mainMenu.displayMenu()

    menuIdx = input("Select> ")

    mainMenu.runItem(menuIdx)


def gameLoop():
    print("\n\n")
    print("We are nwo playing the game")
    player = hero.Hero()

    level = 0
    # Big game loop
    while player.isAlive():
        
        print("level {}".format(level))
        print("player's health is currently {}HP".format(player.curHealth))

        if level % 3 == 0 and level != 0:
            enemy = TreeBoss()
        else:
            enemy = Goblin()
        
        enemy = Goblin()

        # Our fighting loop
        while player.isAlive() and enemy.isAlive():
            print("Player attacks with a {}".format(player.primaryWeapon.name))
            print("the players primary weapon")
            enemy.takeDmg(player.attack())

            player.takeDmg(enemy.attack())

        print("Killed a {}".format(enemy.name))

        # Allow for looting
        if player.isAlive() and not enemy.isAlive():
            # Generate a new menu object
            lootMenu = menu.Menu()

            # TODO Fix but with empty inventory for enemy spawning
            # Add all items from enemy inventory to the menu
            for idx, item in enumerate(enemy.inventory.contains):
                # Adding item, function to execute on selection, and which item should be taken out
                lootMenu.addMenuItem(item.name, enemy.inventory.takeOut, idx)

            # Display 
            lootMenu.displayMenu()

            # Get user input
            userInput = input("Select> ")

            # Add the loot to the user's inventory
            player.inventory.add(lootMenu.runItem(userInput))


        print("Player's Inventory")
        playerInventoryMenu = menu.Menu()
        for idx, item in enumerate(player.inventory.contains):
            if isinstance (item, Weapon):
                playerInventoryMenu.addMenuItem(item.name, player.switchWeapon, idx)
            elif isinstance (item, Consumable):
                playerInventoryMenu.addMenuItem(item.name, item.consume, player)
            


        playerInventoryMenu.displayMenu()
        userInput = input("select> ")
        playerInventoryMenu.runItem(userInput)

        print("\n")
        level += 1


if __name__ == "__main__":
    main()
