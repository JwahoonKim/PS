class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []

        if len(nums) == 0:
            return [[]]

        for i in range(len(nums)):
            now = nums[i]
            for rest in self.permute(nums[:i] + nums[i + 1:]):
                answer.append([now] + rest)

        return answer