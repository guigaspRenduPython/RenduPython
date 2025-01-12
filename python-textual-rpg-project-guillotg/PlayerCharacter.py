import PlayerClass

class PlayerCharacter:
    isKnightInCounter = False
    wizardPowerBurstCounter = 0

    def __init__(self, name, playerClass):
        self.name = name
        self.maxHealth = playerClass.maxHealth
        self.maxHealthLevelUpIncrease = playerClass.maxHealthLevelUpIncrease
        self.health = self.maxHealth
        self.attack = playerClass.attack
        self.attackBuff = 1
        self.defense = playerClass.defense
        self.defenseBuff = 1
        self.speed = playerClass.speed
        self.speedBuff = 1
        self.attackLevelUpIncrease = playerClass.attackLevelUpIncrease
        self.defenseLevelUpIncrease = playerClass.defenseLevelUpIncrease
        self.speedLevelUpIncrease = playerClass.speedLevelUpIncrease
        self.exp = 0
        self.necessaryExp = 10
        self.level = 1
        self.gold = playerClass.startingGold
        self.inventory = list()
        self.specialAction = playerClass.specialAction
    
    def FightRewards(self, enemyExp, enemyGold):
        self.exp += enemyExp
        self.gold += enemyGold

        print("You gain" , enemyGold, "gold and ", enemyExp, " experience points!")

        if self.exp >= self.necessaryExp:
            self.LevelUp()
        
    def LevelUp(self):
        self.level += 1
        self.exp -= self.necessaryExp
        self.attack *= self.attackLevelUpIncrease
        self.defense *= self.defenseLevelUpIncrease
        self.speed *= self.speedLevelUpIncrease
        self.maxHealth *= self.maxHealthLevelUpIncrease
        self.health *= self.maxHealthLevelUpIncrease

        print("You leveled up!")
        print("Max HP : ", self.maxHealth)
        print("Attack : ", self.attack)
        print("Defense : ", self.defense)
        print("Speed : ", self.speed)