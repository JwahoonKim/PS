class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        answer = 0
        g.sort()
        s.sort()

        g_cursor = 0
        g_length = len(g)

        for i in range(len(s)):
            if g_cursor >= g_length:
                break 
            
            if g[g_cursor] <= s[i]:
                answer += 1
                g_cursor += 1
        
        return answer