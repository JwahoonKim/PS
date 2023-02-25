from collections import Counter
from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        answer = 0
        counter = Counter(words)
        for k, v in counter.items():
            if counter[k] > 0 and counter[k[::-1]] > 0 and k != k[::-1]:
                mini = min(counter[k], counter[k[::-1]])
                answer += 4 * mini
                counter[k] -= mini
                counter[k[::-1]] -= mini

            elif k == k[::-1] and v > 1:
                if v % 2 == 0:
                    answer += 2 * v
                    counter[k] = 0
                else:
                    answer += 2 * (v - 1)
                    counter[k] = 1

        #
        for k, v in counter.items():
            if k == k[::-1] and v == 1:
                answer += 2
                break

        return answer


# Solution().longestPalindrome(["nn","nn","hg","gn","nn","hh","gh","nn","nh","nh"])
# Solution().longestPalindrome(["ll","lb","bb","bx","xx","lx","xx","lx","ll","xb","bx","lb","bb","lb","bl","bb","bx","xl","lb","xx"])
# print(Solution().longestPalindrome(["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]))