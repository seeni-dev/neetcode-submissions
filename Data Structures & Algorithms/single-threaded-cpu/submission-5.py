import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [
            tasks[i] + [i]
            for i in range(len(tasks))
        ]
        tasks = sorted(tasks, key=lambda x: x[0])
        if not tasks:
            return []
        t = -1
        tasksIndex = 0
        res = []
        eligibleTasks = []  
        while tasksIndex < len(tasks) or eligibleTasks:
            if not eligibleTasks and t < tasks[tasksIndex][0]:
                t = tasks[tasksIndex][0]
            while tasksIndex < len(tasks) and tasks[tasksIndex][0] <= t:
                task = tasks[tasksIndex]
                tasksIndex +=1
                heapq.heappush(eligibleTasks, [task[1], task[2]])
            task  = heapq.heappop(eligibleTasks)
            t += task[0]
            res.append(task[1])
        return res
        