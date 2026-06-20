class Solution:
    max = 2147483647
    dirs = [
        [0, 1],
        [0, -1],
        [1, 0],
        [-1, 0]
    ]
    def traverse(self, grid: List[List[int]],x: int, y: int, distance: int) -> None:
        if x not in range(len(grid)) or y not in range(len(grid[x])):
            return -1
        if grid[x][y] == -1:
            return -1
        if grid[x][y] < distance:
            return
        grid[x][y] = distance
        for d in self.dirs:
            nx, ny = x + d[0], y + d[1]
            self.traverse(grid, nx, ny, distance + 1)
        return

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == 0:
                    self.traverse(grid, x, y, 0)
        