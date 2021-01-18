n, a, b = map(int, input().split())
Hansoo = max(a, b)
Jimin = min(a, b)
count = 0
while(True):
    # 서로 만난 경우
    if Hansoo % 2 == 0 and Hansoo - Jimin == 1:
        count += 1
        break
    #만나지 않아 한단계 올라가는 경우
    else:
        if Hansoo % 2 == 0:
            Hansoo //= 2
        else:
            Hansoo = (Hansoo + 1) // 2
        if Jimin % 2 == 0:
            Jimin //= 2
        else:
            Jimin = (Jimin + 1) // 2
        count += 1
print(count)

        