from collections import deque
import sys

input = sys.stdin.readline

operator = {
    '*' : 2,
    '/' : 2,
    '+' : 1,
    '-' : 1
}

a = input().rstrip()
number = deque()
oper = deque()
answer = 0
# 식을 숫자와 operator로 나눠서 리스트에 담기
# 식의 맨 앞이 -일 경우 number[0] = ''이 들어가게 만듬
b = ''
for i in range(len(a)):
    if a[i] not in ['+','-','*','/']:
        b += a[i]
    else:
        if i == 0 and b == '':
            number.append('')
        else:
            number.append(str(int(b)))
        oper.append(a[i])
        b = ''
number.append(str(int(b)))
if number[0] == '':
    number.popleft()
    oper.popleft()
    a = number.popleft()
    number.appendleft(str(-int(a)))

if len(number) == 1:
    answer = int(number[0])
else:
    while(len(number) > 2):
        #oper의 원소 양 끝을 비교했는데 우선순위가 같은경우
        if operator[oper[0]] == operator[oper[-1]]:
            preNum1, preNum2 = number[0], number[1]
            postNum1, postNum2 = number[-2], number[-1]
            if oper[0] in ['+', '-']:
                if oper[0] == '-':
                    preResult = int(preNum1) - int(preNum2)
                else:
                    preResult = int(preNum1) + int(preNum2)
                if oper[-1] == '-':
                    postResult = int(postNum1) - int(postNum2)
                else:
                    postResult = int(postNum1) + int(postNum2)
            else:
                if oper[0] == '*':
                    preResult = int(preNum1) * int(preNum2)
                else:
                    preResult = int(int(preNum1) / int(preNum2))
                if oper[-1] == '*':
                    postResult = int(postNum1) * int(postNum2)
                else:
                    postResult = int(int(postNum1)/ int(postNum2))
            # 앞계산과 뒷계산 결과 비교해서 연산결과 집어넣기
            if preResult >= postResult:
                number.popleft()
                number.popleft()
                oper.popleft()
                number.appendleft(preResult)
            else:
                number.pop()
                number.pop()
                oper.pop()
                number.append(postResult)
        #oper의 원소 양 끝을 비교했는데 우선순위가 앞이 더 큰 경우
        elif operator[oper[0]] > operator[oper[-1]]:
            preNum1, preNum2 = number[0], number[1]
            if oper[0] == '*':
                preResult = int(preNum1) * int(preNum2)
            else:
                preResult = int(int(preNum1) / int(preNum2))
            number.popleft()
            number.popleft()
            oper.popleft()
            number.appendleft(preResult)
        #oper의 원소 양 끝을 비교했는데 우선순위가 뒤가 더 큰 경우
        elif operator[oper[0]] < operator[oper[-1]]:
            postNum1, postNum2 = number[-2], number[-1]
            if oper[-1] == '*':
                postResult = int(postNum1) * int(postNum2)
            else:
                postResult = int(int(postNum1) / int(postNum2))
            number.pop()
            number.pop()
            oper.pop()
            number.append(postResult)
    #마무리 작업 --> 숫자 두개, operator 한개 남은 상황
    if oper[0] == '+':
        answer = int(number[0]) + int(number[1])
    elif oper[0] == '-':
        answer = int(number[0]) - int(number[1])
    elif oper[0] == '*':
        answer = int(number[0]) * int(number[1])
    else:
        answer = int(number[0]) // int(number[1])
print(answer)


