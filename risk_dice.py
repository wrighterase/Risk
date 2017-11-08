#!/usr/bin/python
from __future__ import print_function
import sys
from random import randint
from dothat import lcd
from dothat import backlight
import prettytable


#to do:  add pi HAT touch menu options.  start an http server and print all console output to http PUTs

#main place holders
asoldiers=0; dsoldiers=0
atotallost=0; dtotallost=0
atotaldice=0; dtotaldice=0

def clear_all():
    #clear all variables after each roll
    global atotaldice, dtotaldice, asoldiers, dsoldiers, atotallost, dtotallost
    asoldiers=0; dsoldiers=0
    atotallost=0; dtotallost=0
    atotaldice=0; dtotaldice=0

def single(atd,dtd):
    #sanity checks to make sure theres no funny business
    if (atd < 1) or (atd > 3):
        print("Check attacking dice...")
	#quit()
    elif (dtd < 1) or (dtd > 2):
        print("Check defending dice...")
	#quit()
    else:
        roll(atd,dtd)
    #stats()
    tophat()
    clear_all()
    #sys.exit()
def auto(autoa, autod):
    #global variables store total number of attackers and defenders
    global asoldiers, dsoldiers
    asoldiers=autoa; dsoldiers=autod
    #since this is an auto attack.  roll until someone loses
    while True:
        if (asoldiers >= 4): atd=3
        if (asoldiers == 3): atd=2
        if (asoldiers == 2): atd=1
        if (dsoldiers >=2): dtd=2
        if (dsoldiers == 1): dtd=1        
        if (asoldiers <= 1) or (dsoldiers <= 0):
            break
        roll(atd,dtd)
    #print results to Pi HAT
    tophat()
    print("\nAttacker total loss: " + str(atotallost) + "\nDefender total loss: " + str(dtotallost) + '\n')
    #stats()
    clear_all()
    #sys.exit()

def stats():
    #print out statistics of each roll.  probably wont be use long term as its not needed.
    a = prettytable.PrettyTable(["Attacker Lost", "Attacking Dice", "% Lost"])
    a.add_row([atotallost, atotaldice, (float(atotallost) / float(atotaldice)*100)])
    d = prettytable.PrettyTable(["Defender Lost", "Defending Dice", "% Lost"])
    d.add_row([dtotallost, dtotaldice, (float(dtotallost) / float(dtotaldice)*100)])
    print (a); print (d)

def tophat():
    #controls the raspberry pi HAT display
    lcd.clear(); lcd.set_contrast(50); backlight.set_graph(0)
    if (asoldiers > dsoldiers) and (atotallost != 1):
        backlight.rgb(0,255,0)
    elif (asoldiers <= dsoldiers):
        backlight.rgb(255,0,0)
    lcd.set_cursor_position(0,0); lcd.write("War is hell...")
    lcd.set_cursor_position(0,1); lcd.write("Offense Lost: " + str(atotallost))
    lcd.set_cursor_position(0,2); lcd.write("Defense Lost: " + str(dtotallost))

def roll(A,D):
    global atotaldice, dtotaldice, asoldiers, dsoldiers, atotallost, dtotallost
    #set the list for numbers thrown and variables to "collect the dead"
    attacker_dice = []; defender_dice = []; atroops=0; dtroops=0
    #lets go to war!
    while len(attacker_dice) != A:
        attacker_dice.append(randint(1,6))
        atotaldice+=1
    while len(defender_dice) != D:
        defender_dice.append(randint(1,6))
        dtotaldice+=1
        
    #reverse sort the lists of numbers thrown so a high die to high die comparison can be made
    attacker_dice.sort(reverse=True), defender_dice.sort(reverse=True)

    print("Attacking troops: " + str(asoldiers) + ' ' + "Defending troops: " + ' ' + str(dsoldiers))
    print("Attacker dice: " + str(attacker_dice) + '\n' + "Defender dice: " + str(defender_dice))
    
    #for each attacker die thrown, compare the attacker & defender and deduct a troop from the losing side with a tie going to the defender.
    #if the index is 2 (the 3rd die) break since a defender can only throw two dice.
    for idx in range(len(attacker_dice)):
        if (idx == 2):
            break
        if defender_dice[idx] >= attacker_dice[idx]:
            atroops+=1
        else:
            dtroops+=1
        if len(defender_dice) == 1:
            break
    print("Attacker lost: " + str(atroops) + " troops\n" + "Defender lost: " + str(dtroops) + " troops\n")
    asoldiers-=atroops; dsoldiers-=dtroops
    atotallost+=atroops; dtotallost+=dtroops

def mode():
    global asoldiers, dsoldiers
    if len(sys.argv) != 4:
        print("Check attack mode...\n" + sys.argv[0] + " MODE" + " ATTACKING_OPTION" + " DEFENDING_OPTION\n")
        print("e.g. " + sys.argv[0] + " auto" + " ATTACKING_TROOPS" + " DEFENDING_TROOPS")
        print("e.g. " + sys.argv[0] + " single" + " ATTACKING_DICE" + " DEFENDING_DICE")
        quit()
    if sys.argv[1] == 'auto' and int(sys.argv[2]) <= 1:
        print ("Attacking troop number must be greater than one...")
        #quit()
    if sys.argv[1] == 'auto':
        autoa=int(sys.argv[2])
        autod=int(sys.argv[3])
        auto(autoa,autod)
    if sys.argv[1] == 'single':
        atd=int(sys.argv[2])
        dtd=int(sys.argv[3])
        single(atd,dtd)
        
if __name__ == "__main__":
    mode()
