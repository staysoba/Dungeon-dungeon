# Hold menu items ----DONE
# those items should be executable
# items should be selectable
# should be able to display items ---- DONE


class Goblin():
    def __init__(self, health=100):
        self.maxHealth = health
        self.currentHealth = self.maxHealth



class Menu():
    def __init__(self):
        self.menuItems = []
        self.menuFunctions = []


    def addMenuItems(self, text: str, function, param=None):
        self.menuItems.append([text, function, param]) 

    def displayMenu(self):
        for index, item in enumerate(self.menuItems):
            print("{}) {}".format(index, item[0]))

    def runItem(self, menuIndex: str):

        if menuIndex.isdigit():
            menuIndex = int(menuIndex)

            if menuIndex in range(0, len(self.menuItems)):

                if self.menuItems[menuIndex][2] is None:
                    self.menuItems[menuIndex][1]()
                else:
                    self.menuItems[menuIndex][1](self.menuItems[menuIndex])

                




        # menuIndex.
        # menuIndex = int(menuIndex)
        # print(self.menuItems[menuIndex])



