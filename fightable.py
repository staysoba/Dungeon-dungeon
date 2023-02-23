class Fightable():
    def __init__(self, health=1):
        self.maxHealth = health
        self.currentHealth = self.maxHealth
        

        self.baseDefense = 1
        self.baseAtk = 5

    def attack(self):
        return self.baseAtk

    def takeDmg(self, damage):
        self.currentHealth -= damage

    def isAlive(self):
        if self.currentHealth <= 0:
            return False

        return True


class Hero(Fightable):
    def __init__(self):
        super().__init__(health=20)

        self.inventory = ["killer blade","flaming sword",
]
        self.primaryWeapon = None

    def attack(self):
        if self.primaryWeapon:
            ## TODO figure out primary weapon logic
            return self.baseAtk 

        return self.baseAtk





class Mob(Fightable):
    def __init__(self):
        super().__init__()


class Inventory(Fightable):
    def __init__(self):
        super().__init__(self)
        self.sword = self.baseAtk * 3
        self.dagger = self.baseAtk *2
        self.bow = self.baseAtk *2
        self.sheild = self.baseDefense * 5

    def displayInventory(self):
        for index, item in enumerate(Inventory):
            print("{}) {}".format(index, item[0]))

    





class Goblin(Fightable):
    def __init__(self):
        super().__init__(health=100)



        







        
