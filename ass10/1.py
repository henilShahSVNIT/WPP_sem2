'''Consider the 8 queen's problem, it is a 8*8 chess board where you need to 
place queens 
according to the following constraints. 
a. Each row should have exactly only one queen. 
b. Each column should have exactly only one queen. 
c. No queens are attacking each other.''' 
 
import numpy as np 
 
n=int(input("enter the value of n: ")) 
def isSafe(board,row,col,n): 
    for j in range(n): 
        if board[row][j]==1: 
            return False 
    for i in range(n): 
        if board[i][col]==1: 
            return False 
    i,j=row,col 
    while i>=0 and j>=0: 
        if board[i][j]==1: 
            return False 
        i-=1 
        j-=1 
    i,j=row,col 
    while i>=0 and j<n: 
        if board[i][j]==1: 
            return False 
        i-=1 
        j+=1 
 
    return True 
 
def nQueen(board,row,n,ans): 
    if row==n: 
        ans.append(board.copy()) 
        return 
 
    for j in range(n): 
        if isSafe(board,row,j,n): 
            board[row][j]=1 
            nQueen(board,row+1,n,ans) 
            board[row][j]=0 
    # return ans     
 
board=np.zeros((n,n), dtype=int) 
ans=[] 
nQueen(board,0,n,ans) 
for an in ans: 
    print(an) 
    print()