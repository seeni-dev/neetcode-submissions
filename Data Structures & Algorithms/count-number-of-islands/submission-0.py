class Solution:
    dirs = [
        [0,1],
        [0, -1],
        [1, 0],
        [-1, 0]
    ]
    def dfs(self,  grid: List[List[str]], x: int, y: int):
        if x not in range(0, len(grid)) or y not in range(0, len(grid[x])):
            return
        
        if grid[x][y] != "1":
            return
        
        grid[x][y] = "2"
        for d in self.dirs:
            nx, ny = x + d[0], y + d[1]
            self.dfs(grid, nx, ny)


    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for x in range(len(grid)):
            for y in range(0, len(grid[x])):
                if grid[x][y] == "1":
                    count +=1
                    self.dfs(grid, x, y)
        return count