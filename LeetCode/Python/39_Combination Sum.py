class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        def dfs(nums, path, sum):
            if sum == target:
                answer.append(path)
                return 

            if sum > target:
                return 
            
            for i, n in enumerate(nums):
                dfs(nums[i:], path + [n], sum + n)


        dfs(candidates, [], 0)

        return answer