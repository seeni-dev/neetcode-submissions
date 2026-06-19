# city -> [destinations]
# 

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ans = None
        def visit(path, ticketsGraph,ticketsCount, currentCity):
            print(f"Visiting {path} with {ticketsCount}")
            nonlocal ans
            path = path + [currentCity]
            if ticketsCount == 0:
                if ans is None:
                    ans = path
                return
            tickets = ticketsGraph.get(currentCity, {})
            cities = sorted(filter(lambda x: tickets.get(x, 0) > 0, tickets.keys()))
            for city in cities:
                ticketsGraph[currentCity][city] -=1
                visit(path, ticketsGraph, ticketsCount - 1, city)
                if ans is not None:
                    return
                ticketsGraph[currentCity][city] +=1
        
        graph = {}
        for ticket in tickets:
            source, dest = ticket 
            if source not in graph:
                graph[source] = {}
            if dest not in graph[source]:
                graph[source][dest] = 0
            graph[source][dest] +=1
        visit([], graph, len(tickets), "JFK")
        return ans