import random, cmd, os, textwrap, time, sys

class player:
    def __init__(self,name,hp,atk,defense,xp):
        self.name = ''
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.xp = xp
class enemy:
    def __init__(self,name,hp,atk,defense):
        self.name = ''
        self.hp = hp
        self.atk = atk
        self.defense = defense
arun = player("arun",100,30,5,0)
nura = enemy("goblin",100,10,5)
roll = 0
def rolld100():
    roll = random.randint(1,10)
    if roll > 5:
        return True
    elif roll <= 5:
        return False

    
def attack():
    print ("You have done" , (arun.atk) , "dmg.")
    if roll == True:
        nura.hp = (nura.hp - arun.atk)
    elif roll == False:
        nura.hp = (nura.hp - (arun.atk-nura.defense))

def defend():
    print ("You've guarded, therefore the enemy only did" , (nura.atk-arun.defense) , "dmg.")
    nura.hp = (nura.hp - (nura.atk-arun.defense))

def enemyattack():
    print ("The enemy has attacked for" , (nura.atk) , "dmg.")
    print (nura.hp)
    
def enemydefend():
    print ("The enemy guarded and only took" , (arun.atk - nura.defense) , "dmg.")
    print (nura.hp)

def enemybattle():
    os.system ('cls')
    print ("You've found an enemy!")
    print ("What will you do?")
    print ("attack | inspect | defend")
    enemybattlechoice()

def enemybattlechoice():
    while nura.hp > 0:
        roll = rolld100()
        battlechoice = input(">")
        if battlechoice == ("attack"):
            attack()
        elif battlechoice == ("defend"):
            defend()
        else:
            print("that command hasn't been implemented yet, or doesn't exist please input a correct command")
            enemybattlechoice()
            break
        if roll == True:
            enemyattack()
        elif roll == False:
            enemydefend()
    enemydeath()
    
def enemydeath():
    os.system ('cls')
    print ("you've killed the enemy!!")
    print ("you've acquired 5 xp")
    arun.xp = arun.xp + 5
    levelup()
    time.sleep(1)
    wandering()
    

def levelup():

    if arun.xp == 10:
        print("You have levelled up!")
        arun.atk + 1
        arun.defense + 2
        arun.xp = 0

def wandering():
    nura.hp = 100
    os.system ('cls')
    print ("you are wandering after fighting a battle")
    choice = input("what do you want to do now?")
    if choice == "fight":
        enemybattle()