from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        q, q_set = deque(), set()
        answer = 0

        for c in s:
            if c in q_set:
                while q:
                    _c = q.popleft()
                    if _c == c:
                        break
                    q_set.remove(_c)
            
            q.append(c)
            q_set.add(c)
 
            if len(q) > answer:
                answer = len(q)
                
        return answer