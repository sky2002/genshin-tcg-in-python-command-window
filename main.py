#before game, toss a coin to decide who moves first.
#first, draw 5 cards and characters are available to both sides.
#then change 0-5 of 5 cards.
#
#gameloop:
#
#stage 1: roll
#
#roll 8 octahedron dices.
#then one can reroll any amount between 0-8.
#and game starts.
#some card can change something in this part.
#
#stage 2: calculate for cards
#
#some cards may have some effect on this time.
#
#stage 3: play
#the first-move one could do these things before their dice went out or choose to end the round in advance:
#use a card
#change a character in action
#use the character's basic attack, skill or elemental burst
#after doing one of these above the opponent will move
#until both declare to end the round
#
#stage 4: end-round
#
#calculate all summoned objects and cards which have a effect at this stage
#when it's round 15, end the game with a tie.
#draw 2 cards for each player. if one holds 10 cards, excess cards will be burnt.
import gameloop
import random

if __name__ == '__main__':
    a=gameloop.player()
    b=gameloop.player()
    first_move_ind=random.randint(0,1)
    if first_move_ind==0:
        gameloop.gameloop(0,a,b)
    else:
        gameloop.gameloop(1,a,b)