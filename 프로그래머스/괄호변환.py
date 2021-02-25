# 균형잡힌 괄호 문자열인지 체크하는 함수
def isBalanced(s):
    open = 0
    close = 0
    for i in s:
        if i == "(":
            open += 1
        else:
            close += 1
    if open == close:
        return True
    else:
        return False


# 올바른 괄호 문자열인지 체크하는 함수
def isValid(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append("(")
        else:
            if stack:
                stack.pop()
            else:
                return False
    return True


# 괄호 문자열을 거꾸로 바꿔주는 함수
def reverse(s):
    result = ""
    for i in s:
        if i == "(":
            result += ")"
        else:
            result += "("
    return result


def transform(p):
    i = 1
    if p == "":
        return ""
    while 1:
        if isBalanced(p[:i]):
            u = p[:i]
            v = p[i:]
            if isValid(u):
                return u + transform(v)
            else:
                return "(" + transform(v) + ")" + reverse(u[1:-1])
        else:
            i += 1


def solution(p):
    answer = transform(p)
    return answer