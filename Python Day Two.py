import random
import string
com_score=0
player_score=0
print "Welcome to Rock Paper Scissors!"
print "Let's Play!"
again="Yes"
while again=="Yes" or again=="yes":
    player=raw_input("Rock Paper Or Scissors?\n")
    player=str.lower(player)
    computer=random.randint(0,2)
    if computer==0:
        print "My Choice is Rock!"                       #str.lower(bhruvbiv)
    elif computer==1:
        print "My Choice is Paper!"
    else:
        print "My Choice is Scissors!"
    if computer==0 and player=="scissors" or computer==1 and player=="rock" or computer==2 and player=="paper":
        print "I Win!"
        com_score = com_score + 1
    elif computer==0 and player=="paper" or computer==1 and player=="scissors" or computer==2 and player=="rock":
        print "You Win!"
        player_score = player_score + 1
    else:
        print "Tie!"
    again=raw_input("Want to Play Again?\n")
    if again=="No" or again=="no":
        print "Your score was " , player_score , "."
        print "My score was " , com_score , "."
    if again=="No" or again=="no" and com_score > player_score:
         print "I Win!"
    elif again=="No" or again=="no" and com_score < player_score:
        print "You Win!"
    elif again=="No" or again=="no" and com_score == player_score:
        print "We're Tied!"
