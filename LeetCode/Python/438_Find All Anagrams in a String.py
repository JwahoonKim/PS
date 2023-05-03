from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_cnt = [0] * 26
        for c in p:
            p_cnt[ord(c) - ord('a')] += 1

        answer = []
        s_cnt = [0] * 26
        for i in range(len(s)):
            s_cnt[ord(s[i]) - ord('a')] += 1
            if i >= len(p):
                s_cnt[ord(s[i - len(p)]) - ord('a')] -= 1

            if s_cnt == p_cnt:
                answer.append(i - len(p) + 1)

        return answer
