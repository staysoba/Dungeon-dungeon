import menu
import fightable


def main():
    print("Welcome to my Dungeon-game")

    mainMenu = menu.Menu()

    mainMenu.addMenuItems("start Game", gameLoop)
    mainMenu.addMenuItems("scores", print,"print this stuff also")
    mainMenu.addMenuItems("Quit", exit)

    mainMenu.displayMenu()


    menuIndex = input("select > ")

    mainMenu.runItem(menuIndex)

def gameLoop():
    print("we are now playing the game")
    player = fightable.Hero()
    goblin = fightable.Goblin()
    




    while player.isAlive():


        while player.isAlive() and goblin.isAlive():

            goblin.takeDmg(player.attack())
            print("ouch!!")
            print(goblin.currentHealth)


            player.takeDmg(goblin.attack())
            print("ahhhh you slithering beast")
            print(player.currentHealth)

            if player.currentHealth <= 0 and goblin.currentHealth > 0:
                print("you were beat by the goblin fool")

            if goblin.currentHealth <= 0 and player.currentHealth > 0:
                print("you have slayed the Gobline and won, HERO!!!")

            if player.currentHealth == 5:
                print("DAAAMN SON YOU BOUT TO GET SMOKED")



        # print("ouch!!")
        # print(goblin.currentHealth)
        # print(player.currentHealth)




if __name__ == "__main__":
    main()