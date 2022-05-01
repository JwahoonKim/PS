from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        def compare(x, y):
            a = int(str(x) + str(y))
            b = int(str(y) + str(x))
            return 1 if a < b else -1
        
        nums = sorted(nums, key=cmp_to_key(compare))
        answer = ''.join(map(str, nums))
        
        if answer[0] == '0':
            answer = '0'
        
        return answer