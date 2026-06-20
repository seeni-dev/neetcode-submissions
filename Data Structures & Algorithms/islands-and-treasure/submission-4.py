class Solution:
    max = 2147483647
    dirs = [
        [0, 1],
        [0, -1],
        [1, 0],
        [-1, 0]
    ]
    
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = []
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == 0:
                    q.append([x,y])
        distance = 0
        while q:
            nq = []
            for e in q:
                x,y = e
                for d in self.dirs:
                    nx, ny = x + d[0], y + d[1]
                    if nx not in range(len(grid)) or ny not in range(len(grid[nx])):
                        continue
                    if grid[nx][ny] <= 0:
                        continue
                    if grid[nx][ny] <= distance:
                        continue
                    grid[nx][ny] = distance + 1
                    nq.append([nx,ny])
            q = nq
            distance+=1
        
        
        