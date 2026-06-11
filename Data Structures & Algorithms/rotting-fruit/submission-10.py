class Solution:
    dirs = [
        [0,1],
        [0,-1],
        [1,0],
        [-1, 0]
    ]
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = set()
        visited = set()

        totalFruitsCount = 0
        totalRottenCount = 0
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == 2:
                    visited.add((x,y,))
                    rotten.add((x,y,))
                    totalRottenCount +=1
                    totalFruitsCount +=1
                if grid[x][y] == 1:
                    totalFruitsCount += 1
        t = 0
        while rotten:
            print(rotten)
            newlyRotten = set()
            for x,y in rotten:
                for d in self.dirs:
                    nx, ny = x + d[0], y + d[1]
                    tup = (nx, ny,)
                    if nx in range(len(grid)) and ny in range(len(grid[nx])) and t not in visited and grid[nx][ny] == 1:
                        visited.add(tup)
                        newlyRotten.add(tup)
                        grid[nx][ny] = 2
                        totalRottenCount +=1
            rotten = newlyRotten
            if rotten:
                t+=1
        if totalRottenCount != totalFruitsCount:
            return -1
        return t
                    

