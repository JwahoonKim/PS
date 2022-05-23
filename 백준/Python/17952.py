# 스택으로 과제들을 넣어주는데 [1, 점수, 시간 - 1]로 넣어준다
# 0 나오면 스택의 맨 끝에 있는 숙제의 시간을 -1 해준다
# hw[2] == 0 이면 그 숙제는 tasks 에서 제외시키고 score 를 추가한다.

import sys
input = sys.stdin.readline

n = int(input())
tasks = []
score = 0
for i in range(n):
    hw = list(map(int, input().split()))
    if hw[0] == 1:
        if hw[2] == 1:
            score += hw[1]
        else:
            tasks.append([hw[0], hw[1], hw[2] - 1])
    else:
        if len(tasks) == 0:
            continue
        tasks[-1][2] -= 1
        if tasks[-1][2] == 0:
            complete = tasks.pop(-1)
            score += complete[1]
print(score)
            
    