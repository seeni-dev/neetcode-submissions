from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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
        while q:
            nq = []
            for courseTaken in q:
                coursesTakenCount += 1
                for nextCourse in adjacenyList[courseTaken]:
                    depCount[nextCourse] -=1
                    if depCount[nextCourse] == 0:
                        nq.append(nextCourse)
            q = nq
        return coursesTakenCount == numCourses

