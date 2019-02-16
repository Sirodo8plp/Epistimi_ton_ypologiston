import random

def Answer(L):
    print(" ","0|1|2")
    c=0
    for i in range(0,3):
        print(c,A[i][0],A[i][1],A[i][2])
        c +=1

def HumanTurn(L):
    while True:
        row=int(input("Give the number of row(0-2): "))
        col=int(input("Give the number of column(0-2): "))
        if col>=0 and row<=2:
            if L[row][col]=='-':
                L[row][col]='X'
                break
            else:print("You cannot do that!")
        else:print("The numbers given must be between 0 and 2!Try again.")

def PCturn(L):
    while True:
        
        row=random.randint(0,3)
        col=random.randint(0,3)
        if row>=0 and row<=2 and col>=0 and col<=2:
            if L[row][col]=='-':
                L[row][col]='O'
                break

def CheckResult(L):    
    for i in range(0,3):
        if ((L[i][0]=='X' and L[i][1]=='X' and L[i][2]=='X') or (L[0][i]=='X' and L[1][i]=='X' and L[2][i]=='X')):
            print("Congratulations!You won!")
            return True
            
        elif ((L[i][0]=='O' and L[i][1]=='O' and L[i][2]=='O') or (L[0][i]=='O' and L[1][i]=='O' and L[2][i]=='O')):
            print("Oups!You lost.")
            return True

    Tie=True 
    for i in range(0,3):
        for j in range(0,3):
            if (L[i][j]!='X' and L[i][j]!='O'):
                Tie=False
                break
        if(Tie==False):break
    if(Tie==True):
        print("It's a tie!")
        return True

    
    if (L[0][0]=='X' and L[1][1]=='X' and L[2][2]=='X'):
        print("Congratulations!You won!")
        return True
    elif(L[0][0]=='O' and L[1][1]=='O' and L[2][2]=='O'):
        print("Oups!You lost.")
        return True
    elif(L[0][2]=='X' and L[1][1]=='X' and L[2][0]=='X'):
        print("Congratulations!You win!")
        return True
    elif(L[0][2]=='O' and L[1][1]=='O' and L[2][0]=='O'):
        print("Oups!You lost.")
        return True


    #se kathe alli periptosi to paixnidi sinexizetai
    return False
#===========end of functions,main program===========#

A = [['-' for x in range(3)] for y in range(3)]
while True:
    HumanTurn(A)
    Answer(A)
    victory=CheckResult(A)
    if(victory==False):
        PCturn(A)
        Answer(A)
    else:
        print("Game Ended!")
        answer=input("Would you like to play again?(Yes or No)")
        while (answer!='Yes' and answer!='No'):
            answer=input("Only Yes or No is an accepted answer!")
        if (answer=='Yes'):
            A = [['-' for x in range(3)] for y in range(3)]
        else:
            print("Thanks for playing!")
            break


        
        
    



    

             
    















