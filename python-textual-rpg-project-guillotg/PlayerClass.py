import json

class PlayerClass:
    classesDict = dict()
    data = dict()
    @staticmethod
    def getInfoFromFile():
        with open('dataFiles/StartingClass.json', 'r') as file:
            PlayerClass.data = json.load(file)
        for c in PlayerClass.data:
            PlayerClass.classesDict[c] = PlayerClass(c)

    def __init__(self, name):
        self.name = name
        self.maxHealth = PlayerClass.data[name]["maxHealth"]
        self.maxHealthLevelUpIncrease = PlayerClass.data[name]["maxHealthLevelUpIncrease"]
        self.startingGold = PlayerClass.data[name]["startingGold"]
        self.attack = PlayerClass.data[name]["attack"]
        self.defense = PlayerClass.data[name]["defense"]
        self.speed = PlayerClass.data[name]["speed"]
        self.attackLevelUpIncrease = PlayerClass.data[name]["attackLevelUpIncrease"]
        self.defenseLevelUpIncrease = PlayerClass.data[name]["defenseLevelUpIncrease"]
        self.speedLevelUpIncrease = PlayerClass.data[name]["speedLevelUpIncrease"]
        self.specialAction = PlayerClass.data[name]["specialAction"]
