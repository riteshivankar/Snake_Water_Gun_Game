# Snake Water Gun Game Againnnn !!!!!!!
import random

def gameWin(com , player):
    if com == player:
        return None
    
    elif com =='s':        
        if player=='w':
            return False
        elif player == 'g':
            return True
    elif com =='w':        
        if player=='g':
            return False
        elif player == 's':
            return True
    elif com =='g':
        if player=='s':
            return False
        elif player =='w':
            return True
        
print("Computer's turn : choose Snake(s), Water(w), Gun(g)? :")
randNo = random.randint(1,3)
if randNo ==1:
    com = 's'
elif randNo ==2:
    com = 'w'    
elif randNo ==3 :
    com= 'g'
player= input(print("Players's turn : choose Snake(s), Water(w), Gun(g)? : "))

print(f"Computer choose: {com}")
print(f"You choose: {player}")

a = gameWin(com , player)
if a == None:
    print("\tThe Game is Tie!")
elif a:
    print("\tYou Win!")
else:
    print("\tYou Lose!")
    
