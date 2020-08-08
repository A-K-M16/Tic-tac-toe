# putting random comment here
import sys
import os

class Board:
    def __initi__(self):
        self.board = []

    def Create_Board(self):
        self.board = [['1','2','3'],
                      ['4','5','6'],
                      ['7','8','9']]

    def Show_Board(self):
        print("\n")
        for i in range(3):
            print(self.board[i])
        print("\n")

    def Move_Board(self,move,team):
        self.board[move[0]][move[1]] = team
        return(1)

    def Check_win(self,line):
        if (line[0] == line[1] == line[2]):
            return(1)
        return(0)

    def Check_Full(self):
        for i in range(3):
            for j in range(3):
                if (self.board[i][j] != 'X' and self.board[i][j] != 'O'):
                    return(0)
        return(1)

    def Check_status(self):
        for i in range(3):
            if self.Check_win(self.board[i]):
                return(1)
        for i in range(3):
            if self.Check_win(list(j[i] for j in self.board)):
                return(1)
        if self.Check_win(list(self.board[i][i] for i in range(3))):
            return(1)
        if self.Check_win(list(self.board[i][2-i] for i in range(3))):
            return(1)
        if self.Check_Full():
            return(2)
        return(0)

    def Copy(self,b):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = b.board[i][j]

def move(B,P):
    a = 1
    while(a):
        m = []
        try:
            m.append(int(input("X - coordinate :")))
            m.append(int(input("Y - coordinate :")))
            if (B.board[m[0]][m[1]] == 'X' or B.board[m[0]][m[1]] =='O'):
                print("\nAlready filled")
            elif(-1<m[0]<3 and -1<m[1]<3):
                if (B.Move_Board(m,P)):
                    a = 0
            else :
                print("\nCoordinate not on board")
        except:
            print("\nNot a number")
            m = input("Wnat to quit (Y/N) :")
            if (m.upper() == "Y"):
                sys.exit()
            print("\n")

def Possible_move(board):
    a = []
    for i in range(3):
        for j in range(3):
            if (board.board[i][j] != 'X' and  board.board[i][j] !='O'):
                a.append((i,j))
    return a

def Possible_board(b,P,T,n):
    a = Possible_move(b)
    for i,j in a:
        b2 = Board()
        b2.Create_Board()
        b2.Copy(b)
        b2.Move_Board([i,j],P)
        if(b2.Check_status()==0):
            if(P=="X"):Possible_board(b2,"O",T,n+1)
            elif(P=="O"):Possible_board(b2,"X",T,n+1)
        elif(b2.Check_status()==1):
            if(P=="X"):T += 10
            else:T -= 10
        elif(b2.Check_status()==2):
            T += 0
    return(T)

def Ai_move(board):
    a = Possible_move(board)
    n = []
    k=[]
    r= 0
    for i,j in a:
        b2 =Board()
        b2.Create_Board()
        b2.Copy(board)
        b2.Move_Board([i,j],"X")
        if(b2.Check_status()):
            n.append([1000000,[i,j]])
            k.append(1000000)
        else:
            r = Possible_board(b2,"O",0,1)
            n.append([r,(i,j)])
            k.append(r)
    x = max(k)
    for i,j in n:
        if(i==x):
            return(j)


n = 0
B1 = Board()
B1.Create_Board()

while (n == 0):
    os.system('cls')
    B1.Show_Board()
    print("Enter the move for player - O")
    move(B1,"O")
    n = B1.Check_status()
    if(n == 2):
        print("\nNo  winner")
        break
    elif(n==1):
        print("\nWinner is O")
        break
    a = Ai_move(B1)
    B1.Move_Board(a,"X")
    n = B1.Check_status()
    if(n == 2):
        print("\nNo  winner")
        break
    elif(n==1):
        print("\nWinner is X")
        break
