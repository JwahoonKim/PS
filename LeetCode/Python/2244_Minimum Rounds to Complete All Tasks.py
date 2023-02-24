from collections import Counter
from typing import List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counter = Counter(tasks)
        answer = 0
        for k, v in counter.items():
            if v == 1:
                return -1
            answer += self.calc(v)
        return answer

    def calc(self, v):
        if v % 3 == 0:
            return v // 3
        return v // 3 + 1


print(Solution().minimumRounds([2,2,3,3,2,4,4,4,4,4]))
print(Solution().minimumRounds([2,3,3]))