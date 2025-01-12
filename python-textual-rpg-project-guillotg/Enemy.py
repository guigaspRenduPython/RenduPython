import EnemyType

class Enemy:
    def __init__(self, enemyType):
        self.name = enemyType.name
        self.maxHealth = enemyType.maxHealth
        self.health = self.maxHealth
        self.attack = enemyType.attack
        self.attackBuff = 1
        self.defense = enemyType.defense
        self.defenseBuff = 1
        self.speed = enemyType.speed
        self.speedBuff = 1
        self.goldGift = enemyType.goldGift
        self.expGift = enemyType.expGift
        self.specialAction = enemyType.specialAction
        self.specialActionTurnCounter = 0
        self.specialActionFrequency = enemyType.specialActionFrequency
