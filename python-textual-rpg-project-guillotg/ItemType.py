import json

class ItemType:
    data = dict()
    itemTypeList = list()
    @staticmethod
    def getInfoFromFile():
        with open('dataFiles/ItemTypes.json', 'r') as file:
            ItemType.data = json.load(file)
        for it in ItemType.data:
            ItemType.itemTypeList.append(ItemType(it))
        
    def __init__(self, name):
        self.name = name
        self.target = ItemType.data[name]["target"]
        self.price = ItemType.data[name]["price"]
        self.affectedStat = ItemType.data[name]["affectedStat"]
        self.value = ItemType.data[name]["value"]