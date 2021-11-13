n, r, c = map(int, input().split())
ans = 0
k = n - 1
# 평면을 4등분해서 좌상단으로 좌표 끌어가기
while k >= 0:
    if r >= 2 ** k:
        ans += 2 ** (2 * k + 1)
        r -= 2 ** k
    if c >= 2 ** k:
        ans += 2 ** (2 * k)    
        c -= 2 ** k
    k -= 1

print(ans)