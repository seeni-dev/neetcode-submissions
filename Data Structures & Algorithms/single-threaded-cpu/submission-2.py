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
        while tasks:
            eligibleTasks = []
            print("t", t)
            if t < tasks[0][0]:
                t = tasks[0][0]
                print("Jumping to ", t)
            while tasks and tasks[0][0] <= t:
                eligibleTasks.append(heapq.heappop(tasks))
            eligibleTasks.sort(key=lambda x: [x[1], x[2]])
            task  = eligibleTasks[0]
            t += task[1]
            res.append(task[2])
            for task in eligibleTasks[1:]:
                heapq.heappush(tasks, task)
        return res
        