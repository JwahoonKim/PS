n = int(input())
W = list(map(int, input().split()))
W.sort()
sum = 0
# W의 i행까지의 합 + 1이 W[i + 1]보다 작으면 sum(W[:i+1]) + 1은 못만들고 이것이 답
for i in range(n):
    if sum + 1 < W[i]:
        break
    else:
        sum += W[i]
print(sum + 1)