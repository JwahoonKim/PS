class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if digits == "":
            return []
        
        digit_letter_map = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        
        def dfs(i, str):
            if i == len(digits):
                answer.append(str)
                return 

            letters = digit_letter_map[digits[i]]
            for l in letters:
                dfs(i + 1, str + l)
        
        answer = []
        dfs(0, '')
        
        return answer