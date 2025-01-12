import json

class EnemyType:
    enemyTypeNormalList = list()
    enemyTypeEliteList = list()
    enemyTypeBossList = list()
    data = dict()
    @staticmethod
    def getInfoFromFile():
        with open('dataFiles/Enemies.json', 'r') as file:
            EnemyType.data = json.load(file)
        for et in EnemyType.data:
            eType = EnemyType(et)
            if eType.tier == "normal":
                EnemyType.enemyTypeNormalList.append(eType)
            if eType.tier == "elite":
                EnemyType.enemyTypeEliteList.append(eType)
            if eType.tier == "boss":
                EnemyType.enemyTypeBossList.append(eType)

    def __init__(self, name):
        self.name = name
        self.tier = EnemyType.data[name]["tier"]
        self.maxHealth = EnemyType.data[name]["maxHealth"]
        self.expGift = EnemyType.data[name]["expGift"]
        self.goldGift = EnemyType.data[name]["goldGift"]
        self.attack = EnemyType.data[name]["attack"]
        self.defense = EnemyType.data[name]["defense"]
        self.speed = EnemyType.data[name]["speed"]
        self.specialAction = EnemyType.data[name]["specialAction"]
        self.specialActionFrequency = EnemyType.data[name]["specialActionFrequency"]
