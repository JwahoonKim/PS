from typing import List


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        answer = 0

        for bomb in bombs:
            bomb[0] -= 1
            bomb[1] -= 1

        def is_detonated(bomb1, bomb2):
            if bomb1[0] == bomb2[0] or bomb1[1] == bomb2[1]:
                return True
            elif abs(bomb1[0] - bomb2[0]) == abs(bomb1[1] - bomb2[1]):
                return True
            else:
                return False

        def dfs(bomb, bombs, cnt, visited):
            nonlocal answer

            if cnt > answer:
                answer = cnt

            for i in range(len(bombs)):
                if not visited[i] and is_detonated(bomb, bombs[i]):
                    visited[i] = True
                    dfs(bombs[i], bombs, cnt + 1, visited)
                    visited[i] = False

        for i in range(len(bombs)):
            visited = [False] * len(bombs)
            visited[i] = True
            dfs(bombs[i], bombs, 1, visited)

        return answer

