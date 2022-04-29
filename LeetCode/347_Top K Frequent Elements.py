from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = []
        counter = Counter(nums).most_common(k)

        for num, count in counter:
            answer.append(num)
        return answer