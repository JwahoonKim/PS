def solution(s):
    answer = 0
    for i in range(len(s)):
        s = rotate_left(s)
        if isValid(s):
            answer += 1
    return answer

def isValid(s):
    stack = []
    bracket = {'[' : ']',
                    '(' : ')',
                    '{' : '}'}
    for i in s:
        if i in bracket.keys():
            stack.append(i)
        else:
            if not stack:
                return False
            else:
                top = stack.pop()
                if bracket[top] == i:
                    continue
                else:
                    return False
    if stack:
        return False
    return True

def rotate_left(s):
    return s[1:] + s[0]