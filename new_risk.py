#!/usr/bin/python
import sys
from random import randint
from dothat import lcd
from dothat import backlight

#to do: tune pimoroni hat.  break out dice modification into its own function as well as HAT display

#main place holders
asoldiers=0; dsoldiers=0
atotallost=0; dtotallost=0

def war():
    global asoldiers; global dsoldiers
    #sanity checks to make sure theres no funny business
    if len(sys.argv) != 3:
        print "Check arguments..." + '\n' + sys.argv[0] + ' ' + "ATTACKING_TROOPS " + "DEFENDING TROOPS "; quit()
    #these statements control how many dice can be thrown according to how many troops are available and can advance to the territory captured
    asoldiers = int(sys.argv[1]); dsoldiers = int(sys.argv[2])
    if (asoldiers >= 4):
        atd=3
    if (asoldiers == 3):
        atd=2
    if (asoldiers == 2):
        atd=1
    if (dsoldiers >=2):
        dtd=2
    if (dsoldiers == 1):
        dtd=1
        
    while True:
        #if attacking troops available is 1 then break because there are no reserves left to advance
        #going full kamikaze isnt in the rules :)
        if asoldiers == 3:
            atd=2
        if asoldiers == 2:
            atd=1
        if dsoldiers == 1:
            dtd=1
        if (asoldiers <= 1) or (dsoldiers <= 0):
            break
        roll(atd,dtd)
    lcd.clear(); lcd.set_contrast(50); backlight.set_graph(0.0)
    lcd.set_cursor_position(0,0); lcd.write("War is hell...")
    lcd.set_cursor_position(0,1); lcd.write("Offense Lost: " + str(atotallost))
    lcd.set_cursor_position(0,2); lcd.write("Defense Lost: " + str(dtotallost))
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
