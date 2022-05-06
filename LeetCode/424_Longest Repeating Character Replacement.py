from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        max_window_size = 1
        counter = Counter()
        
        for right in range(len(s)):
            counter[s[right]] += 1
            
            most_count_char = counter.most_common(1)[0][1]
            
            if right - left + 1 - most_count_char > k:
                counter[s[left]] -= 1
                left += 1
            
            max_window_size = max(max_window_size, right - left + 1)
            
        return max_window_size