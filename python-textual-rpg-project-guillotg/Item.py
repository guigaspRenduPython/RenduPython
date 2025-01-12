import ItemType

class Item:
    def __init__(self, itemType):
        self.name = itemType.name
        self.target = itemType.target
        self.price = itemType.price
        self.affectedStat = itemType.affectedStat
        self.value = itemType.value

    @staticmethod
    def ChooseItem(player, enemy):
        print("Which item do you want to use?")
        choice = 0

        while choice != -1:
            for i in player.inventory:
                print("%d - " + i.name)
            print("-1 - quit")
            choice = input()

            if choice in range(0, len(player.inventory) - 1, 1):
                if player.inventory[choice].target == "self":
                    player.inventory[choice].UseItemOnSelf(player)

                elif player.inventory[choice].target == "enemy":
                    player.inventory[choice].UseItemOnEnemy(enemy)

                player.inventory.pop(choice)

            elif choice != -1:
                print("Invalid")
        
        if choice == -1:
            return False
        else:
            return True

    def UseItemOnSelf(self, player):
        if self.affectedStat == "attack":
            player.attackBuff += self.value
            print("You used a " + self.name + ".\nYour attacks are more potent!")

        elif self.affectedStat == "defense":
            player.defenseBuff += self.value
            print("You used a " + self.name + ".\nYou become more resilient!")

        elif self.affectedStat == "speed":
            player.speedBuff += self.value
            print("You used a " + self.name + ".\nYou feel more nimble!")
        
        elif self.affectedStat == "health":
            player.health += self.value
            print("You used a " + self.name + ".\nYour wounds seem to have healed!")

            if player.health > player.maxHealth:
                player.health = player.maxHealth
    
    def UseItemOnEnemy(self, enemy):
        if self.affectedStat == "attack":
            enemy.attackBuff -= self.value
            print("You used a " + self.name + ".\nThe " + enemy.name + "looks feeble!")

        elif self.affectedStat == "defense":
            enemy.defenseBuff -= self.value
            print("You used a " + self.name + ".\nThe " + enemy.name + "seems brittle!")

        elif self.affectedStat == "speed":
            enemy.speedBuff -= self.value
            print("You used a " + self.name + ".\nThe " + enemy.name + "has become sluggish!")
        
        elif self.affectedStat == "health":
            enemy.health -= self.value
            print("You used a " + self.name + ".\nThe " + enemy.name + "is hurt!\nIt takes %d damage.", self.value)

            if enemy.health > enemy.maxHealth:
                enemy.health = enemy.maxHealth

