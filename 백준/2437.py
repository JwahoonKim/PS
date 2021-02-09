from itertools import combinations as c
from bisect import bisect_right as bs
import sys
input = sys.stdin.readline

n = int(input())
W = list(map(int, input().split()))
dp = [False for _ in range(max(W) + 1)]
for i in W:
    dp[i] = True
W.sort()
answer = 0

if W[0] > 1:
    answer = W[0] - 1
else:
    cur = 2
    while(1):
        if dp[cur] == True:
            cur += 1
            continue
        flag = False
        bsIndex = bs(W, cur)
        for i in range(bsIndex):
            temp = 0
            for j in range(i, bsIndex):
                temp += W[j]
                if temp > cur:
                    break
                elif temp == cur:
                    cur += 1
                    flag = True
                    break
            if flag == True:
                break
        if flag == False:
            answer = cur
            break
print(answer)        


            
