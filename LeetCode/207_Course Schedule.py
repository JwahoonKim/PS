from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)

        for x, y in prerequisites:
            graph[x].append(y)

        path = set()
        visited = set()

        def dfs(x):
            if x in path:
                return False
            
            if x in visited:
                return True

            path.add(x)
            for next in graph[x]:
                if not dfs(next):
                    return False
            path.remove(x)
            visited.add(x)

            return True

        for x in list(graph):
            if not dfs(x):
                return False

        return True
            