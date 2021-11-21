import copy
import alphaBetaPruning
import random

VICTORY=10**20 #The value of a winning board (for max) 
LOSS = -VICTORY #The value of a losing board (for max)
TIE=0 #The value of a tie
SIZE=4 #the length of winning seq.
COMPUTER=SIZE+1 #Marks the computer's cells on the board
HUMAN=1 #Marks the human's cells on the board
Continue=555
rows=6
columns=7

first_time=True

class game:
    board=[]
    size=rows*columns
    playTurn = HUMAN
    
     #Used by alpha-beta pruning to allow pruning

    '''
    The state of the game is represented by a list of 4 items:
        0. The game board - a matrix (list of lists) of ints. Empty cells = 0,
        the comp's cells = COMPUTER and the human's = HUMAN
        1. The heuristic value of the state.
        2. Whose turn is it: HUMAN or COMPUTER
        3. Number of empty cells
    '''

def create(s):
        #Returns an empty board. The human plays first.
        #create the board
        s.board=[]
        for i in range(rows):
            s.board = s.board+[columns*[0]]
        
        s.playTurn = HUMAN
        s.size=rows*columns
        s.val=0.00001
    
        #return [board, 0.00001, playTurn, r*c]     # 0 is TIE

def cpy(s1):
        # construct a parent DataFrame instance
        s2=game()
        s2.playTurn = s1.playTurn
        s2.size=s1.size
        s2.board=copy.deepcopy(s1.board)
        print("board ", s2.board)
        return s2
    
    
    
def value(s):
    '''
    /********************************* HUMAN **********************/
    '''
    # Horizontal win
    for c in range(columns - 3):
        for r in range(rows):
            if s.board[-(r + 1)][c] == HUMAN and s.board[-(r + 1)][ c + 1] == HUMAN and \
                    s.board[-(r + 1)][c + 2] == HUMAN and s.board[-(r + 1)][ c + 3] == HUMAN:
                return LOSS

    # Vertical win
    for r in range(rows - 3):
        for c in range(columns):
            if s.board[-(r + 1)][ c] == HUMAN and s.board[-(r + 2)][ c] == HUMAN and \
                    s.board[-(r + 3)][ c] == HUMAN and s.board[-(r + 4)][ c] == HUMAN:
                return LOSS

    # Diagonal win Positive Slope
    for c in range(columns - 3):
        for r in range(rows - 3):
            if s.board[-(r + 1)][ c] == HUMAN and s.board[-(r + 2)][ c + 1] == HUMAN and \
                    s.board[-(r + 3)][ c + 2] == HUMAN and s.board[-(r + 4)][ c + 3] == HUMAN:
                return LOSS

    # Diagonal Win Negative Slope
    for c in range(columns - 3):
        for r in range(rows - 3):
            if s.board[r][ c] == HUMAN and s.board[r + 1][ c + 1] == HUMAN and \
                    s.board[r + 2][ c + 2] == HUMAN and s.board[r + 3][ c + 3] == HUMAN:
                return LOSS
    '''
    /*********************************************** COMPUTER *********************************/         
    '''
    # Horizontal win
    for c in range(columns - 3):
        for r in range(rows):
            if s.board[-(r + 1)][c] == COMPUTER and s.board[-(r + 1)][ c + 1] == COMPUTER and \
                    s.board[-(r + 1)][c + 2] == COMPUTER and s.board[-(r + 1)][ c + 3] == COMPUTER:
                return VICTORY

    # Vertical win
    for r in range(rows - 3):
        for c in range(columns):
            if s.board[-(r + 1)][ c] == COMPUTER and s.board[-(r + 2)][ c] == COMPUTER and \
                    s.board[-(r + 3)][ c] == COMPUTER and s.board[-(r + 4)][ c] == COMPUTER:
                return VICTORY

    # Diagonal win Positive Slope
    for c in range(columns - 3):
        for r in range(rows - 3):
            if s.board[-(r + 1)][ c] == COMPUTER and s.board[-(r + 2)][ c + 1] == COMPUTER and \
                    s.board[-(r + 3)][ c + 2] == COMPUTER and s.board[-(r + 4)][ c + 3] == COMPUTER:
                return VICTORY

    # Diagonal Win Negative Slope
    for c in range(columns - 3):
        for r in range(rows - 3):
            if s.board[r][ c] == COMPUTER and s.board[r + 1][ c + 1] == COMPUTER and \
                    s.board[r + 2][ c + 2] == COMPUTER and s.board[r + 3][ c + 3] == COMPUTER:
                return VICTORY
    '''
    IF we can continue the game *********************?
   '''
    for i in range(rows):
        for j in range(columns):
            if s.board[i][j] != HUMAN and s.board[i][j] != COMPUTER:
                return Continue
    # When the board is full is a tie
    return TIE

def printState(s):
#Prints the board. The empty cells are printed as numbers = the cells name(for input)
#If the game ended prints who won.
        for r in range(rows):
            print("\n|",end="")
        #print("\n",len(s[0][0])*" --","\n|",sep="", end="")
            for c in range(columns):
                if s.board[r][c]==COMPUTER:
                    print("X|", end="")
                elif s.board[r][c]==HUMAN:
                    print("O|", end="")
                else:
                    print(" |", end="")

        print()

        for i in range(columns):
            print(" ",i,sep="",end="")

        print()
        
        val=value(s)

        if val==VICTORY:
            print("I won!")
        elif val==LOSS:
            print("You beat me!")
        elif val==TIE:
            print("It's a TIE")



def isFinished(s):
#Seturns True iff the game ended
        return value(s) in [LOSS, VICTORY, TIE] or s.size==0


def isHumTurn(s):
#Returns True iff it is the human's turn to play
        return s.playTurn==HUMAN
    


def decideWhoIsFirst(s):
#The user decides who plays first
        if int(input("Who plays first? 1-me / anything else-you : "))==1:
            s.playTurn=COMPUTER
        else:
            s.playTurn=HUMAN
            
        return s.playTurn
        

def makeMove(s, c):
#Puts mark (for huma. or comp.) in col. c
#and switches turns.
#Assumes the move is legal.

        r=0
        while r<rows and s.board[r][c]==0:
            r+=1

        s.board[r-1][c]=s.playTurn # marks the board
        s.size -= 1 #one less empty cell
        if (s.playTurn == COMPUTER ):
            s.playTurn = HUMAN
        else:
            s.playTurn = COMPUTER

   
def inputMove(s):
#Reads, enforces legality and executes the user's move.

        #self.printState()
        flag=True
        while flag:
            c=int(input("Enter your next move: "))
            if c<0 or c>=columns or s.board[0][c]!=0:
                print("Illegal move.")

            else:
                flag=False
                makeMove(s,c)

        
def getNext(s):
#returns a list of the next states of s
        ns=[]
        for c in list(range(columns)):
            print("c=",c)
            if s.board[0][c]==0:
                print("possible move ", c)
                tmp=cpy(s)
                makeMove(tmp, c)
                print("tmp board=",tmp.board)
                ns+=[tmp]
                print("ns=",ns)
        print("returns ns ", ns)
        return ns

def inputComputer(s):    
        return alphaBetaPruning.go(s)
