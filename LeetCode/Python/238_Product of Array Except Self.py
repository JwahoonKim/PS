class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []

        # left 훑기
        p = 1
        for i in range(len(nums)):
            answer.append(p)
            p *= nums[i]

        # right 훍기
        p = 1
        for i in range(len(nums) - 1, 0 - 1, -1):
            answer[i] *= p
            p *= nums[i]

        return answer