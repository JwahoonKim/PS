class Solution:
    def trap(self, height: List[int]) -> int:
        answer = 0
        max_height = max(height)
        max_place = height.index(max_height)
        
        left_max = height[0]
        right_max = height[-1]
        
        # left 돌기
        for i in range(max_place):
            left_max = max(left_max, height[i])
            answer += left_max - height[i]
        
        # right 돌기
        for i in reversed(range(max_place, len(height))):
            right_max = max(right_max, height[i])      
            answer += right_max - height[i]      
        
        return answer