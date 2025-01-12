import PlayerCharacter
import Enemy
import Item
import ItemType
import random

class CombatManager:
    @staticmethod
    def CombatBehaviour(pChar, enemy):

        print("\n\n\n")

        print("You encounter a " + enemy.name + "! Prepare for battle!")
        
        while pChar.health > 0 and enemy.health > 0:
            print("\n\n")
            enemyTurnCounter = 0
            playerTurnCounter = 0
            while enemyTurnCounter < 100 or playerTurnCounter < 100:
                enemyTurnCounter += enemy.speed
                playerTurnCounter += pChar.speed

            if playerTurnCounter >= 100:
                playerTurnCounter = 0

                print(pChar.name + ":")
                print(pChar.health, " / ",pChar.maxHealth, " HP\nAttack : ", pChar.attack * pChar.attackBuff, "\nDefense : ", pChar.defense * pChar.defenseBuff, "\nSpeed : ", pChar.speed * pChar.speedBuff)

                validChoice = False
                
                while validChoice == False:
                    print("Choose your action:")
                    pA = input("1 - Attack \n 2 - Analyse \n 3 - Items \n 4 - Special action \n")

                    print("\n\n")
                    if pA == "1":
                        ap = pChar.attack * pChar.attackBuff
                        dp = enemy.defense * enemy.defenseBuff
                        calculatedDamage = ap * (1 + ((ap - dp) / ap))
                        if calculatedDamage < 1:
                            calculatedDamage = 1
                        print("You attack the " + enemy.name + "!\nYou inflict ", calculatedDamage, " damage!")
                        enemy.health -= calculatedDamage
                        validChoice = True

                    elif pA == "2":
                        print("You attentively observe the " + enemy.name + ".\nYou now know a lot more about it!")
                        print(enemy.name + ": \n", enemy.health, " / ", enemy.maxHealth, " HP\nAttack : ", enemy.attack * enemy.attackBuff, "\nDefense : ", enemy.defense * enemy.defenseBuff, "\n Speed : ", enemy.speed * enemy.speedBuff, "\n Speial Action - " + enemy.specialAction + "\n")
                        validChoice = True
                    
                    elif pA == "3":
                        if Item.ChooseItem(pChar, enemy) == True:
                            validChoice = True
                        else:
                            validChoice = False

                    elif pA == "4":
                        CombatManager.PlayerSpecialAction(pChar, enemy)
                        validChoice = True
                    
                    else:
                        print("Not a valid choice")

            if enemyTurnCounter >= 100:
                enemyTurnCounter = 0
                if enemy.specialActionTurnCounter == enemy.specialActionFrequency:
                    enemy.specialActionTurnCounter = 0
                    CombatManager.EnemySpecialAction(pChar, enemy)
                else:
                    ap = enemy.attack * enemy.attackBuff
                    dp = pChar.defense * pChar.defenseBuff
                    calculatedDamage = ap * (1 + ((ap - dp) / ap))
                    if calculatedDamage < 1:
                        calculatedDamage = 1
                    print("The " + enemy.name + " attacks you!\nYou take ", calculatedDamage, " damage!")
                    pChar.health -= calculatedDamage

                    if PlayerCharacter.PlayerCharacter.isKnightInCounter == True:
                        ap = pChar.attack * pChar.attackBuff + pChar.defense * pChar.defense
                        dp = enemy.defense * enemy.defenseBuff
                        calculatedDamage = ap * (1 + ((ap - dp) / ap))
                        if calculatedDamage < 1:
                            calculatedDamage = 1
                        print("You counter with great force!\nThe " + enemy.name + " receieves ", calculatedDamage, " damage!")
                        enemy.health -= calculatedDamage
                        validChoice = True
                        PlayerCharacter.PlayerCharacter.isKnightInCounter = False
                        pChar.defenseBuff -= 2
        
        if pChar.health <= 0:
            print("You have been vanquished by the " + enemy.name + "...")
            return "defeat"
        if enemy.health <= 0:
            print("You won!")
            return "victory"
        
    @staticmethod
    def PlayerSpecialAction(player, enemy):
        if player.specialAction == "Counter":
            if PlayerCharacter.PlayerCharacter.isKnightInCounter == False:
                PlayerCharacter.PlayerCharacter.isKnightInCounter = True
                player.defenseBuff += 2
                print("You enter a defensive stance and prepare for counter attacking.")
            else:
                print("You keep a steady defense, ready to counter.")

        elif player.specialAction == "Racket":
            calculatedDamage = player.attack * (1 + ((player.attack - enemy.defense) / player.attack))
            racketSuccessBuff = (player.speed / enemy.speed)
            calculatedDamage *= racketSuccessBuff * racketSuccessBuff
            enemy.health -= calculatedDamage

            racketSuccessResult = False
            if racketSuccessBuff >= 1.5:
                racketSuccessResult = True
            elif racketSuccessBuff >= 1:
                racketSuccessResult = random.choice([True, False])
            
            if racketSuccessResult == True:
                player.inventory.append(Item(ItemType.ItemTypeList[random.randint(0, len(ItemType.ItemTypeList) - 1)]))
            
        elif player.specialAction == "Life drain":
            remainingEnemyHealth = enemy.maxHealth / enemy.health
            lostPlayerHealth = player.maxHealth / (player.maxHealth - player.health)
            averageValue = remainingEnemyHealth + lostPlayerHealth / 2
            calculatedDamage = player.attack * averageValue
            enemy.health -= calculatedDamage
            player.health += calculatedDamage
        
        elif player.specialAction == "Power burst":
            PlayerCharacter.PlayerCharacter.wizardPowerBurstCounter += 1
            print("You take time to gather your mind and charge a powerful spell...")
            if PlayerCharacter.PlayerCharacter.wizardPowerBurstCounter >= 3:
                if PlayerCharacter.PlayerCharacter.wizardPowerBurstCounter < 4:
                    print("You feel a surge of energy and release a massive flow of magic!")
                    calculatedDamage == (player.attack * player.attackBuff * player.defenseBuff * player.speedBuff) * 2
                    print("The " + enemy.name + " recieves ", calculatedDamage, " damage!")
                    enemy.health -= calculatedDamage

                else:
                    print("The last assault took everything you had! You take some time to recuperate...")
                    PlayerCharacter.PlayerCharacter.wizardPowerBurstCounter = 0
        
        elif player.specialAction == "Unyielding rage":
            print("You puff your chest and roar with all your strenght!\nYou feel so angry your heart might lose out!")
            hpLoss = player.maxHealth / 10
            player.maxHealth -= hpLoss
            player.health -= hpLoss
            print("You lose ", hpLoss, " HP and max HP!")
            print("All your other stats increase !")
            player.attack *= (player.attack * player.attackBuff) / 20
            player.defense *= (player.defense * player.defenseBuff) / 20
            player.speed *= (player.speed * player.speedBuff) / 20
        
    @staticmethod
    def EnemySpecialAction(player, enemy):
        if enemy.specialAction == "Sciophobia":
            print("The shadow dashes towards you and dives into the ground! It fuses with your own shadow and pulls it back to itself!")
            print("You feel your strenght being heavily sapped while the Shadow seems to grow!")
            player.attackBuff -= 0.5
            player.defenseBuff -= 0.5
            player.speedBuff -= 0.5
            enemy.attackBuff += 2
            enemy.defenseBuff += 2
            enemy.speedBuff += 2

        elif enemy.specialAction == "Motivating howl":
            print("The Armored Orthrus harmonizes its howls in what looks like a battlecry.")
            print("You can feel its resolve burst! It grows stronger permanently!")
            if enemy.attackBuff < 1:
                enemy.attackBuff = 1.1
            if enemy.defenseBuff < 1:
                enemy.defenseBuff = 1.1
            if enemy.speedBuff < 1:
                enemy.speedBuff = 1.5

            enemy.attack *= enemy.attackBuff
            enemy.defense *= enemy.defenseBuff
            enemy.speed *= enemy.speedBuff

        elif enemy.specialAction == "Destructive roar":
            print("The Behemoth rears back and takes a deep breath...")
            print("It pushes an earth shattering roar! Your defenses are innefective!")
            ap = enemy.attack * enemy.attackBuff
            print("You take ", ap, " damage!")
            player.health -= ap
            print("You feel shaken and fragile!")
            player.defenseBuff -= 0.5
