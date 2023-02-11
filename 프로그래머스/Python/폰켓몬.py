from collections import Counter

def solution(nums):
    freqs = Counter(nums)
    if (len(freqs) < len(nums) // 2):
        return len(freqs)
    return len(nums) // 2

print(solution([3,1,2,3]))