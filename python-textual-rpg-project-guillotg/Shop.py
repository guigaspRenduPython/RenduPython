import json
import random
import Item
import ItemType
import PlayerCharacter

class Shop:
    data = dict()

    def __init__(self):
        self.itemsList = list()
        self.text = Shop.data
        self.mysteriousMixturePrice = 0

        self.itemsList.append(Item.Item(ItemType.ItemType.itemTypeList[0]))
        while len(self.itemsList) < 8:
            self.itemsList.append(Item.Item(ItemType.ItemType.itemTypeList[random.randint(0, len(ItemType.ItemType.itemTypeList) - 1)]))

    def ShopBehaviour(self, player):
        print("Welcome to the cave diver's respite!\nWhat can I do for you?")

        self.mysteriousMixturePrice = player.level * (player.necessaryExp - player.exp) * 10

        quit = False

        while quit == False:
            print("1 - Buy\n2 - Sell\n3 - Some advice?\n4 - Try the mixture for ", self.mysteriousMixturePrice, " gold\n5 - Leave\n")
            choice = input().strip()

            if choice == "1":
                self.Buy(player)
            elif choice == "2":
                self.Sell(player)
            elif choice == "3":
                self.Advice()
            elif choice == "4":
                self.Mixture(player)
            elif choice == "5":
                print("See you around! Hopefully, HAHAHA!")
                return
            else:
                print("Stop wasting my time and tell me what you want!")
    

    def Buy(self, player):
        print("Want so see what's in stock?")
        iN = 0
        choice = 0

        while choice != -1:
            iN = 0
            for i in self.itemsList:
                print(iN ," - " + i.name + " - ", i.price, " gold")
                iN += 1
            choice = int(input("Anything that catches your eye? (-1 to quit)\n"))

            if choice in range(0, len(self.itemsList) - 1, 1):
                if player.gold < self.itemsList[choice].price:
                    print("The house doesn't do credit!")
                else:
                    print("Thank you for your patronage!")
                    player.gold -= self.itemsList[choice].price
                    player.inventory.append(self.itemsList[choice])
                    self.itemsList.pop(choice)
            elif choice != -1:
                print("Are you going to buy something or not?")

    
    def Sell(self, player):
        print("Happy to bargain!")
        iN = 0
        choice = 0

        while choice != -1:
            iN = 0
            for i in player.inventory:
                print(iN ," - " + i.name + " - ", i.price * 0.75, " gold")
                iN += 0
            choice = int(input("What do you want to sell?\n"))

            if choice in range(0, len(player.inventory) - 1, 1):
                print("You won't get a better deal elsewhere!")
                player.gold += player.inventory[choice].price * 0.75
                self.itemsList.append(player.inventory[choice])
                player.inventory.pop(choice)
            else:
                print("More dealing, less nonsense!")

    def Advice(self):
        print("Not done yet")

    def Mixture(self, player):
        if player.gold < self.mysteriousMixturePrice:
            print("The house doesn't do credit!")
        else:
            player.gold -= self.mysteriousMixturePrice
            print("The concoction is clear, light and has no odor.\n Ingesting it gives you a strange headache and a general discomfort... But also a refreshing and strenghthening feeling.\n")
            player.LevelUp()
            player.exp = 0
    
    