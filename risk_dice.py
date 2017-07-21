#!/usr/bin/python
import sys
from random import randint

#to do:  ability to specify troops as arguments
asoldiers=10; dsoldiers=8
atotallost=0; dtotallost=0

def war():
    #sanity checks to make sure theres no funny business
	if len(sys.argv) != 3:
		print "Check arguments..." + '\n' + sys.argv[0] + ' ' + "ATTACKING_DICE " + "DEFENDING DICE"; quit()
	if (int(sys.argv[1]) < 1) or (int(sys.argv[1]) > 3):
		print "Check attacking dice..."; quit()
	elif (int(sys.argv[2]) < 1) or (int(sys.argv[2]) > 2):
		print "Check defending dice..."; quit()
	else:
		atd = int(sys.argv[1])
		dtd = int(sys.argv[2])
	while True:
            #these statements control how many dice can be thrown according to how many troops are available and can advance to the territory captured
            if asoldiers == 3:
                atd=2
            if asoldiers == 2:
                atd=1
            if dsoldiers == 1:
                dtd=1
            #if attacking troops available is 1 then break because there are no reserves left to advance
            #going full kamikaze isnt in the rules :)
            if (asoldiers <= 1) or (dsoldiers <= 0):
                break
            roll(atd,dtd)
	print '\n' + "Attacking troops lost: " + str(atotallost) + '\n' + "Defending troops lost: " + str(dtotallost) + '\n'
	sys.exit()

def roll(A,D):
    #set the list for numbers thrown and variables to "collect the dead"
    attacker_dice = []; defender_dice = []; atroops=0; dtroops=0
    global asoldiers; global dsoldiers; global atotallost; global dtotallost

    #lets go to war!
    while len(attacker_dice) != A:
        attacker_dice.append(randint(1,6))
    while len(defender_dice) != D:
        defender_dice.append(randint(1,6))

    #reverse sort the lists of numbers thrown so a high die to high die comparison can be made
    attacker_dice.sort(reverse=True), defender_dice.sort(reverse=True)

    print "Attacking troops: " + str(asoldiers) + ' ' + "Defending troops: " + ' ' + str(dsoldiers)
    print "Attacker dice: " + str(attacker_dice) + '\n' + "Defender dice: " + str(defender_dice)
    
    #for each attacker die thrown, compare the attacker & defender and deduct a troop from the losing side with a tie going to the defender.
    #if the index is 2 (the 3rd die) break since a defender can only throw two dice.
    for idx in range(len(attacker_dice)):
    	if (idx == 2):
            break
    	if defender_dice[idx] >= attacker_dice[idx]:
            atroops+=1
    	else:
            dtroops+=1
        #if a defender has only thrown one die then break after the roll.  this if statement is necessary because if the amount of dice thrown
        #by the attacker is greater than the amount thrown by the defender then an index out of range error is thrown.
        #this result is the same no matter if evaluating the attacking or defending dice index.
        if len(defender_dice) == 1:
            break
    print "Attacker lost: " + str(atroops) + " troops" + '\n' + "Defender lost: " + str(dtroops) + " troops" + '\n'
    asoldiers-=atroops; dsoldiers-=dtroops
    atotallost+=atroops; dtotallost+=dtroops

war()