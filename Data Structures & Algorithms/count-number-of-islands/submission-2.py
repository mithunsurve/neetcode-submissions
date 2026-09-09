class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        stack=[]
        island = 0
        ROWS = len(grid)-1
        COLS = len(grid[0])-1
        for i in range(ROWS+1):
            for j in range(COLS+1):
                if grid[i][j] == "1":
                    island +=1
                    stack.append((i,j))
                    while stack:
                        i, j = stack.pop()
                        grid[i][j] = "0"
                        if i>0 and grid[i-1][j]=="1":
                            stack.append((i-1, j))
                        if i<ROWS and grid[i+1][j] == "1":
                            stack.append((i+1, j))
                        if j>0 and grid[i][j-1] == "1":
                            stack.append((i, j-1))
                        if j<COLS and grid[i][j+1] == "1":
                            stack.append((i, j+1))
        return island