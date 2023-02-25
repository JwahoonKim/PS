from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        answer = 0
        counter = Counter(tasks)

        while 1:
            sub_count = 0
            for task, count in counter.most_common(n + 1):
                sub_count += 1
                answer += 1
                counter[task] -= 1
                if counter[task] == 0:
                    counter.pop(task)

            if not counter:
                break

            answer += (n + 1 - sub_count)

        return answer

Solution().leastInterval(["A","A","A","B","B","B"], 2)