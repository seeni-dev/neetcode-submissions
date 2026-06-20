# city -> [destinations]
# 

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ans = None
        def visit(path, ticketsGraph,ticketsCount, currentCity):
            nonlocal ans
            path = path + [currentCity]
            if ticketsCount == 0:
                if ans is None:
                    ans = path
                return
            cities = ticketsGraph.get(currentCity, [])
            for i, city in enumerate(cities):
                del ticketsGraph[currentCity][i]
                visit(path, ticketsGraph, ticketsCount - 1, city)
                if ans is not None:
                    return
                ticketsGraph[currentCity].insert(i, city)
        
        graph = {}
        for ticket in sorted(tickets):
            source, dest = ticket 
            if source not in graph:
                graph[source] = []
            graph[source].append(dest)
        visit([], graph, len(tickets), "JFK")
        return ans