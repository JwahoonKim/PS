expression = input()
postfix = []
stack = []
operDict = {"*": 2, "/": 2, "+": 1, "-": 1, "(": 0}
# 식에서 알파벳은 다 postfix에 집어넣기
# 연산자라면 위 우선순위에 따라 다음규칙에 맞게 넣는다.
# 1.stack에 넣으려는 연산자의 우선순위가 stack[-1] 의 우선순위보다 높아야 넣을 수 있다.
# 2.그렇지 않으면 본인보다 우선순위가 낮은 연산자가 나올때까지 pop하여 postfix로 옮긴다.
for char in expression:
    if char.isalpha():
        postfix.append(char)
    elif char == ")":
        while stack:
            a = stack.pop()
            if a == "(":
                break
            postfix.append(a)
    elif char == "(":
        stack.append(char)
    elif char in operDict:
        if len(stack) == 0:
            stack.append(char)
        elif operDict[char] > operDict[stack[-1]]:
            stack.append(char)
        else:
            while stack and operDict[char] <= operDict[stack[-1]]:
                a = stack.pop()
                postfix.append(a)
            stack.append(char)
# 위 과정 하고도 남은 스택 원소들 postfix로 옮겨주기
while stack:
    a = stack.pop()
    postfix.append(a)

for i in postfix:
    print(i, end="")
