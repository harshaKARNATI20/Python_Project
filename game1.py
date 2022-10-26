import random

comp=random.randint(1,3)
if comp==1:
    comp="r"
elif comp==2:
    comp="p"
else:
    comp="s"

player = input("Choose Rock(r) paper(p) or scissors(s)")
print("Computer choose : ",comp)

def youWin(comp,player):
    if comp==player:
        return None
    elif comp=="r":
        if player=="p":
            return True
        elif player=="s":
            return False
    elif comp=="p":
        if player=="s":
            return True
        elif player=="r":
            return False
    elif comp=="s":
        if player=="r":
            return True
        elif player=="p":
            return False
if youWin(comp,player) == True:
    print("You Win")
elif youWin(comp,player) == False:
    print("You Lose")
else:
    print("Tie")






















