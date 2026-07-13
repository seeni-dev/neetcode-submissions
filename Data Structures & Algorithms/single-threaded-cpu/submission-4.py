import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [
            tasks[i] + [i]
            for i in range(len(tasks))
        ]
        heapq.heapify(tasks)
        if not tasks:
            return []
        t = -1
        res = []
        eligibleTasks = []  
        while tasks or eligibleTasks:
            if not eligibleTasks and t < tasks[0][0]:
                t = tasks[0][0]
            while tasks and tasks[0][0] <= t:
                task = heapq.heappop(tasks)
                heapq.heappush(eligibleTasks, [task[1], task[2]])
            task  = heapq.heappop(eligibleTasks)
            t += task[0]
            res.append(task[1])
        return res
        