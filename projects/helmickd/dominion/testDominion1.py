# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 2020

@author: helmickd
"""

import Dominion
import random
from collections import defaultdict
import testUtility

#Get player names
player_names = testUtility.getPlayerNames()

#number of curses and victory cards
#nV, nC = testUtility.GetNumberOfCurseAndVictoryCards(player_names)

#BUG: Number of victory & curse cards is not determined by # of players
nV, nC = 8, 10

#Define box
box = testUtility.getBoxes(nV)

supply_order = testUtility.GetSupplyOrder()

#Set up supply
supply = testUtility.GetSupply(box, player_names, nV, nC)

#initialize the trash
trash = []

#Construct the Player objects
players = testUtility.GetPlayers(player_names)

#Play the game
turn  = 0
while not Dominion.gameover(supply):
    turn += 1    
    print("\r")    
    for value in supply_order:
        print (value)
        for stack in supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))
    print("\r")
    for player in players:
        print (player.name,player.calcpoints())
    print ("\rStart of turn " + str(turn))    
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)
            

#Final score
dcs=Dominion.cardsummaries(players)
vp=dcs.loc['VICTORY POINTS']
vpmax=vp.max()
winners=[]
for i in vp.index:
    if vp.loc[i]==vpmax:
        winners.append(i)
if len(winners)>1:
    winstring= ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0],'wins!'])

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)