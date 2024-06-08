def analyseBoard(board):
  c = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
  for i in range(0,8):
    if(board[c[i][0]]!=0 and
       board[c[i][0]] == board[c[i][1]] and
       board[c[i][1]] == board[c[i][2]]):
      return board[c[i][0]]

  return 0

def constBoard(board):
  print("The current board of the Game:")
  for i in range(0, 9):
    if(i>0 and i%3==0):
        print("\n\n")
    if(board[i]==0):
        print(" _ ", end=" ")
    if(board[i]==-1):
        print(" X ", end=" ")
    if(board[i]==1):
        print(" O ", end=" ")

  print("\n\n")

def user1Turn(board):
    pos=input("Enter 'X' on posotion[1, 9]")
    pos=int(pos)
    if(board[pos-1]!=0):
        print("Wrong move!")
        exit(0)
    board[pos-1]=-1


def user2Turn(board):
    pos=input("Enter 'O' on posotion[1, 9]")
    pos=int(pos)
    if(board[pos-1]!=0):
        print("Wrong move!")
        exit(0)
    board[pos-1]=1

def compTurn(board):
  pos=-1
  value=-2
  for i in range(0,9):
    if(board[i]==0):
      board[i]=1
      score= -minmax(board, -1)
      board[i]=0
      if(score>value):
        value=score
        pos=i
  board[pos]=1

def minmax(board, player):
    x=analyseBoard(board)
    if(x!=0):
        return(x*player)
    pos=-1
    value=-2
    for i in range(0, 9):
      if(board[i]==0):
        board[i]=player
        score=minmax(board, player*-1)
        board[i]=0
        if(score>value):
          value=score
          pos=i
    if(pos==-1):
        return 0
    return value

def main():
  choice=input("Enter 1 for Single Player or 2 for Mult-Platyers")
  choice=int(choice)
  board=[0, 0, 0, 0, 0, 0, 0, 0, 0]
  if(choice==1):
    print("You have chosed Single Player mode where You are going to play with Computer \n")
    print("'O' Represent Computer and 'X' Represent You as player\n")
    player = input("Enter '1' to move first or '2' to move second:\n")
    player=int(player)
    for i in range(0, 9):
      if(analyseBoard(board)!=0):
        break
      if((i+player)%2==0):
        compTurn(board)
      else:
        constBoard(board)
        user1Turn(board)
  else:
    for i in range(0, 9):
      if(analyseBoard(board)!=0):
        break

      if(i%2==0):
        constBoard(board)
        user1Turn(board)
      else:
        constBoard(board)
        user2Turn(board)
  constBoard(board)
  if(analyseBoard(board)==0):
    print("Draw")
  elif(analyseBoard(board)==-1):
    print("Player1 Win the Game")
  else:
    print("Player2 Win the Game")
