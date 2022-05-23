class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(x, y):
            if grid[x][y] == "0":
                return

            grid[x][y] = "0"

            dx = [1,-1,0,0]
            dy = [0,0,1,-1]

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    dfs(nx, ny)

            return True

        count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        
        return count

