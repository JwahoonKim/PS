from collections import deque

# 괄호가 유효한지 체크하는 함수
def isValid(bracketStirng):
    stack = []
    dic = {')' : '(', ']' : '['}
    for bracket in bracketStirng:
        if bracket in dic.values():
            stack.append(bracket)
        elif bracket in dic:
            if len(stack) == 0 or stack[-1] != dic[bracket]:
                return False
            elif stack[-1] == dic[bracket]:
                stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False

#괄호로 계산하는 함수
def calculate(bracketString):
    dic = {')' : '(', ']' : '['}
    stack = []

    for bracket in bracketString:
        if bracket in dic.values():
            stack.append(bracket)
        elif bracket == ')':
            if stack[-1] == '(':
                stack[-1] = 2
            else:
                temp = 0
                while(1):
                    if stack[-1] == '(':
                        temp *= 2
                        stack[-1] = temp
                        break
                    else:
                        temp += stack[-1]
                        stack = stack[:-1]

        elif bracket == ']':
            if stack[-1] == '[':
                stack[-1] = 3
            else:
                temp = 0
                while(1):
                    if stack[-1] == '[':
                        temp *= 3
                        stack[-1] = temp
                        break
                    else:
                        temp += stack[-1]
                        stack = stack[:-1]
    return sum(stack)

if __name__ == '__main__':
    brackets = input()
    if isValid(brackets) == False:
        print(0)
    else:
        answer = calculate(brackets)
        print(answer) 



