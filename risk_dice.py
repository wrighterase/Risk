import sys
from random import randint

def roll(A,D):
    attacker_dice = []; defender_dice = []
    atroops=0; dtroops=0
    #print "Attacker rolling: " + str(A) + '\n' + "Defender rolling: " + str(D)
    while len(attacker_dice) != A:
        attacker_dice.append(randint(1,6))
    while len(defender_dice) != D:
        defender_dice.append(randint(1,6))
    attacker_dice.sort(reverse=True), defender_dice.sort(reverse=True)
    print "Attacker dice: " + str(attacker_dice) + '\n' + "Defender dice: " + str(defender_dice)
    if defender_dice[0] >= attacker_dice[0]:
        atroops+=1
    else:
        dtroops+=1
    if defender_dice[1] >= attacker_dice[1]:
        atroops+=1
    else:
        dtroops+=1
    print "Attacker lost: " + str(atroops) + " troops" + '\n' + "Defender lost: " + str(dtroops) + " troops"


if len(sys.argv) != 3:
    print "Check number of dice being rolled..."
    
if (int(sys.argv[1]) < 1) or (int(sys.argv[1]) > 3):
    print "Check attacking dice..."
elif (int(sys.argv[2]) < 1) or (int(sys.argv[2]) > 2):
    print "Check defending dice..."
else:
    atd = int(sys.argv[1])
    dtd = int(sys.argv[2])
    roll(atd,dtd)
