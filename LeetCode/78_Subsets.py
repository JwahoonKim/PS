class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def dfs(path, index):
            answer.append(path)

            for i in range(index, len(nums)):
                dfs(path + [nums[i]], i + 1)

        dfs([], 0)
        return answer
