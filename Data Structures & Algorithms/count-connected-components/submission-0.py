class Solution:
    def visit(self, i: int, adjancenyList: dict[int,set], visited:set[int]):
        q = [i]
        while q:
            nq = []
            for e in q:
                visited.add(e)
                for neighbour in adjancenyList[e]:
                    if neighbour not in visited:
                        nq.append(neighbour)
            q = nq
        return 
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacenyList = defaultdict(set)
        for edge in edges:
            a,b = edge
            adjacenyList[a].add(b)
            adjacenyList[b].add(a)
        
        visited = set()
        isolated = 0
        for i in range(n):
            if i not in visited:
                isolated +=1
                self.visit(i, adjacenyList, visited)
        return isolated 