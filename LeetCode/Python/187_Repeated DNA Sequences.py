from collections import defaultdict
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        counter = defaultdict(int)
        for i in range(len(s) - 10 + 1):
            now = s[i:i+10]
            counter[now] += 1

        answer = []
        for c in counter.keys():
            if counter[c] >= 2:
                answer.append(c)

        return answer
