import sys
from collections import deque

input = sys.stdin.readline
special_sign = ['(', ')', '[', ']', '.', ',', ';', ':']

def isEqual(s1, s2):
    # 모두 소문자로 변경
    s1 = s1.lower()
    s2 = s2.lower()
    #좌 우 공백 제거
    s1 = s1.strip()
    s2 = s2.strip()
    # 같은 취급받는 특수부호는 하나로 통일 >> 더 좋은 방법 없나 너무 긴데
    s1 = s1.replace('{', '(').replace('[', '(').replace('}',')').replace(']', ']').replace(';', ',')
    s2 = s2.replace('{', '(').replace('[', '(').replace('}',')').replace(']', ']').replace(';', ',')

    #특수문자 좌우는 공백 없애기
    q1 = deque()
    q1.append(s1[0])
    q2 = deque()
    q2.append(s2[0])
    for i in s1[1:]:
        if i in special_sign:
            while(q1[-1] == ' '):
                q1.pop()
            q1.append(i)
        elif i == ' ' and q1[-1] in special_sign:
            continue
        else: q1.append(i)

    for i in s2[1:]:
        if i in special_sign:
            while(q2[-1] == ' '):
                q2.pop()
            q2.append(i)
        elif i == ' ' and q2[-1] in special_sign:
            continue
        else: q2.append(i)
    # 만든 큐로 문자열 다시 만들기.. A   B 와 AB는 다른 문자열이라 다음에 할 처리과정 한번 더 거쳐야해서..
    a = ''
    b = ''
    while(q1):
        a += q1.popleft()
    while(q2):
        b += q2.popleft()      

    # 공백 존재하면 모두 한칸짜리 공백으로 바꾸기
    while(a.find("  ") != -1):
        a = a.replace("  ", " ")
    while(b.find("  ") != -1):
        b = b.replace("  ", " ")

    if a == b:
        return 'equal'
    else: return 'not equal'
    
test_case = int(input())

for i in range(test_case):
    data1 = input()
    data2 = input()
    ans = isEqual(data1, data2) 
    print(f'Data Set {i + 1}: {ans}')
    print('')
