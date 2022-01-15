import random
board = ['' for x in range(10)]
def printed(list):
    print(list[1] + " |", end="")
    print(list[2]+ " |",end="")
    print(list[3])
    print("--------")
    print(list[4] + " |", end="")
    print(list[5]+ " |",end="")
    print(list[6])
    print("--------")
    print(list[7] + " |", end="")
    print(list[8]+ " |",end="")
    print(list[9])

def insertPos(letter, pos):
    if spaceIsFree(pos):
        board[pos] = letter
    
def tic_tac():
    intro = input("Enter y to play or n to exit the game")

def spaceIsFree(pos):
  
    if(board[pos] == ''):
        return True
    return False
def isFull(b):
    for x in b:
        if(x == ''):
            return False
    return True

def IsWinner(b,l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[8] == l and b[9] == l) or
    (b[1] == l and b[4] == l and b[7] == l) or
    (b[2] == l and b[5] == l and b[8] == l) or
    (b[3] == l and b[6] == l and b[9] == l) or
    (b[1] == l and b[5] == l and b[9] == l) or
    (b[3] == l and b[5] == l and b[7] == l))


def playerMove(pos):
    while True:

        try:
            pos = int(pos)
            if spaceIsFree(pos):
                insertPos("X",pos)
                return True
            else:
                print("space is choosen before, Please enter another position")
        except:
            print("Please Enter valid number ")

def computerMove():
    possiblemove = [x for x, letter in enumerate(board) if letter == '' and x != 0]
    move = 0

    for let in ['X','O']:
        for i in possiblemove:
            boardcopy = board[:]
            boardcopy[i] = let
            if IsWinner(boardcopy,let):
                move = i
                return move
    
    openCorners = []
    for i in possiblemove:
        if i in [1,3,7,9]:
            openCorners.append(i)
    if len(openCorners)>0:
        move = random.choice(openCorners)
        return move

    openMid = []
    for i in possiblemove:
        if i in [2,5,8]:
            openMid.append(i)
    if len(openMid) > 0:
        move = random.choice(openMid)
        return move

    openSide = []
    for i in possiblemove:
        if i in [4,6]:
            openSide.append(i)
    if len(openSide)>0:
        move = random.choice(openSide)
        return move
    
printed(board)
while not isFull(board):
    choice = input("enter a number between 1 and 9\n ")
    playerMove(choice)
    insertPos("O",computerMove())
    printed(board)
    if IsWinner(board,"X"):
        winner = "X"
        break
    if IsWinner(board,"O"):
        winner = "O"
        break

if isFull(board):
    print("Wow it's an intense game!\n let's play again!")
if winner == "X":
    print("I didn't thought you're that good!")
if winner == "Y":
    print("Ezzzzzzzzzzzzzzz game \n Go play away Booooi!")

        

            
    




    
        


        

    




l = ["0","1","2","3","4","5","6","7","8"]
printed(board)
    

    
