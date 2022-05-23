from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, stack_set, stack = Counter(s), set(), []

        for c in s:
            counter[c] -= 1
            
            if c in stack_set:
                continue

            while stack and stack[-1] > c and counter[stack[-1]] != 0:
                stack_set.remove(stack.pop())
            
            stack.append(c)
            stack_set.add(c)

        return ''.join(stack)
