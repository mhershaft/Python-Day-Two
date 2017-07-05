again="Yes"
while again=="Yes" or again=="yes":
    player=raw_input("Rock Paper Or Scissors?\n")
    import random
    computer=random.randint(0,2)
    if computer==0:
        print "My Choice is Rock!"
    elif computer==1:
        print "My Choice is Paper!"
    else:
        print "My Choice is Scissors!"
    if computer==0 and player=="Scissors" or computer==1 and player=="Rock" or computer==2 and player=="Paper":
        print "I Win!"
    elif computer==0 and player=="Paper" or computer==1 and player=="Scissors" or computer==2 and player=="Rock":
        print "You Win!"
    else:
        print "Tie!"
    again=raw_input("Want to Play Again?\n")
