class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n =len(board),len(board[0])
        def dfs(i,j):
            board[i][j] ='A'
            for x,y in (i+1,j),(i-1,j),(i,j+1),(i,j-1):
                if 0<=x<m and 0<=y<n and board[x][y]=='O':
                    dfs(x,y)
    
        for i in range(m):
            step =1 if i==0 or i==m-1 else n-1
            for j in range(0,n,step):
                if board[i][j]=='O':
                    dfs(i,j)

        for i in range(m):
            for j in range(n):
                if board[i][j] =='A':
                    board[i][j] ="O"
                elif board[i][j] =="O":
                    board[i][j] ="X"
