class Solution:
    dirs = [
        [0,1],
        [0, -1],
        [1, 0],
        [-1, 0]
    ]

    def traverse(self, heights: List[List[int]], q):
        visitedSet = set()
        # Traverse
        while q:
            nq = []
            for e in q:
                if e in visitedSet:
                    continue
                visitedSet.add(e)
                x, y = e
                for d in self.dirs:
                    nx,ny = x+d[0],y+d[1]
                    if nx not in range(len(heights)) or ny not in range(len(heights[nx])):
                        continue
                    t = (nx, ny,)
                    if heights[nx][ny] >= heights[x][y] and t not in visitedSet:
                        nq.append(t)
            q = nq
        return visitedSet

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        for i in range(len(heights)):
            pacific.add((i,0,))
            atlantic.add((i,len(heights[i])-1,))

        for i in range(len(heights[0])):
            pacific.add((0, i, ))
            atlantic.add((len(heights)-1, i, ))
        
        # print(pacific, atlantic)
        # print(self.traverse(heights, pacific))
        # print(self.traverse(heights, atlantic))
        res = self.traverse(heights, pacific) & self.traverse(heights, atlantic)
        return list(map(lambda x: [x[0], x[1]], res))

        