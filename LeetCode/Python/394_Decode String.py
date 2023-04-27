class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c == "[" or c.isalnum():
                stack.append(c)

            elif c == "]":
                tmp = ""
                while 1:
                    last = stack.pop()
                    if last == "[":
                        break
                    tmp = last + tmp

                num = ""
                while stack and stack[-1].isdigit():
                    last = stack.pop()
                    num = last + num

                stack.append(int(num) * tmp)

        return ''.join(stack)


print(Solution().decodeString("3[a]2[bc]"))
Solution().decodeString("3[a2[c]]")
Solution().decodeString("2[abc]3[cd]ef")