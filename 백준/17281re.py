import sys
from collections import deque
from itertools import permutations as p

input = sys.stdin.readline

n = int(input())
answer = 0
hitInfo = [[] for _ in range(9)]

for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(9):
        hitInfo[j].append(arr[j])
tasoons = list(p(range(1,9),8))
for tasoon in tasoons:
    #4번타자는 1번선수가(인덱스로는 0번 선수)
    tasoon = list(tasoon)[:3] + [0] + list(tasoon[3:])
    score = 0
    inning = 0
    out = 0
    ru_1, ru_2, ru_3 = 0, 0, 0
    hit = 0
    while(inning < n):
        if hitInfo[tasoon[hit]][inning] == 0:
            out += 1
            if out == 3:
                inning += 1
                out = 0
                ru_1, ru_2, ru_3 = 0, 0, 0
        else:
            # 1루타
            if hitInfo[tasoon[hit]][inning] == 1:
                score += ru_3
                #한칸씩 밀기
                ru_1, ru_2, ru_3 = 1, ru_1, ru_2 

            # 2루타
            elif hitInfo[tasoon[hit]][inning] == 2:
                score += ru_3 + ru_2
                ru_1, ru_2, ru_3 = 0, 1, ru_1

            # 3루타
            elif hitInfo[tasoon[hit]][inning] == 4:
                score += ru_3 + ru_2 + ru_1
                ru_1, ru_2, ru_3 = 0, 0, 1
            # 홈런
            elif hitInfo[tasoon[hit]][inning] == 4:
                score += ru_3 + ru_2 + ru_1 + 1
                ru_1, ru_2, ru_3 = 0, 0, 0
        hit = (hit + 1) % 9  
    answer = max(answer, score)
print(answer)

    


