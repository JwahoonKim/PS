from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = []

        for interval in intervals:
            if not result:
                result.append(interval)
            else:
                last = result[-1]
                s1, e1 = last
                s2, e2 = interval
                if s2 <= e1:
                    result.pop()
                    result.append([s1, max(e1, e2)])
                else:
                    result.append([s2, e2])

        return result

Solution().merge([[1,3],[2,6],[8,10],[15,18]])