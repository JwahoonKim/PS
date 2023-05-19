from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)

        answer, acc, tmp = 0, 0, 0
        for i in range(len(satisfaction)):
            acc += satisfaction[i]
            tmp += acc
            answer = max(answer, tmp)

        return answer


print(Solution().maxSatisfaction([-1,-8,0,5,-9]))
print(Solution().maxSatisfaction([4,3,2]))
