number = list(map(int, input().split()))
ans = 0
for i in number:
    ans += i ** 2
ans = ans % 10
print(ans)