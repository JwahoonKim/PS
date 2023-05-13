class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        s = s.replace("IV", "IIII")\
            .replace("IX", "VIIII")\
            .replace("XL", "XXXX")\
            .replace("XC", "LXXXX")\
            .replace("CD", "CCCC")\
            .replace("CM", "DCCCC")

        answer = 0
        for c in s:
            answer += roman_map[c]

        return answer


print(Solution().romanToInt("III"))
