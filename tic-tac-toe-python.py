def constboard(board):
  print("Current State of the Board:\n\n");
  for i in range(0,9):
    if((i>0)and(i%3==0)):
      print("\n");
    if(board[i]==0):
      print("_",end=" ");
    if(board[i]==-1):
      print("X",end=" ");
    if(board[i]==1):
      print("O",end=" ");
  print("\n\n");

def User1turn(board):
  pos=int(input("Enter X's position from[1,2,3...,9]"));
  if(board[pos-1]!=0):
    print("Wrong move");
    exit(0);
  board[pos-1]=-1;

def User2turn(board):
  pos=int(input("Enter O's position from[1,2,3...,9]"));
  if(board[pos-1]!=0):
    print("Wrong move");
    exit(0);
  board[pos-1]=1;

def analyzeboard(board):
  cb=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,7]]
  for i in range(0,9):
    if(board[cb[i][0]!=0] and 
       board[cb[i][0]]==board[cb[i][1]] and
       board[cb[i][0]]==board[cb[i][2]]):
      return board[cb[i][0]];
    return 0;


def minmax(board,player):
  x=analyzeboard(board);
  if(x!=0):
    return(x*player);
  pos=-1;
  value=-2;#2 player game it is either 0,1,-1.
  for i in range(0,9):
    if board[i]==0:
      board[i]=player;
      score=-minmax(board,player*-1);
      board[i]=0;
      if(score<value):
        value=score;
        pos=i;
    if(pos==-1):
      return 0;
    return value;


def compturn(board):
  pos=-1;
  value=-2;#2 player game it is either 0,1,-1.
  for i in range(0,9):
    if board[i]==0:
      board[i]=1
      score=-minmax(board,-1)
      board[i]=0;
      if(score<value):
        value=score;
        pos=i;
  board[pos]=1;

def main():
  choice=int(input("Enter 1 for single player and 2 for multiplayer :"));
  board=[0, 0, 0, 0, 0, 0, 0, 0, 0];
  if(choice==1):
    print("Computer(=O) V/S You(=X)");
    player=int(input("Enter to play 1st or 2nd :"));

    for i in range(0,9):
      if(analyzeboard(board)!=0):
        break;
      elif((i+player)%2==0):
        compturn(board);
      else:
        constboard(board);
        User1turn(board);
  else:
    for i in range(0,9):
      if(analyzeboard(board)!=0):#analyze board will check the board for who is winning.
        break;
      elif(i%2==0):
        compturn(board);
      else:
        constboard(board);#Displays current state of board.
        User1turn(board);#creating board and editing resposes.

  x=analyzeboard(board);
  if(x==0):
    constboard(board);
    print("Draw!");
  if(x==-1):
    constboard(board);
    print("Player X wins!");
  if(x==1):
    constboard(board);
    print("Player O wins!");
