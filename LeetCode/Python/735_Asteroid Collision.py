from collections import deque
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        asteroids = deque(asteroids)
        for asteroid in asteroids:
            if not stack:
                stack.append(asteroid)
                continue

            can_append = True
            while stack and asteroid < 0 < stack[-1]:
                if stack[-1] == -asteroid:
                    stack.pop()
                    can_append = False
                    break
                elif stack[-1] < -asteroid:
                    stack.pop()
                    continue
                elif stack[-1] > -asteroid:
                    can_append = False
                    break

            if can_append:
                stack.append(asteroid)

        return stack
