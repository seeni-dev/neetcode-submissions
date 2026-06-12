class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjacenyList = defaultdict(set)
        depCount = defaultdict(lambda : 0)
        for a,b in prerequisites:
            adjacenyList[b].add(a)
            depCount[a] += 1
        
        q = []
        for i in range(numCourses):
            if depCount[i] == 0:
                q.append(i)
        coursesTakenCount = 0
        res = []
        while q:
            nq = []
            for courseTaken in q:
                coursesTakenCount += 1
                res.append(courseTaken)
                for nextCourse in adjacenyList[courseTaken]:
                    depCount[nextCourse] -=1
                    if depCount[nextCourse] == 0:
                        nq.append(nextCourse)
            q = nq
        if coursesTakenCount == numCourses:
            return res
        else:
            return []