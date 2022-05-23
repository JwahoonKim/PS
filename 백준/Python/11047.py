n, k = map(int, input().split())
coin = []
for i in range(n):
    coin.append(int(input()))
coin.sort(reverse = True)
count = 0
for i in range(n):
    coin_now = coin[i]
    if k == 0:
        break
    if coin_now > k:
        continue
    else:
        mul = k // coin_now
        k -= coin_now * mul
        count += mul

print(count)