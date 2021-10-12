def check_valid(brackets):
    stack = []
    for bracket in brackets:
        if bracket == '(':
            stack.append(bracket)
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return 'NO'
    if stack:
        return 'NO'
    return 'YES'

for _ in range(int(input())):
    print(check_valid(input()))
    
