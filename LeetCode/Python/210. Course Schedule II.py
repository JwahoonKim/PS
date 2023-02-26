from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        answer = []
        visited = [False] * numCourses
        in_dict = defaultdict(set)

        for cur, pre in prerequisites:
            in_dict[cur].add(pre)

        q = deque()
        for i in range(numCourses):
            if not in_dict[i]:
                q.append(i)

        while q:
            course = q.popleft()
            if visited[course]:
                continue

            visited[course] = True
            answer.append(course)

            for k, v in in_dict.items():
                if course in v:
                    v.remove(course)

            for i in range(numCourses):
                if not in_dict[i] and not visited[i]:
                    q.append(i)

        return [] if len(answer) != numCourses else answer




Solution().findOrder(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]])
