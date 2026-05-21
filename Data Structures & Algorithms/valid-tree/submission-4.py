from collections import defaultdict

class Solution:
    def dfs(self, node: int, parent, edge_map: List[List[int]], visited: set[int]) -> bool:
        if node in visited:
            return False
        
        visited.add(node)
        for neigh in edge_map[node]:
            if neigh != parent:
                if not self.dfs(neigh, node, edge_map, visited):
                    return False
        return True

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        edge_map = defaultdict(set)
        for edge in edges:
            edge_map[edge[0]].add(edge[1])
            edge_map[edge[1]].add(edge[0])
        v = set()
        return self.dfs(0, -1, edge_map, v) and len(v) == n
        