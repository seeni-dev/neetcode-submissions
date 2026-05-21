dirs = [[0,1], [1,0], [-1,0], [0, -1]]
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    res = max(res, self.maxAreaOfIslandHelper(grid, i, j))
        return res
    def maxAreaOfIslandHelper(self, grid: List[List[int]], i, j) -> int:
        if i not in range(0, len(grid)) or j not in range(0, len(grid[i])):
            return 0
        
        if grid[i][j] != 1:
            return 0
        
        grid[i][j] = 2
        res = 1
        for dir in dirs:
            res += self.maxAreaOfIslandHelper(grid, i + dir[0], j + dir[1])
        return res
        