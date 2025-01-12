import random

import PlayerClass
import PlayerCharacter
import EnemyType
import Enemy
import CombatManager
import BranchingPaths
import Shop
import Item
import ItemType

class GameStateManager:
    data = dict()
    
    def __init__(self):
        self.state = "startGame"
        self.player = PlayerCharacter.PlayerCharacter("defaultPlayer", PlayerClass.PlayerClass.classesDict["Knight"])
        self.text = GameStateManager.data
        self.stateList = list()
        self.currentStage = -1
        self.currentBranch = "branch1"

    def GameUpdate(self):
        if self.state == "startGame":
            self.StartGame()
        elif self.state == "combat":
            self.Combat(0)
        elif self.state == "elite":
            self.Combat(1)
        elif self.state == "boss":
            self.Combat(2)
        elif self.state == "shop":
            self.Shop()
        elif self.state == "branch":
            self.Branch()
        elif self.state == "treasure":
            self.Treasure()
        elif self.state == "rest":
            self.Rest()
        elif self.state == "defeat":
            self.Defeat()

    def StartGame(self):
        pName = input("Choose your character's name: ").strip()
        print("Choose your character's class: ")
        print("Knight : High defense, High HP and moderate attack. Low speed. Special action: Counter - Greatly increase defense for a single turn and if an attack hits you, you retaliate with both your attack and defense stats. If you don't get hit, you pass your turns until you are.")
        print("Thief: High speed, moderate attack, low defense and HP. Special action: Racket - Deal damage while attempting to steal an item from the enemy. Success rate and damage are determined by the difference in speed with the enemy.")
        print("Sage: moderate speed, low attack and defense, moderate HP. Special action: Life drain - Deals damage to the enemy ignoring their defense and averaging your lost health percentage with their remaining health percentage.")
        print("Wizard: moderate speed, low attack, moderate defense and low HP. Special action: Power burst - Charge for 2 turns to release an extremely powerful attack on the 3rd use that ignores defense and gets boosted further by any of your current buffs. Will allow the enemy to attack 2 turns in a row afterwards.")
        print("Barbarian : moderate attack, very high HP, moderate defense and moderate speed. Special Action: Unyielding rage - Permanently reduce your total HP by a tenth to permanently increase all your other stats by a twentieth. You only gain HP on level ups. Buffs and debuffs are counted during the calculations.")
        pClass = input().strip()

        print(PlayerClass.PlayerClass.classesDict.keys())

        if pClass in PlayerClass.PlayerClass.classesDict.keys():
            self.player = PlayerCharacter.PlayerCharacter(pName, PlayerClass.PlayerClass.classesDict[pClass])
    
        while self.player.name == "defaultPlayer":
            pClass = input("Not valid class: ").strip()
            if pClass in PlayerClass.PlayerClass.classesDict.keys():
                self.player = PlayerCharacter.PlayerCharacter(pName, PlayerClass.PlayerClass.classesDict[pClass])
            
        
        self.state = "branch"
        self.GameUpdate()
    
    def Branch(self):
        print("\n\n\n")
        print("You arrive at a fork in the road. 3 paths in front of you.")
        print("In the middle of the room, what looks like a bird bath full of blood and an ornate knife rest. On the blade you can read the words: <<Knowledge requires sacrifice>>")
        print("You can see what is awaiting in the next 3 rooms but no further.")

        hasCleared = False
        valid = False

        print(self.currentStage + 1)
        
        while valid == False :
            print("Path 1: -" + BranchingPaths.BranchingPaths.branches["branch1"][self.currentStage + 1])
            print("Path 2: -" + BranchingPaths.BranchingPaths.branches["branch2"][self.currentStage + 1])
            print("Path 3: -" + BranchingPaths.BranchingPaths.branches["branch3"][self.currentStage + 1])
            
            print("What do you choose to do ?")
            print("1 - Take the 1st path")
            print("2 - Take the 2nd path")
            print("3 - Take the 3rd path")
            print("4 - Sacrifice health to the pool (",self.player.maxHealth / 10,")")

            choice = input("Your choice :").strip()

            if choice == "1":
                print("You continue forward in the 1st path")
                self.currentStage += 1
                self.state = BranchingPaths.BranchingPaths.branches["branch1"][self.currentStage]
                valid = True

            elif choice == "2":
                print("You continue forward in the 2nd path")
                self.currentStage += 1
                self.state = BranchingPaths.BranchingPaths.branches["branch2"][self.currentStage]
                valid = True

            elif choice == "3":
                print("You continue forward in the 3rd path")
                self.currentStage += 1
                self.state = BranchingPaths.BranchingPaths.branches["branch3"][self.currentStage]
                valid = True

            elif choice == "4":
                if hasCleared == False:
                    print("You slice your hand open over the oversized chalice and let some blood drip into it.")
                    self.player.health -= 5
                    print("The liquid thins and clears to reveal you your paths:")
                    i = 1
                    for p in BranchingPaths.BranchingPaths.branches:
                        print("Path", i, " -")
                        print(BranchingPaths.BranchingPaths.branches["branch1"])
                        i += 1
                else:
                    print("You can already see what awaits you.")
            else:
                print("Invalid choice")
        
        self.GameUpdate()
    
    def Combat(self, combatTier):
        print("\n\n\n")

        self.currentStage += 1

        i = 0
        fightResult = "not set"

        if combatTier == 0:
            i = random.randint(0, len(EnemyType.EnemyType.enemyTypeNormalList) - 1)
            enemy = Enemy.Enemy(EnemyType.EnemyType.enemyTypeNormalList[i])
        elif combatTier == 1:
            i = random.randint(0, len(EnemyType.EnemyType.enemyTypeEliteList) - 1)
            enemy = Enemy.Enemy(EnemyType.EnemyType.enemyTypeEliteList[i])
        elif combatTier == 2:
            i = random.randint(0, len(EnemyType.EnemyType.enemyTypeBossList) - 1)
            enemy = Enemy.Enemy(EnemyType.EnemyType.enemyTypeBossList[i])

        fightResult = CombatManager.CombatManager.CombatBehaviour(self.player, enemy)

        if fightResult == "victory":
            self.player.FightRewards(enemy.expGift, enemy.goldGift)
            self.state = BranchingPaths.BranchingPaths.branches[self.currentBranch][self.currentStage]

        if fightResult == "defeat":
            self.state = "defeat"
        
        self.GameUpdate()

    def Shop(self):
        self.currentStage += 1

        newShop = Shop.Shop()
        newShop.ShopBehaviour(self.player)

        self.state = BranchingPaths.BranchingPaths.branches[self.currentBranch][self.currentStage]
        self.GameUpdate()
    
    def Rest(self):
        self.currentStage += 1

        print("You seem to find a calm room in the cave.\nYou decide to dedicate a few moments to respite.")
        print("You recover 3 fourth of your total HP.")

        self.state = BranchingPaths.BranchingPaths.branches[self.currentBranch][self.currentStage]
        self.GameUpdate()

    def Treasure(self):
        self.currentStage += 1

        print("This room is calm, but it shows traces of previous occupants, long gone without a trace as to where...")
        print("You search the rubles and find a few things. Some useless but some...")

        iN = random.randint(1, 3)
        x = 0 
        while x < iN:
            x += 1
            randI = random.randint(0, len(ItemType.ItemType.itemTypeList) - 1)
            newItem = Item.Item(ItemType.ItemType.itemTypeList[randI])
            print("You find a " + newItem.name + "!")        

        print("Nothing of interest seems to be left...\nYou leave with your newfound goods.")

        self.state = BranchingPaths.BranchingPaths.branches[self.currentBranch][self.currentStage]
        self.GameUpdate()

    def Defeat(self):
        print("End of the game")